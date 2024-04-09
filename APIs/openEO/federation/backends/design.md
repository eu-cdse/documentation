## openEO federation Design

### openEO Aggregator

The openEO Aggregator is the central component that receives all incoming openEO requests for the federation. 
It mainly contains the logic that decides to which backends requests need to be forwarded. 
It does not perform any processing. 
To prevent bottlenecks, the aggregator does not handle any data transfers, either to the user or between backends.

Maintained by the openEO community, the aggregator is an open source component with its code hosted on GitHub:

[https://github.com/Open-EO/openeo-aggregator/](https://github.com/Open-EO/openeo-aggregator/)

### Processes

Each of the underlying back-ends of the federation can define its own set of available processes,
but there is in practice a very large common ground across these back-ends.
As such, the federation's listing of available processes is the _intersection_
of the process sets of each of the underlying back-ends.
This is the most straightforward combination with the least surprise.

::: tip Advanced/experimental usage
A savvy user that knows which underlying back-end will execute their job
can however still submit process graphs with processes that are available
on that back-end but fall outside the intersection,
as the federation will just forward the process graph as-is to that back-end.
:::

::: tip Note
For the technical discussion on process federation, see [Open-EO/openeo-aggregator#4](https://github.com/Open-EO/openeo-aggregator/issues/4)
:::

### File formats

The federation currently lists the _union_ of import/export file formats available
at each of the underlying back-ends.

::: tip Note
For the technical discussion on file format federation, see [Open-EO/openeo-aggregator#1](https://github.com/Open-EO/openeo-aggregator/issues/1)
:::


### How does the aggregator route requests?

The current routing logic is based on the collections and processes involved in a request. 
In almost all cases, this combination will allow the system to select a single backend. 
If more than one backend can manage the request, the aggregator will select backends according to a fixed preference, which makes the overall system deterministic. 
However, users have the option to indicate a preferred backend in their openEO process graph.

Currently, there's no established way to evenly distribute load within the federation. 
However, such more advanced mechanisms are certainly possible and can be implemented by the community or anyone who is interested in such a feature.

### What if a request uses collections from multiple backends?

By default, this request will not be accepted.
However, an experimental setting can be enabled to activate this feature.
When enabled, the process graph will be split into independent subgraphs.
These subgraphs will be submitted, resulting in STAC collections that are not considered finished (as the processing will take some time). 
These results, called 'partials', can be used in a `load_stac` process. 
This approach regenerates the initial process graph where `load_collection` processes with unavailable data are replaced with `load_stac` containing a partial result.

This final process graph also gets submitted.
The receiving backend will wait for partial results to become available before finishing the full computation.


