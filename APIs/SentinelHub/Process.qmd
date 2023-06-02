---
title: Processing API
---

The Processing API (or shortly \"Process API\") is the most commonly
used API in Sentinel Hub as it provides images based on satellite data.
Users can request raw satellite data, simple band combinations such as
false colour composites, calculations of simple remote sensing indices
like NDVI, or more advanced processing such as calculation of Leaf area
index (LAI).

Even though satellite imagery data are often distributed in \"tiles\",
we do not want users to be limited to these. Tiles are an artificially
introduced entity to make data distribution easier to handle. However,
users should not have to care about whether their AOI is on one tile or
another, or perhaps on the border of two tiles. This is why Sentinel Hub
API hides this complexity and simply makes the data available over
chosen area of interest and temporal period of interest. Tiles are
therefore automatically stitched together based on defined parameters
(AOI, time period, cloud coverage, priority, etc., depending on the data
type).
