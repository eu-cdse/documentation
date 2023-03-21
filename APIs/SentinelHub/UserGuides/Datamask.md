---
title: Data Mask
---

## dataMask - handling of pixels with "no data"

With evalscript v3 we are now providing full control to you over what is
to be returned for image parts (pixels) where there is "no data". In the
`setup` function, you can request **dataMask** as an element of the
`input` array and then use it in the `evaluatePixel` function in the
same manner as any other input band.

### General notes

**dataMask** has value 0 for "no data" pixels and 1 elsewhere.

By "no data" pixels we mean:

-   All pixels which lay outside of the requested polygon (if
    specified).
-   All pixels for which no source data was found.
-   All pixels for which source data was found and is explicitly "no
    data".

Things to note:

1.  All "no data" pixels as defined above have a dataMask value of 0.
    All band values for these pixels are also 0, except for Landsat data
    collections, where band values for no data pixels are NaN.
2.  \"No data\" pixels are treated like any other in the evalscript.
    Their value, namely zero (or NaN in case of Landsat data
    collections), is applied to your evalscript just like any other
    other pixel. E.g. `return [sample.B04*sample.B03]` will return 0 for
    "no data" pixels, while `return [sample.B04/sample.B03]` would
    return \"Infinity\" (if requested `sampleType` is FLOAT32) due to
    division by zero (or \"NaN\" for Landsat data collection where the
    division would be by \"NaN\"). To treat \"no data\" pixels
    differently, explicitly handle them in your evalscript. See the
    examples below.

### Example 1: Assign an arbitrary value (99) to "no data" pixels

#### Example using evalscript V3

``` javascript
//VERSION=3

function setup() {
  return {
    input: ["B02", "B03", "B04", "dataMask"],
    output: { bands: 3 }
  }
}

function evaluatePixel(sample) {
  if (sample.dataMask == 1)  {
    return [2.5 * sample.B04, 2.5 * sample.B03, 2.5 * sample.B02]
  } else {
    return [99, 99, 99]
  }
}
```

#### Example using simple script

``` javascript
//VERSION=3
if (dataMask == 1)  {
  return [2.5 * B04, 2.5 * B03, 2.5 * B02]
} else {
  return [99/255, 99/255, 99/255] //normalized with 255 for visualization in EO Browser
}
```

### Example 2: Use values in dataMask as the transparency band

*Note: If you\'d like to use this example, you must set the
`output.responses.format.type` parameter of your `process` API request
to `image/png` or `image/tiff`. The png format will automatically
interpret the fourth band as transparency.*

#### Example using evalscript V3

``` javascript
//VERSION=3

function setup() {
  return {
    input: ["B02", "B03", "B04", "dataMask"],
    output: { bands: 4 }
  }
}

function evaluatePixel(sample) {
    return [2.5 * sample.B04, 2.5 * sample.B03, 2.5 * sample.B02, sample.dataMask]
}
```

#### Example using simple script

``` javascript
//VERSION=3
return [2.5 * B04, 2.5 * B03, 2.5 * B02, dataMask]
```
