// Interactive globe viewer for an openEO SAR result (COG), built with deck.gl.
// Tiles are read straight from the COG with geotiff.js and reprojected UTM -> Web Mercator in the browser.
import { fromUrl, Pool } from "https://esm.sh/geotiff@2.1.3";
import proj4 from "https://esm.sh/proj4@2.23.0";

const TILE = 256;
// draw order, not depth, decides stacking: avoids z-fighting between tile levels on the globe
const FLAT = { depthCompare: "always", depthWriteEnabled: false };
// deck.gl's UMD bundle registers itself with RequireJS instead of window.deck when a page already loads require.js
// (e.g. Jupyter widget output), so AMD is hidden while the script loads.
async function loadDeck() {
  if (window.deck) return window.deck;
  const amd = window.define;
  window.define = undefined;
  try {
    await new Promise((resolve, reject) => {
      const el = document.createElement("script");
      el.src = "https://unpkg.com/deck.gl@9.1.12/dist.min.js";
      el.onload = resolve;
      el.onerror = () => reject(new Error("Could not load deck.gl"));
      document.head.appendChild(el);
    });
  } finally {
    window.define = amd;
  }
  return window.deck;
}
const deck = await loadDeck();
const {
  Deck, _GlobeView: GlobeView, MapView, TileLayer, BitmapLayer, SolidPolygonLayer, LinearInterpolator,
} = deck;

const TERRAIN_URL = "https://s3.amazonaws.com/elevation-tiles-prod/terrarium/{z}/{x}/{y}.png";
const MESH_N = 32; // mesh segments per tile edge
const mercY = (lat) => Math.log(Math.tan(Math.PI / 4 + (lat * Math.PI) / 360));
const invMercY = (y) => (2 * Math.atan(Math.exp(y)) - Math.PI / 2) * (180 / Math.PI);

// BitmapLayer whose tessellated mesh carries elevation, so the image is draped over terrain on globe and flat map.
class TerrainBitmapLayer extends BitmapLayer {
  _createMesh() {
    const { heights, exaggeration, bounds } = this.props;
    if (!heights) return super._createMesh();
    const [west, south, east, north] = bounds;
    const n = MESH_N, cnt = n + 1;
    const yN = mercY(north), yS = mercY(south);
    const positions = new Float64Array(cnt * cnt * 3);
    const texCoords = new Float32Array(cnt * cnt * 2);
    const indices = new Uint32Array(n * n * 6);
    let k = 0;
    for (let u = 0; u < cnt; u++) {
      for (let v = 0; v < cnt; v++) {
        const vert = u * cnt + v; // v runs south -> north like deck's own mesh
        const lat = invMercY(yS + (v / n) * (yN - yS));
        positions[vert * 3] = west + (u / n) * (east - west);
        positions[vert * 3 + 1] = lat;
        positions[vert * 3 + 2] = heights[(n - v) * cnt + u] * exaggeration;
        texCoords[vert * 2] = u / n;
        texCoords[vert * 2 + 1] = 1 - v / n;
        if (u > 0 && v > 0) {
          indices[k++] = vert - cnt; indices[k++] = vert - cnt - 1; indices[k++] = vert - 1;
          indices[k++] = vert - cnt; indices[k++] = vert - 1; indices[k++] = vert;
        }
      }
    }
    return { vertexCount: indices.length, positions, indices, texCoords };
  }

  updateState(params) {
    const { props, oldProps } = params;
    super.updateState(params);
    const changed = props.heights !== oldProps.heights || props.exaggeration !== oldProps.exaggeration;
    if (changed && props.bounds === oldProps.bounds && this.state.model) {
      const mesh = this._createMesh();
      this.state.model.setVertexCount(mesh.vertexCount);
      const am = this.getAttributeManager();
      for (const key of ["indices", "positions", "texCoords"]) am.invalidate(key);
      this.setState({ mesh });
    }
  }
}
TerrainBitmapLayer.layerName = "TerrainBitmapLayer";
TerrainBitmapLayer.defaultProps = { ...BitmapLayer.defaultProps, heights: null, exaggeration: 1 };

const elevationCache = new Map();
// Decoded 256x256 Terrarium tile (meters), cached per tile.
function elevationTile(z, x, y) {
  const key = `${z}/${x}/${y}`;
  if (!elevationCache.has(key)) {
    const url = TERRAIN_URL.replace("{z}", z).replace("{x}", x).replace("{y}", y);
    elevationCache.set(key, fetch(url).then((r) => r.blob()).then(createImageBitmap).then((bmp) => {
      const c = new OffscreenCanvas(256, 256);
      const ctx = c.getContext("2d", { willReadFrequently: true });
      ctx.drawImage(bmp, 0, 0);
      const px = ctx.getImageData(0, 0, 256, 256).data;
      const h = new Float32Array(256 * 256);
      for (let i = 0; i < h.length; i++) h[i] = Math.max(0, px[i * 4] * 256 + px[i * 4 + 1] + px[i * 4 + 2] / 256 - 32768);
      return h;
    }).catch(() => { elevationCache.delete(key); return null; }));
  }
  return elevationCache.get(key);
}

// Heights on the (MESH_N+1)^2 grid of a web-mercator tile, sampled from the Terrarium tile (or its ancestor).
async function tileHeights({ x, y, z }) {
  const ze = Math.min(z, 12);
  const f = 2 ** (z - ze);
  const tile = await elevationTile(ze, Math.floor(x / f), Math.floor(y / f));
  if (!tile) return null;
  const ox = (x % f) / f, oy = (y % f) / f;
  const out = new Float32Array((MESH_N + 1) ** 2);
  for (let r = 0; r <= MESH_N; r++) {
    for (let c = 0; c <= MESH_N; c++) {
      const px = Math.min(255, Math.round((ox + c / MESH_N / f) * 255));
      const py = Math.min(255, Math.round((oy + r / MESH_N / f) * 255));
      out[r * (MESH_N + 1) + c] = tile[py * 256 + px];
    }
  }
  return out;
}

const COLORMAPS = {
  Gray: ["#000000", "#ffffff"],
  Viridis: ["#440154", "#472d7b", "#3b528b", "#2c728e", "#21918c", "#28ae80", "#5ec962", "#addc30", "#fde725"],
  Magma: ["#000004", "#180f3e", "#451077", "#721f81", "#9f2f7f", "#cd4071", "#f1605d", "#fd9567", "#fec98d", "#fcfdbf"],
  Turbo: ["#30123b", "#4662d7", "#36aaf9", "#1ae4b6", "#72fe5e", "#c8ef34", "#faba39", "#f66b19", "#ca2a04", "#7a0403"],
  Cividis: ["#00204d", "#31446b", "#666970", "#958f78", "#cbba69", "#ffea46"],
};

const BANDS = {
  VV: { label: "VV", unit: "dB", range: [-26, 4], init: [-18, -4] },
  VH: { label: "VH", unit: "dB", range: [-34, -2], init: [-26, -10] },
  RATIO: { label: "VH − VV", unit: "dB", range: [-24, 0], init: [-12, -2] },
};

const BASEMAPS = {
  Dark: { url: "https://services.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Dark_Gray_Base/MapServer/tile/{z}/{y}/{x}", maxZoom: 16 },
  Satellite: { url: "https://services.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}", maxZoom: 17 },
};

const hexToRgb = (h) => [1, 3, 5].map((i) => parseInt(h.slice(i, i + 2), 16));
function buildLut(name) {
  const stops = COLORMAPS[name].map(hexToRgb);
  const lut = new Uint8ClampedArray(256 * 3);
  for (let i = 0; i < 256; i++) {
    const t = (i / 255) * (stops.length - 1);
    const k = Math.min(Math.floor(t), stops.length - 2);
    const f = t - k;
    for (let c = 0; c < 3; c++) lut[i * 3 + c] = stops[k][c] * (1 - f) + stops[k + 1][c] * f;
  }
  return lut;
}

const toDb = (v) => 10 * Math.log10(v);

// value of the selected band in dB from raw linear [VV, VH]
// cfg.db: the COG already holds dB values; cfg.bands: band names present in the COG (default VV, VH)
function bandValue(band, vv, vh, db) {
  const conv = db ? (v) => v : toDb;
  const ok = (v) => (db ? Number.isFinite(v) : v > 0);
  if (band === "VV") return ok(vv) ? conv(vv) : NaN;
  if (band === "VH") return ok(vh) ? conv(vh) : NaN;
  return ok(vv) && ok(vh) ? conv(vh) - conv(vv) : NaN;
}

export async function createViewer(root, cfg) {
  const $ = (s) => root.querySelector(s);
  const status = $(".sar-status");
  const setStatus = (msg, kind = "") => {
    status.textContent = msg;
    status.dataset.kind = kind;
    status.hidden = !msg;
  };
  setStatus("Opening COG…", "busy");

  const utm = proj4("WGS84", cfg.proj);
  const db = !!cfg.db;
  const bandNames = cfg.bands ?? ["VV", "VH"];
  const nSamples = bandNames.length;
  const bandOpts = $("[data-ctl=band]");
  for (const o of bandOpts.options) o.hidden = o.disabled = !(o.value === "RATIO" ? nSamples > 1 : bandNames.includes(o.value));
  bandOpts.value = bandNames[0];
  const pool = new Pool();
  const sources = cfg.sources ?? [{ label: "", dates: { "": cfg.url } }];
  const dates = Object.keys(sources[0].dates).sort();
  const compare = sources.length > 1;

  const opened = new Map(); // url -> Promise of the opened COG
  function openCog(url) {
    if (!opened.has(url)) {
      opened.set(url, (async () => {
        const tiff = await fromUrl(url);
        const count = await tiff.getImageCount();
        const images = [];
        for (let i = 0; i < count; i++) {
          const im = await tiff.getImage(i);
          // openEO writes single-valued SampleFormat/BitsPerSample tags for a multi-band file; repeat them per band
          for (const tag of ["SampleFormat", "BitsPerSample"]) {
            const v = Array.from(im.fileDirectory[tag] ?? []);
            if (v.length === 1) Object.defineProperty(im.fileDirectory, tag, { value: Array(im.getSamplesPerPixel()).fill(v[0]), configurable: true });
          }
          images.push(im);
        }
        const base = images[0];
        const [ox, oy] = base.getOrigin();
        const [rx, ry] = base.getResolution();
        const W0 = base.getWidth();
        const H0 = base.getHeight();
        const bbox = [ox, oy + ry * H0, ox + rx * W0, oy]; // minx, miny, maxx, maxy in the COG's CRS
        const corners = [[bbox[0], bbox[1]], [bbox[2], bbox[1]], [bbox[2], bbox[3]], [bbox[0], bbox[3]]].map((p) => utm.inverse(p));
        const lons = corners.map((c) => c[0]);
        const lats = corners.map((c) => c[1]);
        return { images, ox, oy, rx, ry, W0, H0, extent: [Math.min(...lons), Math.min(...lats), Math.max(...lons), Math.max(...lats)] };
      })().catch((e) => { opened.delete(url); throw e; }));
    }
    return opened.get(url);
  }
  const extent = (await openCog(sources[0].dates[dates[dates.length - 1]])).extent;

  // Picks the coarsest image (overview) that is still at least as detailed as the screen needs.
  const pickImage = ({ images, rx, W0 }, west, east, lat) => {
    const target = ((east - west) / TILE) * 111320 * Math.cos((lat * Math.PI) / 180);
    let best = 0;
    for (let i = 0; i < images.length; i++) if (Math.abs(rx) * (W0 / images[i].getWidth()) <= target * 1.2) best = i;
    return images[best];
  };

  // Reads the bands, mapping the file's nodata value to NaN.
  async function readBands(img, opts) {
    const rs = await img.readRasters({ ...opts, samples: bandNames.map((_, i) => i), pool });
    const nd = img.getGDALNoData();
    return Array.from(rs, (a) => {
      if (nd !== null && !Number.isNaN(nd)) for (let i = 0; i < a.length; i++) if (a[i] === nd) a[i] = NaN;
      return a;
    });
  }

  // Reads one web-mercator tile from a COG: returns Float32Array [vv, vh] interleaved, NaN where there is no data.
  async function readTile(cog, tb) {
    const { ox, oy, rx, ry, W0, H0 } = cog;
    const { west, south, east, north } = tb;
    if (east < cog.extent[0] || west > cog.extent[2] || north < cog.extent[1] || south > cog.extent[3]) return null;
    const img = pickImage(cog, west, east, (north + south) / 2);
    const iw = img.getWidth();
    const ih = img.getHeight();
    const sx = iw / W0;
    const sy = ih / H0;

    // footprint of the tile in the COG's CRS
    const pts = [];
    for (let i = 0; i <= 4; i++) for (let j = 0; j <= 4; j++) {
      pts.push(utm.forward([west + ((east - west) * i) / 4, south + ((north - south) * j) / 4]));
    }
    const minx = Math.min(...pts.map((p) => p[0])), maxx = Math.max(...pts.map((p) => p[0]));
    const miny = Math.min(...pts.map((p) => p[1])), maxy = Math.max(...pts.map((p) => p[1]));
    let x0 = Math.floor(((minx - ox) / rx) * sx) - 1, x1 = Math.ceil(((maxx - ox) / rx) * sx) + 1;
    let y0 = Math.floor(((maxy - oy) / ry) * sy) - 1, y1 = Math.ceil(((miny - oy) / ry) * sy) + 1;
    x0 = Math.max(0, x0); y0 = Math.max(0, y0); x1 = Math.min(iw, x1); y1 = Math.min(ih, y1);
    if (x1 <= x0 || y1 <= y0) return null;

    const rasters = await readBands(img, { window: [x0, y0, x1, y1] });
    const ww = x1 - x0;
    const out = new Float32Array(TILE * TILE * 2).fill(NaN);
    const yN = mercY(north), yS = mercY(south);
    let any = false;
    for (let py = 0; py < TILE; py++) {
      const lat = invMercY(yN + ((py + 0.5) / TILE) * (yS - yN));
      for (let px = 0; px < TILE; px++) {
        const lon = west + ((px + 0.5) / TILE) * (east - west);
        const [ux, uy] = utm.forward([lon, lat]);
        const ix = Math.floor(((ux - ox) / rx) * sx) - x0;
        const iy = Math.floor(((uy - oy) / ry) * sy) - y0;
        if (ix < 0 || iy < 0 || ix >= ww || iy >= y1 - y0) continue;
        const k = iy * ww + ix;
        const o = (py * TILE + px) * 2;
        out[o] = rasters[0][k];
        out[o + 1] = rasters[1] ? rasters[1][k] : NaN;
        any = true;
      }
    }
    return any ? out : null;
  }

  // One raw tile per source for a date; shared by the main and the comparison map so each tile is read once.
  const tileCache = new Map();
  function tileRaws(tb, index, date) {
    const key = `${date}|${index.z}|${index.x}|${index.y}`;
    let p = tileCache.get(key);
    if (!p) {
      p = Promise.all(sources.map(async (src) => (src.dates[date] ? readTile(await openCog(src.dates[date]), tb) : null)));
      p.catch(() => tileCache.delete(key));
      tileCache.set(key, p);
      if (tileCache.size > 300) tileCache.delete(tileCache.keys().next().value);
    }
    return p;
  }

  // ---------- state ----------
  const state = {
    band: bandNames[0], cmap: "Magma", min: BANDS[bandNames[0]].init[0], max: BANDS[bandNames[0]].init[1], opacity: 0.95,
    basemap: "Dark", date: dates[dates.length - 1], split: 0.5, globe: false, terrain: true, exaggeration: 3, lut: buildLut("Magma"), version: 0,
  };
  const canvasCache = new WeakMap();

  function renderCanvas(raw) {
    const key = `${state.band}|${state.min}|${state.max}|${state.cmap}`;
    const cached = canvasCache.get(raw);
    if (cached && cached.key === key) return cached.canvas;
    const canvas = document.createElement("canvas"); // new object so the layer re-uploads the texture
    canvas.width = canvas.height = TILE;
    const ctx = canvas.getContext("2d");
    const imgData = ctx.createImageData(TILE, TILE);
    const d = imgData.data;
    const span = state.max - state.min;
    for (let i = 0; i < TILE * TILE; i++) {
      const v = bandValue(state.band, raw[i * 2], raw[i * 2 + 1], db);
      if (Number.isNaN(v)) continue;
      const t = Math.max(0, Math.min(1, (v - state.min) / span));
      const l = Math.round(t * 255) * 3;
      d[i * 4] = state.lut[l]; d[i * 4 + 1] = state.lut[l + 1]; d[i * 4 + 2] = state.lut[l + 2]; d[i * 4 + 3] = 255;
    }
    ctx.putImageData(imgData, 0, 0);
    canvasCache.set(raw, { key, canvas });
    return canvas;
  }

  // ---------- histogram from a coarse overview ----------
  let sample = null; // Float32 [vv, vh] of the first source
  async function loadSample() {
    const { images } = await openCog(sources[0].dates[state.date]);
    const overview = images.find((im) => im.getWidth() <= 700) || images[images.length - 1];
    const r = await readBands(overview, {});
    sample = { vv: r[0], vh: r[1] ?? r[0].map(() => NaN) };
    drawHistogram();
  }

  const hist = $(".sar-hist");
  function histogramData() {
    if (!sample) return null;
    const [lo, hi] = BANDS[state.band].range;
    const bins = new Array(80).fill(0);
    let n = 0;
    const vals = [];
    for (let i = 0; i < sample.vv.length; i++) {
      const v = bandValue(state.band, sample.vv[i], sample.vh[i], db);
      if (Number.isNaN(v)) continue;
      vals.push(v);
      const b = Math.floor(((v - lo) / (hi - lo)) * bins.length);
      if (b >= 0 && b < bins.length) { bins[b]++; n++; }
    }
    vals.sort((a, b) => a - b);
    return { bins, n, p2: vals[Math.floor(vals.length * 0.02)], p98: vals[Math.floor(vals.length * 0.98)] };
  }

  function drawHistogram() {
    const h = histogramData();
    const dpr = window.devicePixelRatio || 1;
    const w = hist.clientWidth, ht = hist.clientHeight;
    hist.width = w * dpr; hist.height = ht * dpr;
    const ctx = hist.getContext("2d");
    ctx.scale(dpr, dpr);
    ctx.clearRect(0, 0, w, ht);
    if (!h) return;
    const [lo, hi] = BANDS[state.band].range;
    const peak = Math.max(...h.bins);
    const bw = w / h.bins.length;
    h.bins.forEach((c, i) => {
      const v = lo + ((i + 0.5) / h.bins.length) * (hi - lo);
      const t = Math.max(0, Math.min(1, (v - state.min) / (state.max - state.min)));
      const inside = v >= state.min && v <= state.max;
      const l = Math.round(t * 255) * 3;
      ctx.fillStyle = inside ? `rgb(${state.lut[l]},${state.lut[l + 1]},${state.lut[l + 2]})` : "rgba(255,255,255,0.18)";
      const bh = Math.sqrt(c / peak) * (ht - 4);
      ctx.fillRect(i * bw + 0.5, ht - bh, Math.max(1, bw - 1), bh);
    });
    state.auto = [h.p2, h.p98];
  }

  // ---------- controls ----------
  const el = {
    band: $("[data-ctl=band]"), cmap: $("[data-ctl=cmap]"), min: $("[data-ctl=min]"), max: $("[data-ctl=max]"),
    opacity: $("[data-ctl=opacity]"), minOut: $("[data-out=min]"), maxOut: $("[data-out=max]"),
    base: $("[data-ctl=basemap]"), proj: $("[data-ctl=projection]"), auto: $("[data-ctl=auto]"),
    legend: $(".sar-legend-bar"), legMin: $("[data-out=legmin]"), legMax: $("[data-out=legmax]"), legTitle: $("[data-out=legtitle]"),
    fly: $("[data-ctl=fly]"), terrain: $("[data-ctl=terrain]"), exag: $("[data-ctl=exaggeration]"),
    exagRow: $("[data-row=exaggeration]"), exagOut: $("[data-out=exaggeration]"),
  };
  el.cmap.innerHTML = Object.keys(COLORMAPS).map((n) => `<option>${n}</option>`).join("");
  el.cmap.value = state.cmap;
  el.base.innerHTML = Object.keys(BASEMAPS).map((n) => `<option>${n}</option>`).join("");

  function syncControls(resetRange) {
    const b = BANDS[state.band];
    if (resetRange) [state.min, state.max] = b.init;
    for (const k of ["min", "max"]) { el[k].min = b.range[0]; el[k].max = b.range[1]; el[k].step = 0.5; }
    el.min.value = state.min; el.max.value = state.max;
    el.minOut.textContent = `${(+state.min).toFixed(1)} dB`;
    el.maxOut.textContent = `${(+state.max).toFixed(1)} dB`;
    el.legMin.textContent = (+state.min).toFixed(1);
    el.legMax.textContent = (+state.max).toFixed(1);
    el.legTitle.textContent = `${b.label} (${b.unit})`;
    el.legend.style.background = `linear-gradient(to right, ${COLORMAPS[state.cmap].join(",")})`;
  }

  // ---------- deck ----------
  const tooltip = $(".sar-tooltip");
  const viewState = { longitude: cfg.center[0], latitude: 30, zoom: 1.2, minZoom: 0, maxZoom: 15, pitch: 0, bearing: 0 };
  let currentView = viewState;
  let loadingTimer;

  // which = "top": only the comparison source, drawn by the second deck above the first
  function layers(which) {
    const bm = BASEMAPS[state.basemap];
    const t3d = state.terrain;
    const exag = state.exaggeration;
    // with relief, depth decides visibility; the SAR drape is biased slightly towards the camera to avoid z-fighting
    const depth = t3d ? { depthCompare: "less-equal", depthWriteEnabled: true } : FLAT;
    const cogDepth = t3d ? { ...depth, depthBias: -50, depthBiasSlopeScale: -2 } : FLAT;
    const Drape = t3d ? TerrainBitmapLayer : BitmapLayer;
    const bmLayer = new TileLayer({
      id: `basemap-${state.basemap}${t3d ? "-3d" : ""}`, data: bm.url, minZoom: 0, maxZoom: bm.maxZoom, tileSize: 256,
      refinementStrategy: t3d ? "no-overlap" : "best-available",
      ...(t3d && {
        getTileData: async ({ url, index, signal }) => {
          const [img, heights] = await Promise.all([
            fetch(url, { signal }).then((r) => r.blob()).then(createImageBitmap), tileHeights(index),
          ]);
          return { img, heights };
        },
      }),
      renderSubLayers: (p) => {
        const { west, south, east, north } = p.tile.bbox;
        return new Drape(p, {
          data: null, image: t3d ? p.data?.img : p.data, heights: t3d ? p.data?.heights : null, exaggeration: exag,
          bounds: [west, south, east, north], parameters: depth,
        });
      },
      updateTriggers: { renderSubLayers: [exag] },
    });
    const cogLayer = (i) => new TileLayer({
      id: `${t3d ? "cog-3d" : "cog"}-${i}`, minZoom: 3, maxZoom: 13, tileSize: TILE, extent,
      refinementStrategy: t3d ? "no-overlap" : "best-available",
      getTileData: async ({ bbox: tb, index }) => {
        try {
          const [raws, heights] = await Promise.all([tileRaws(tb, index, state.date), t3d ? tileHeights(index) : null]);
          return raws[i] && { raw: raws[i], raws, heights };
        } catch (e) {
          console.warn(e);
          setStatus("Data unavailable — the COG could not be read.", "error");
          return null;
        }
      },
      renderSubLayers: (p) => {
        if (!p.data) return null;
        const { west, south, east, north } = p.tile.bbox;
        return new Drape(p, {
          data: null, image: renderCanvas(p.data.raw), heights: p.data.heights, exaggeration: exag,
          bounds: [west, south, east, north], opacity: state.opacity, pickable: i === 0, parameters: cogDepth,
          updateTriggers: { image: state.version },
        });
      },
      updateTriggers: { getTileData: [state.date], renderSubLayers: [state.version, exag] },
      onViewportLoad: () => { setStatus(""); },
      onTileError: () => {},
    });
    if (which === "top") return [cogLayer(1)];
    const sphere = new SolidPolygonLayer({
      id: "sphere", data: [[[-180, 90], [0, 90], [180, 90], [180, -90], [0, -90], [-180, -90]]],
      getPolygon: (d) => d, stroked: false, filled: true, getFillColor: [9, 14, 26], visible: state.globe, parameters: FLAT,
    });
    return state.globe ? [sphere, bmLayer, cogLayer(0)] : [bmLayer, cogLayer(0)];
  }

  const makeView = () => (state.globe ? new GlobeView({ id: "globe", resolution: 5 }) : new MapView({ id: "map", repeat: true }));

  function readValue(info) {
    if (!info.picked || !info.tile || !info.tile.content || !info.bitmap) return null;
    const { west, south, east, north } = info.tile.bbox;
    let px, py;
    if (info.coordinate) {
      const [lon, lat] = info.coordinate;
      px = Math.floor(((lon - west) / (east - west)) * TILE);
      py = Math.floor(((mercY(lat) - mercY(north)) / (mercY(south) - mercY(north))) * TILE);
    } else {
      [px, py] = info.bitmap.pixel;
    }
    if (px < 0 || py < 0 || px >= TILE || py >= TILE) return null;
    const o = (py * TILE + px) * 2;
    const ok = (v) => (db ? Number.isFinite(v) : v > 0);
    const vals = info.tile.content.raws.map((raw) => (raw ? [raw[o], raw[o + 1]] : [NaN, NaN]));
    if (!vals.some(([vv]) => ok(vv))) return null;
    return { vals, coordinate: info.coordinate };
  }

  const fmt = (v) => (Number.isFinite(v) ? v.toFixed(1) : "–");
  const dk = new Deck({
    parent: $(".sar-map"),
    views: makeView(),
    viewState: currentView,
    controller: { inertia: true },
    layers: layers(),
    useDevicePixels: true,
    parameters: { clearColor: [0, 0, 0, 0] },
    onViewStateChange: ({ viewState: vs }) => {
      currentView = vs;
      setView(vs);
      setStatus("Loading tiles…", "busy");
    },
    getCursor: ({ isDragging }) => (isDragging ? "grabbing" : "crosshair"),
    onHover: (info, ev) => {
      const r = readValue(info);
      if (!r) { tooltip.hidden = true; return; }
      const dB = (v) => (db ? v : toDb(v));
      const coord = r.coordinate ? `${r.coordinate[1].toFixed(4)}°N, ${r.coordinate[0].toFixed(4)}°E` : "";
      let rows;
      if (compare) {
        const v = r.vals.map(([vv, vh]) => bandValue(state.band, vv, vh, db));
        rows = sources.map((src, i) => `<div>${src.label} <span>${fmt(v[i])} dB</span></div>`).join("")
          + `<div>${sources[1].label} − ${sources[0].label} <span>${fmt(v[1] - v[0])} dB</span></div>`;
      } else {
        const vvDb = dB(r.vals[0][0]), vhDb = dB(r.vals[0][1]);
        rows = [["VV", vvDb], ["VH", vhDb]].filter(([n]) => bandNames.includes(n)).map(([n, v]) => `<div>${n} <span>${fmt(v)} dB</span></div>`).join("")
          + (nSamples > 1 ? `<div>VH−VV <span>${fmt(vhDb - vvDb)} dB</span></div>` : "");
      }
      tooltip.innerHTML = `<b>${coord}</b>${rows}`;
      tooltip.hidden = false;
      const rect = $(".sar-map").getBoundingClientRect();
      const x = ev.srcEvent.clientX - rect.left, y = ev.srcEvent.clientY - rect.top;
      tooltip.style.transform = `translate(${Math.min(x + 16, rect.width - 190)}px, ${Math.min(y + 16, rect.height - 100)}px)`;
    },
  });

  // Comparison: a second, non-interactive deck on top shows the second source, clipped to the right of the slider.
  const mapTop = compare ? document.createElement("div") : null;
  let dk2 = null;
  if (compare) {
    mapTop.className = "sar-map sar-map-top";
    $(".sar-map").after(mapTop);
    dk2 = new Deck({
      parent: mapTop, views: makeView(), viewState: currentView, controller: false, layers: layers("top"),
      useDevicePixels: true, parameters: { clearColor: [0, 0, 0, 0] },
    });
  }
  function setView(vs) {
    dk.setProps({ viewState: vs });
    if (dk2) {
      const { transitionDuration, transitionInterpolator, ...plain } = vs; // dk drives the transition, dk2 follows its frames
      dk2.setProps({ viewState: plain });
    }
  }
  function setLayers() {
    dk.setProps({ layers: layers() });
    dk2?.setProps({ layers: layers("top") });
  }
  const refresh = () => { state.version++; setLayers(); drawHistogram(); };

  if (compare) {
    const bar = document.createElement("div");
    bar.className = "sar-swipe";
    bar.innerHTML = '<span class="sar-swipe-label" data-side="left"></span><span class="sar-swipe-label" data-side="right"></span><div class="sar-swipe-grip">⇆</div>';
    bar.querySelector("[data-side=left]").textContent = sources[0].label;
    bar.querySelector("[data-side=right]").textContent = sources[1].label;
    root.append(bar);
    const setSplit = (f) => {
      state.split = Math.min(0.98, Math.max(0.02, f));
      bar.style.left = `${state.split * 100}%`;
      mapTop.style.clipPath = `inset(0 0 0 ${state.split * 100}%)`;
    };
    let dragging = false;
    bar.addEventListener("pointerdown", (e) => { dragging = true; bar.setPointerCapture(e.pointerId); e.preventDefault(); });
    bar.addEventListener("pointermove", (e) => {
      if (!dragging) return;
      const r = root.getBoundingClientRect();
      setSplit((e.clientX - r.left) / r.width);
    });
    for (const t of ["pointerup", "pointercancel"]) bar.addEventListener(t, () => { dragging = false; });
    setSplit(state.split);
  }

  let settleTimer;
  function flyTo(vs, duration = 3000) {
    currentView = { ...currentView, ...vs, transitionDuration: duration, transitionInterpolator: new LinearInterpolator(["longitude", "latitude", "zoom", "pitch", "bearing"]) };
    setView(currentView);
    // leftover transition props would make every scroll-zoom step start a new slow transition (jitter)
    clearTimeout(settleTimer);
    settleTimer = setTimeout(() => {
      const { transitionDuration, transitionInterpolator, ...clean } = currentView;
      currentView = clean;
      setView(clean);
    }, duration + 100);
  }
  // zoom that fits the data extent in the map, so small areas are not lost in the overview
  const fitZoom = () => {
    const w = Math.max(300, $(".sar-map").clientWidth);
    const span = Math.max(extent[2] - extent[0], 1e-4);
    return Math.min(14, Math.max(3, Math.log2(((w * 0.5) / TILE) * (360 / span))));
  };
  const home = () => flyTo({ longitude: cfg.center[0], latitude: cfg.center[1], zoom: fitZoom(), ...(state.terrain && { pitch: 60 }) });

  // event wiring
  el.band.addEventListener("change", () => { state.band = el.band.value; syncControls(true); refresh(); });
  el.cmap.addEventListener("change", () => { state.cmap = el.cmap.value; state.lut = buildLut(state.cmap); syncControls(); refresh(); });
  const onRange = () => {
    let a = +el.min.value, b = +el.max.value;
    if (a >= b) { if (document.activeElement === el.min) a = b - 0.5; else b = a + 0.5; }
    state.min = a; state.max = b; syncControls(); refresh();
  };
  let raf;
  const throttled = () => { cancelAnimationFrame(raf); raf = requestAnimationFrame(onRange); };
  el.min.addEventListener("input", throttled); el.max.addEventListener("input", throttled);
  el.opacity.addEventListener("input", () => { state.opacity = +el.opacity.value; refresh(); });
  el.base.addEventListener("change", () => { state.basemap = el.base.value; refresh(); });
  function setGlobe(on) {
    state.globe = on;
    el.proj.textContent = on ? "Switch to flat map" : "Switch to globe";
    dk.setProps({ views: makeView() });
    dk2?.setProps({ views: makeView() });
    setLayers();
  }
  el.proj.addEventListener("click", () => {
    if (!state.globe && state.terrain) {
      state.terrain = el.terrain.checked = false;
      el.exagRow.hidden = true;
      flyTo({ pitch: 0, bearing: 0 }, 800);
    }
    setGlobe(!state.globe);
  });
  el.auto.addEventListener("click", () => {
    if (!state.auto) return;
    state.min = Math.round(state.auto[0] * 2) / 2; state.max = Math.round(state.auto[1] * 2) / 2;
    syncControls(); refresh();
  });
  el.fly.addEventListener("click", home);
  el.terrain.addEventListener("change", () => {
    state.terrain = el.terrain.checked;
    el.exagRow.hidden = !state.terrain;
    // GlobeView cannot tilt, so relief is shown on the flat map
    if (state.terrain && state.globe) setGlobe(false);
    setLayers();
    flyTo({ pitch: state.terrain ? 60 : 0, bearing: 0 }, 1500);
  });
  el.exag.addEventListener("input", () => {
    state.exaggeration = +el.exag.value;
    el.exagOut.textContent = `${state.exaggeration.toFixed(1)}×`;
    setLayers();
  });
  const advBtn = $("[data-ctl=advanced]");
  const advPanel = $(".sar-advanced");
  advBtn.addEventListener("click", () => {
    advPanel.hidden = !advPanel.hidden;
    advBtn.setAttribute("aria-expanded", String(!advPanel.hidden));
    if (!advPanel.hidden) drawHistogram(); // the canvas has no size while hidden
  });
  const fsBtn = $("[data-ctl=fullscreen]");
  if (!root.requestFullscreen) fsBtn.hidden = true;
  fsBtn.addEventListener("click", () => (document.fullscreenElement ? document.exitFullscreen() : root.requestFullscreen()));
  document.addEventListener("fullscreenchange", () => {
    const on = document.fullscreenElement === root;
    fsBtn.textContent = on ? "Exit fullscreen" : "Fullscreen";
    setTimeout(drawHistogram, 100);
  });
  window.addEventListener("resize", drawHistogram);

  const dateRow = $("[data-row=date]");
  const dateSel = $("[data-ctl=date]");
  if (dateRow && dateSel && dates.length > 1) {
    dateRow.hidden = false;
    dateSel.innerHTML = dates.map((d) => `<option>${d}</option>`).join("");
    dateSel.value = state.date;
    dateSel.addEventListener("change", () => {
      state.date = dateSel.value;
      setStatus("Loading tiles…", "busy");
      loadSample().catch((e) => console.warn("histogram unavailable", e));
      refresh();
    });
  }
  loadSample().catch((e) => console.warn("histogram unavailable", e));

  // 3D terrain is on by default: a tilted flat map, since the globe cannot tilt
  el.terrain.checked = state.terrain;
  el.exagRow.hidden = !state.terrain;
  el.proj.textContent = state.globe ? "Switch to flat map" : "Switch to globe";

  syncControls(false);
  setStatus("Loading tiles…", "busy");
  setTimeout(home, 600);
  return dk;
}

// Builds a viewer source from an openEO workspace export: a STAC collection with one item per date.
export async function loadCollectionSource(label, collectionUrl, asset = "VV") {
  const getJson = async (url) => {
    const r = await fetch(url);
    if (!r.ok) throw new Error(`${r.status} for ${url}`);
    return r.json();
  };
  const collection = await getJson(collectionUrl);
  const itemUrls = collection.links.filter((l) => l.rel === "item").map((l) => new URL(l.href, collectionUrl).href);
  const items = (await Promise.all(itemUrls.map((url) => getJson(url).then((item) => ({ item, url })).catch(() => null))))
    .filter((x) => x?.item.assets?.[asset]);
  if (!items.length) throw new Error(`No item with a ${asset} asset in ${collectionUrl}`);
  const dates = {};
  const stamp = ({ item }) => item.properties.datetime ?? item.properties.start_datetime;
  for (const x of items.sort((a, b) => stamp(a).localeCompare(stamp(b)))) {
    dates[stamp(x).slice(0, 10)] = new URL(x.item.assets[asset].href, x.url).href;
  }
  const [{ item }] = items;
  return { label, dates, bbox: item.bbox, proj: item.properties["proj:code"] };
}
