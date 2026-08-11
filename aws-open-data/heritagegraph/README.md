# HeritageGraph — A Knowledge Graph of Nepal's Cultural Heritage

HeritageGraph is an RDF knowledge graph of Nepal's **tangible and intangible
cultural heritage**, built on the CIDOC-CRM–aligned
[HeritageGraph ontology](https://cairnepal.github.io/heritagegraphontology/) and populated from
trusted open sources. Every entity carries machine-readable **provenance** and a
link back to its source. No synthetic data is used.

## What's in the bucket

```
heritagegraph/
├── README.md            ← this file
├── LICENSE.txt          ← licensing (our CC BY 4.0; OSM layer is ODbL)
├── ontology/            ← schema (TBox)
│   ├── HeritageGraph.ttl         OWL ontology  (namespace https://cair-nepal.org/heritagegraph/)
│   ├── HeritageGraph.shacl.ttl   SHACL shapes (validation)
│   └── HeritageGraph.yaml        LinkML source
├── kg/                  ← data (ABox), two files split by license
│   ├── heritagegraph-core.ttl  CC BY 4.0  Wikidata + UNESCO + intangible + crosswalks (no OSM)
│   └── heritagegraph-osm.ttl   ODbL       ~7,589 OpenStreetMap features + their crosswalk links
└── examples/
    ├── competency-questions.md             32 SPARQL competency questions
    ├── competency-questions-data-results.txt  sample results over this data
    └── build_stats.json                    entity counts per source / class
```

## Scale

~7,850 tangible heritage entities (temples, stupas, monasteries, traditional
water spouts/*dhunge dhara*, monuments) + a curated intangible-heritage layer.

| Class | Count |
|-------|------:|
| ArchitecturalStructure | 6,771 |
| BuddhistMonument | 798 |
| WaterStructure | 141 |
| DhungeDhara | 115 |
| Chaitya / Stupa | 13 / 13 |
| Murti | 1 |
| + intangible: festivals, chariot festivals, masked dances, Guthi, caste groups, deities, rituals, Living-Goddess lifecycle |

## Format & tooling

Data is **RDF 1.1 Turtle** (`.ttl`). Query it with [`rdflib`](https://rdflib.readthedocs.io/)
(Python) or load into a triplestore — [**Amazon Neptune**](https://aws.amazon.com/neptune/),
[Apache Jena Fuseki](https://jena.apache.org/), or [GraphDB](https://graphdb.ontotext.com/) —
and query with **SPARQL**. Validate extensions against `ontology/HeritageGraph.shacl.ttl`.

HeritageGraph is released under **CC BY 4.0**. The OpenStreetMap layer is split
into its own file (`heritagegraph-osm.ttl`) because it carries OpenStreetMap's
share-alike **ODbL** terms, so the CC BY core (`heritagegraph-core.ttl`) can be
used on its own. See `LICENSE.txt`.

## Namespaces

- Schema / classes & properties: `https://cair-nepal.org/heritagegraph/`
- Instance identifiers: `https://data.cair-nepal.org/heritagegraph/`

## Quick start

```python
from rdflib import Graph
g = Graph()
g.parse("kg/heritagegraph-core.ttl", format="turtle")   # CC BY core
g.parse("kg/heritagegraph-osm.ttl", format="turtle")    # + OSM layer (ODbL)
print(len(g), "triples")
```

See the
[Get to Know the HeritageGraph KG tutorial](https://github.com/CAIRNepal/heritagegraphontology/blob/main/aws-open-data/get-to-know-the-heritagegraph-kg.ipynb)
on GitHub, or the
[Registry of Open Data on AWS](https://registry.opendata.aws/heritagegraph)
entry once published.

