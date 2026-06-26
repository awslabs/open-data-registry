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
├── LICENSE.txt          ← per-source licensing (CC0 / ODbL / CC BY)
├── ontology/            ← schema (TBox)
│   ├── HeritageGraph.ttl         OWL ontology  (namespace https://cair-nepal.org/heritagegraph/)
│   ├── HeritageGraph.shacl.ttl   SHACL shapes (validation)
│   └── HeritageGraph.yaml        LinkML source
├── kg/                  ← data (ABox), one file per source / named graph
│   ├── wikidata.ttl     CC0     ~254 richly-described entities
│   ├── osm.ttl          ODbL    ~7,589 geolocated physical features
│   ├── unesco.ttl       —       8 World Heritage cultural components
│   ├── intangible.ttl   CC BY   festivals, Guthi, Kumari, deities, castes, rituals
│   ├── crosswalk.ttl    mixed   owl:sameAs / provenance back-links (not SHACL-validated)
│   └── intangible_crosswalk.ttl  mixed  intangible-layer owl:sameAs / typing links
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

The sources are kept in **separate named graphs** so a pure-CC0 core
(Wikidata + UNESCO) can be used independently of the share-alike OSM (ODbL)
layer. See `LICENSE.txt`.

## Namespaces

- Schema / classes & properties: `https://cair-nepal.org/heritagegraph/`
- Instance identifiers: `https://data.cair-nepal.org/heritagegraph/`

## Quick start

```python
from rdflib import Graph
g = Graph()
for f in ["wikidata", "osm", "unesco", "intangible", "crosswalk", "intangible_crosswalk"]:
    g.parse(f"kg/{f}.ttl", format="turtle")
print(len(g), "triples")
```

See the
[Get to Know the HeritageGraph KG tutorial](https://github.com/CAIRNepal/heritagegraphontology/blob/main/aws-open-data/get-to-know-the-heritagegraph-kg.ipynb)
on GitHub, or the
[Registry of Open Data on AWS](https://registry.opendata.aws/heritagegraph)
entry once published.

