---
title: Evalscript (custom script)
---

An evalscript (or \"custom script\") is a piece of Javascript code which
defines how the satellite data shall be processed by Sentinel Hub and
what values the service shall return. It is a required part of any
[process](/APIs/SentinelHub/Process.md), [batch processing]() or [OGC
request]().

Evalscripts can use any JavaScript function or language structures,
along with certain [utility
functions](/APIs/SentinelHub/Evalscript/Functions.md) we provide for
your convenience. For running evalscripts we use the [Chrome
V8](https://v8.dev/) JavaScript engine.

In the [Evalscript V3](/APIs/SentinelHub/Evalscript/V3.md) section you
will find a technical documentation with detailed explanations of
parameters and functions you can use in your evalscripts.

### Examples

Examples of various evalscritps can be found on our [Custom Scripts
Repository](https://custom-scripts.sentinel-hub.com/).

### Tutorials and Other Related Materials

-   A PDF tutorial on writing simple evalscripts for beginners: [Custom
    scripts
    tutorial](https://www.sentinel-hub.com/explore/education/custom-scripts-tutorial/)
-   A webinar on writing evalscripts for beginners: [Custom
    Scripts](https://www.youtube.com/watch?v=cgAH2beNYoU), September 28,
    2020
-   A webinar on multi-temporal scripts and data fusion: [Multi-temporal
    Scripts and Data
    Fusion](https://www.youtube.com/watch?v=kbw3OyYkbA4), March 3, 2021
-   A blog on good scripting practices: [Custom Scripts: Faster,
    Cheaper,
    Better!](https://medium.com/sentinel-hub/custom-scripts-faster-cheaper-better-83f73894658a),
    November 18, 2019
-   A blog post on color maps: [PUCK - Perceptually Uniform Color Maps
    in Satellite
    Imagery](https://medium.com/sentinel-hub/perceptually-uniform-color-maps-in-satellite-imagery-3e3e24e30af5),
    January 28, 2021
-   A blog post on sampleType: [SampleType: what's all the fuss
    about?](https://medium.com/sentinel-hub/sampletype-whats-all-the-fuss-about-d7348b4de647),
    February 15, 2022
-   More blog posts and useful links can be found on our [Sentinel Hub
    website](https://www.sentinel-hub.com/develop/custom-scripts/).
