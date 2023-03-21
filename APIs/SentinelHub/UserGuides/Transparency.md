---
title: Transparency
---

## Transparency and Background Color

Parts of the image can be made transparent by including the fourth
output channel, also known as the *alpha* channel. The value 0 makes a
pixel fully transparent, while the maximum value makes it fully opaque
(not transparent).

*Note: maximum value depends on sampleType as described
[above](/APIs/SentinelHub/Evalscript/V3.md#sampletype): 1 in case of
AUTO or FLOAT32, 255 in case of UINT8, and 65535 in case of UINT16.*

An alternative approach of marking pixels is to use a background color,
or to combine transparency and background color. Note that the JPEG
format does not support alpha channel and thus only background color can
be used for JPEG outputs.

### Transparent no-data pixels

In many collections no-data pixels are marked by the value 0 in the
`dataMask`. Thus we can simply use this band as the fourth channel in
the `function evaluatePixel(samples, scenes)` in order to return the
no-data pixels as transparent. The `dataMask` band should be added to
the `input:bands` and four bands should be output in `output:bands` of
the `function setup()`. In the following example, Sentinel-2 L2A was
used, returning a true color image.

``` javascript
//VERSION=3
function setup () {
    return {
        input: ["B04", "B03", "B02", "dataMask"],
        output: {bands: 4}
    }
}
function evaluatePixel(samples, scenes) {
  return [samples.B04 * 3.5, samples.B03 * 3.5, samples.B02 * 3.5, samples.dataMask]
}
```

[Examine in EO
Browser](https://apps.sentinel-hub.com/eo-browser/?lat=45.7097&lng=13.4258&zoom=10&time=2020-03-19&preset=CUSTOM&datasource=Sentinel-2%20L2A&layers=B01,B02,B03&evalscript=Ly9WRVJTSU9OPTMKZnVuY3Rpb24gc2V0dXAgKCkgewoJcmV0dXJuewoJCWlucHV0OlsiQjA0IiwgIkIwMyIsICJCMDIiLCAiZGF0YU1hc2siXSwKCQlvdXRwdXQ6e2JhbmRzOiA0fQoJfQkJCn0KCgpmdW5jdGlvbiBldmFsdWF0ZVBpeGVsKHNhbXBsZXMsc2NlbmVzKSB7ICAKCiAgCiAgcmV0dXJuIFtzYW1wbGVzLkIwNCozLjUsIHNhbXBsZXMuQjAzKjMuNSwgc2FtcGxlcy5CMDIqMy41LCBzYW1wbGVzLmRhdGFNYXNrXQp9)

### Transparent data pixels

To use some other condition for turning pixels transparent, simply
return the condition in the fourth channel, while also outputting four
bands in the `function setup()`. In the example below, we are returning
the Sentinel-2 L1C [NDVI
index](https://custom-scripts.sentinel-hub.com/sentinel-2/ndvi/) larger
than 0.6 as transparent. We also leave the no-data pixels
non-transparent and thus do not need to use the the `dataMask` input
band.

``` javascript
//VERSION=3
function setup () {
  return {
    input: ["B02", "B03", "B04", "B08"],
    output: {bands: 4}
  }
}
function evaluatePixel(samples, scenes) {
  var NDVI = (samples.B08 - samples.B04) / (samples.B08 + samples.B04)
  return [samples.B04 * 2.5, samples.B03 * 2.5, samples.B02 * 2.5, NDVI < 0.6]
}
```

[Examine in EO Browser](https://tinyurl.com/y98vmqjd)

**Transparency with other sampleTypes**

For sampleType other than AUTO and FLOAT32, the fourth channel has to be
scaled as well. The above example, if using UINT8, would thus be:

``` javascript
//VERSION=3
function setup () {
  return {
    input: ["B02", "B03", "B04", "B08"],
    output: {
      bands: 4,
      sampleType: UINT8
    }
  }
}
function evaluatePixel(samples, scenes) {
  var NDVI = (samples.B08 - samples.B04) / (samples.B08 + samples.B04)
  return [samples.B04 * 2.5 * 255, samples.B03 * 2.5 * 255, samples.B02 * 2.5 * 255, (NDVI < 0.6) * 255]
}
```

### Both data pixels and no-data pixels transparent

In the following example, we have returned Sentinel-3 OLCI pixels with
[OTCI index](https://custom-scripts.sentinel-hub.com/sentinel-3/otci/)
values larger than 1 as transparent, rendering most marine pixels
transparent. Additionally, we have also multiplied the condition for the
transparent pixels with data in the fourth channel with `dataMask`,
making no-data values transparent as well.

``` javascript
//VERSION=3
function setup () {
    return {
        input: ["B04", "B06", "B08", "B10", "B11", "B12", "dataMask"],
        output: {bands: 4}
    }
}
function evaluatePixel(samples, scenes) {
  var OTCI = (samples.B12 - samples.B11) / (samples.B11 - samples.B10)
  return [samples.B08 * 2.5, samples.B06 * 2.5, samples.B04 * 2.5, OTCI > 1 * samples.dataMask]
}
```

[Examine in EO Browser](https://tinyurl.com/y7dskybg)

### Background color for no-data pixels

To show no-data pixels as a chosen background color instead of
transparent, `evaluatePixel` simply returns the background color if the
condition is met. In this example we are using Sentinel-1, creating an
RGB output of `VV, VH * 5, VH * 5`, but return the no-data pixels as
blue.

``` javascript
//VERSION=3
function setup () {
    return {
        input: ["VV", "VH", "dataMask"],
        output: {bands: 3}
    }
}
function evaluatePixel(samples, scenes) {
  if (samples.dataMask == 0) {
    return [0, 0, 0.3]
  }
  else {
    return [samples.VV, samples.VH * 5, samples.VH * 5]
  }
}
```

[Examine in EO Browser](https://tinyurl.com/y92f4zoo)

### Background color for no-data pixels with transparency for data pixels

In this example we want to return no-data pixels as grey and the
Sentinel-1 VH polarization pixels lower than 0.01 as transparent. To do
this, we set up a condition to return grey color if `dataMask` is equal
to 0, while for pixels with data we return the transparency condition in
the fourth channel. Since we are producing a four-band output, the grey
color returned for no-data pixels also has to have four channels and the
value of the fourth channel must be 1.

``` javascript
//VERSION=3
function setup () {
    return {
        input: ["VV", "VH", "dataMask"],
        output: {bands: 4}
    }
}
function evaluatePixel(samples, scenes) {
  if (samples.dataMask == 0) {
    return [0.5, 0.5, 0.5, 1]
  }
  else {
    return [samples.VV, samples.VH * 5, samples.VH * 5, samples.VH > 0.01]
  }
}
```

[Examine in EO Browser](https://tinyurl.com/yaa839uq)

### Switching between transparency and background color with multiple conditions

The easy way to control which parts are transparent is to use either 1
(not transparent) or 0 (transparent) in the fourth channel. In the
example using Landsat 8 below, we have separated the pixel evaluation
into 3 parts: the first \'if\' statement includes all the [NDMI
index](https://www.usgs.gov/land-resources/nli/landsat/normalized-difference-moisture-index)
\> 0.5 pixels, the second \'if\' statement includes the no-data pixels
(those with the value 0 in the `dataMask` band). The final `return`
produces true color bands for all the other pixels. Currently, all of
them have 1 in the fourth channel, making them visible.

``` javascript
//VERSION=3
function setup () {
    return {
        input: ["B02", "B03", "B04", "B05", "B06", "dataMask"],
        output: {bands: 4}
    }
}
function evaluatePixel(samples, scenes) {
  if ((index(samples.B05, samples.B06)) > 0.5) {
    return [0, 0.5, 1, 1]
  }
  if (samples.dataMask == 0) {
    return [0.5, 0.5, 0.5, 1]
  }
  return [samples.B04 * 2.5, samples.B03 * 2.5, samples.B02 * 0.5, 1]
}
```

[Examine in EO Browser](https://tinyurl.com/yb3xmelp)

We can turn any one of them instantly transparent by changing 1 in the
fourth channel to 0. In the example below, we left the NDMI \> 0.5
pixels as blue and no-data pixels as grey, while returning all other
pixels transparent, by simply changing the fourth channel to 0.

``` javascript
//VERSION=3
function setup () {
    return {
        input: ["B02", "B03", "B04", "B05", "B06", "dataMask"],
        output: {bands: 4}
    }
}
function evaluatePixel(samples, scenes) {
  if ((index(samples.B05, samples.B06)) > 0.5) {
    return [0, 0.5, 1, 1]
  }
  if (samples.dataMask == 0) {
    return [0.5, 0.5, 0.5, 1]
  }
  return [samples.B04 * 2.5, samples.B03 * 2.5, samples.B02 * 0.5, 0]
}
```

[Examine in EO Browser](https://tinyurl.com/y9lywgwh)

### Transparency with commercial Planet data

Transparency can be used with all the available EO collections,
including the commercial Planet and Pleiades data. Planet values needs
to be scaled to transform them to reflectance values (we don\'t have to
convert no-data pixels). To learn more, visit our documentation on
[Planet](/data/planet/planet-scope/).

``` javascript
//VERSION=3
function setup() {
  return {
    input: ["B1", "B2", "B3", "dataMask"],
    output: { bands: 4}
  }
}
function evaluatePixel(sample) {
  return [sample.B3 / 3000,
          sample.B2 / 3000,
          sample.B1 / 3000,
          sample.dataMask]
}
```

### Combining transparency and sampleType for commercial satellites

This Pleiades example looks into how to handle commercial data with
transparency and custom sampleType formats. First, Pleiades data
requires us to divide the values by a scaling factor to bring them to
reflectance values. To learn more, visit our [Pleiades
documentation](/data/airbus/pleiades/). Note that no-data pixels don\'t
need this scaling. To return an image in UINT16 format, we need to
additionally multiply the values by 65535 to bring them to 16-bit range
and this also applies to no-data values. Learn more on sampleType
formats and conversions
[here](/APIs/SentinelHub/Evalscript/V3.md#sampletype).

``` javascript
//VERSION=3
function setup() {
  return {
    input: ["B0", "B1", "B2", "dataMask"],
    output: { bands: 4,
      sampleType: "UINT16" }
  }
}
function evaluatePixel(sample) {
  return [sample.B2 / 3000 * 65535,
          sample.B1 / 3000 * 65535,
          sample.B0 / 3000 * 65535,
          sample.dataMask * 65535]
}
```
