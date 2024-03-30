## openEO federation Design

### openEO Aggregator

The openEO Aggregator is the central component that receives all incoming openEO requests for the federation. It mainly
contains the logic that decides to which backends requests need to be forwarded. It does not perform any processing. Data
transfers to the user or between backends do not pass through the aggregator, to avoid bottlenecks.

The aggregator is an open source component maintained by the openEO community. It's code is hosted on GitHub:

https://github.com/Open-EO/openeo-aggregator/

### How does the aggregator route requests?

The current logic is simply based on the collections and processes involved in a request. In almost all cases, this combination
will allow to select a single backend. When there would be more than one potential candidate, the aggregator simply uses
selects backends according to a fixed preference, which makes it very deterministic. It is however possible for the user
to indicate a preferred backend in the openEO process graph.

This means that there's currently no mechanism to evenly distribute load. Such more advanced mechanisms are certainly 
possible, and can be implemented by the community or anyone who is interested in such a feature.

### What if a request uses collections from multiple backends?

By default, this request will not be accpeted, but there is an experimental setting that allows to enable this.
When enabled, the process graph will be split in multiple parts. Subgraphs without dependencies will be submitted, resulting
in STAC collections that are not yet finished (as the processing will take some time). These results are called 'partial',
and can already be used in a 'load_stac' process. Hence a process graph is created where load_collections with unavailable 
data are replaced with 'load_stac' with a partial result.

This final process graph is also submitted, and the receiving backend will wait for partial results to become available before
finishing the full computation.


