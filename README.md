# pipeline-visualization
how to render a pipeline flow with graph and time chart

# usage
to run the pipeline through

    python runner.py

testing containers e.g. graphviz rendering

create `cache/test/example.dot` with content such as
```dot
digraph G {
    A -> B;
    B -> C;
    C -> A;
}
```
note cache is mapped in `/data` inside the container.

Then generate the graph with

    run graphviz test/example.dot

