# Using HeritageGraph — AWS Open Data Tutorial

HeritageGraph is an RDF knowledge graph of Nepal's **tangible and intangible
cultural heritage**: temples, stupas, monasteries, stone water spouts (*dhunge
dhara*), UNESCO World Heritage sites, festivals, Guthi institutions, ritual
roles, deities, and more. Every fact carries machine-readable **provenance**
(source, confidence, epistemic stance) and links back to Wikidata or
OpenStreetMap where available.

Once published, the dataset will appear on the
[Registry of Open Data on AWS](https://registry.opendata.aws/heritagegraph).
Full ontology documentation lives at
[https://cairnepal.github.io/heritagegraphontology/](https://cairnepal.github.io/heritagegraphontology/).
Source code and releases are in the
[CAIRNepal/heritagegraphontology](https://github.com/CAIRNepal/heritagegraphontology)
repository on GitHub.

---

## Start here: guided notebook

The fastest way to explore the data is the
[**Get to Know the HeritageGraph KG**](get-to-know-the-heritagegraph-kg.ipynb)
notebook (AWS Open Data template). It walks through bucket layout, loading Turtle
files, entity statistics, a map of geolocated heritage, and provenance-aware
SPARQL queries.

**Run locally** (uses the bundled `heritagegraph/` data — no S3 bucket required):

```bash
git clone https://github.com/CAIRNepal/heritagegraphontology.git
cd heritagegraphontology/aws-open-data
pip install rdflib matplotlib boto3 jupyter
jupyter lab get-to-know-the-heritagegraph-kg.ipynb
```

**Run against the public S3 bucket** (once provisioned): open the notebook,
set `BUCKET` to the registry bucket name in the second code cell, and run all
cells. Public buckets use unsigned S3 requests (no AWS account needed to read).

---

## Access the data

### From Amazon S3

After publication, files are under the `heritagegraph/` prefix, for example:

```
s3://<bucket>/heritagegraph/
├── LICENSE.txt
├── README.md
├── ontology/          HeritageGraph OWL, SHACL shapes, LinkML source
├── kg/                RDF Turtle — CC BY core + separate ODbL OSM layer
└── examples/          SPARQL competency questions and sample results
```

Download a single file with the AWS CLI:

```bash
aws s3 cp s3://<bucket>/heritagegraph/kg/heritagegraph-core.ttl ./heritagegraph-core.ttl --no-sign-request
```

Sync the full dataset:

```bash
aws s3 sync s3://<bucket>/heritagegraph/ ./heritagegraph/ --no-sign-request
```

### From this repository

Clone the repo and use the copy under `aws-open-data/heritagegraph/` — it matches
the S3 layout exactly.

---

## What's in `heritagegraph/kg/`

The KG ships as **two files**. The split is purely about licensing: the OSM layer
carries OpenStreetMap's share-alike (ODbL) terms, so it is kept on its own and the
rest is released as one graph under our CC BY 4.0.

| File | License | Contents |
|------|---------|----------|
| `heritagegraph-core.ttl` | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) | The HeritageGraph core: Wikidata-sourced facts (originally CC0), UNESCO World Heritage components, the curated intangible layer (festivals, Guthi, Kumari, deities, castes, rituals), and the crosswalk links between them. No OSM data. |
| `heritagegraph-osm.ttl` | [ODbL](https://opendatacommons.org/licenses/odbl/1-0/) | ~7,589 geolocated physical features from OpenStreetMap (© OpenStreetMap contributors) plus the crosswalk links that reference them. |

**Tip:** To avoid ODbL share-alike obligations, use only `heritagegraph-core.ttl`.
Load `heritagegraph-osm.ttl` as well for full geographic coverage, but note any
database that incorporates it must then be shared under ODbL. See
`heritagegraph/LICENSE.txt` for full terms.

**Scale:** ~7,850 tangible entities + a curated intangible layer (~138k triples
in total). See `heritagegraph/examples/build_stats.json` for per-class counts.

---

## Quick start: Python + rdflib

```python
from rdflib import Graph

g = Graph()
# CC BY core only:
g.parse("heritagegraph/kg/heritagegraph-core.ttl", format="turtle")
# Add the OSM layer for full geographic coverage (adds ODbL share-alike terms):
g.parse("heritagegraph/kg/heritagegraph-osm.ttl", format="turtle")

print(f"{len(g):,} triples loaded")
```

### Example SPARQL — geolocated temples and stupas

```python
q = """
PREFIX hg:   <https://cair-nepal.org/heritagegraph/>
PREFIX crm:  <http://www.cidoc-crm.org/cidoc-crm/>
PREFIX geo:  <http://www.opengis.net/ont/geosparql#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT ?label ?wkt WHERE {
  ?s a ?cls ; rdfs:label ?label ; crm:P55_has_current_location ?p .
  ?p geo:asWKT ?wkt .
  FILTER(?cls IN (hg:ArchitecturalStructure, hg:Stupa, hg:BuddhistMonument))
} LIMIT 10
"""
for row in g.query(q):
    print(row.label, "→", row.wkt)
```

More queries: `heritagegraph/examples/competency-questions.md` (32 competency
questions with sample results in `competency-questions-data-results.txt`).

---

## Quick start: Amazon Neptune

For production SPARQL at scale, load the Turtle files into
[Amazon Neptune](https://aws.amazon.com/neptune/):

1. Upload `heritagegraph/kg/*.ttl` to an S3 bucket Neptune can read.
2. Use bulk load (`neptune-loader`) or the Neptune Workbench to import.
3. Query with SPARQL 1.1 — the graph uses standard prefixes (`crm:`, `geo:`,
   `prov:`, `hg:`).

The ontology and SHACL shapes in `heritagegraph/ontology/` define the schema and
validation rules for any data you add.

Alternatives: [Apache Jena Fuseki](https://jena.apache.org/),
[GraphDB](https://graphdb.ontotext.com/), or any RDF 1.1 triplestore.

---

## Namespaces

| Purpose | IRI |
|---------|-----|
| Classes & properties | `https://cair-nepal.org/heritagegraph/` |
| Instance identifiers | `https://data.cair-nepal.org/heritagegraph/` |
| Source vocabulary | `https://data.cair-nepal.org/heritagegraph/source/` |

---

## Licensing

HeritageGraph (ontology, SHACL shapes, and the `heritagegraph-core.ttl` graph)
is released by CAIR-Nepal under **CC BY 4.0**.

> Attribution: *"HeritageGraph © CAIR-Nepal, CC BY 4.0
> (https://cair-nepal.org/heritagegraph/)"*

Some underlying facts are **sourced from** third parties — Wikidata (originally
CC0), the UNESCO World Heritage Centre, and OpenStreetMap. The OpenStreetMap layer
is the only one carrying onward obligations: it is governed by the share-alike
**ODbL** license and is therefore published as a separate file,
`heritagegraph-osm.ttl` (© OpenStreetMap contributors). Any combined database that
includes the OSM layer must comply with ODbL; `heritagegraph-core.ttl` can be used
under CC BY 4.0 on its own. Full terms:
[`heritagegraph/LICENSE.txt`](heritagegraph/LICENSE.txt).

---

## Learn more

| Resource | Link |
|----------|------|
| Registry entry | [registry.opendata.aws/heritagegraph](https://registry.opendata.aws/heritagegraph) |
| Ontology docs | [cairnepal.github.io/heritagegraphontology](https://cairnepal.github.io/heritagegraphontology/) |
| GitHub repository | [github.com/CAIRNepal/heritagegraphontology](https://github.com/CAIRNepal/heritagegraphontology) |
| Guided notebook | [get-to-know-the-heritagegraph-kg.ipynb](get-to-know-the-heritagegraph-kg.ipynb) |
| Bucket README | [heritagegraph/README.md](heritagegraph/README.md) |
| Contact | info@cair-nepal.org · [CAIR-Nepal](https://cair-nepal.org) |
