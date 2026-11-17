# GloBI Regional Building Inventory Data

Canonical technical documentation lives in [`globi-data/docs/PUBLIC-DATA.md`](https://github.com/MITSustainableDesignLab/globi-data/blob/main/docs/PUBLIC-DATA.md).

## Overview

The **Global Building Inventory (GloBI)** dataset maintained by the [MIT Sustainable Design Lab](https://sustainability.mit.edu/) provides versioned Urban Building Energy Modeling (UBEM) input bundles and building-level simulation results across **eight regions in seven countries** (`BR`, `GB`, `IN`, `KE`, `NO`, `PT`, `SG`, `US`). Each regional model is developed a regional partner university and stakeholder.

It supports climate resilience, peak grid planning, and building decarbonization research by pairing historical climate (**TMY**) and mid-century morphed climate (**2050 SSP2-4.5 FTMY**) simulations with reproducible EnergyPlus component libraries and archetype definitions.

## Bucket layout

One public bucket (`RequesterPays: false`, anonymous read) with two prefixes:

| Prefix | Format | Launch volume | Description |
|--------|--------|---------------|-------------|
| `globi-inputs/` | SQLite (`.db`), YAML, EPW/DDY weather, `.parquet` | 8 regional `v001` bundles (130 files, ~57 MB) | Self-contained regional simulation inputs (`<ISO>/<Partner>/vNNN/`). Excludes raw `buildings.geojson` footprints (sha256 recorded in manifests). |
| `globi-public/` | Apache Parquet (`.parquet`) | 28 experiments × 3 tables (84 Parquet files) | Building-level results (`<ISO>/<City>/<weather>/<Scenario>/<output_version>/`): `energy_and_peak.parquet`, `overheating.parquet`, and `emissions_by_building.parquet`. |

## Regional coverage at launch

- **Simulated cities (28 TMY/FTMY scenario runs):** Ahmedabad (`IN`: `BAU` vs `CC`), Lisbon (`PT`: `Baseline` vs `Retrofit`), Manchester (`GB`: `No_DSR` vs `DSR`), Nairobi (`KE`: `noAC` vs `withAC`), São Paulo Bela Vista (`BR`: `noAC` vs `withAC`), Singapore (`SG`: `Baseline` vs `Retrofit`), Trondheim (`NO`: `LowEfficiency` vs `HighEfficiency`).
- **Surrogate feature & input bundle:** Massachusetts (`US/MA/v001`).

## Quick access examples

```bash
# Sync a regional input bundle (no AWS account required)
aws s3 sync s3://<bucket>/globi-inputs/PT/Lisbon/v001/ ./Lisbon-v001 --no-sign-request

# Copy building-level Parquet results for one experiment
aws s3 cp \
  s3://<bucket>/globi-public/IN/Ahmedabad/ftmy/CC/v001/overheating.parquet \
  . --no-sign-request
```

 Parquet files can also be queried in place with **DuckDB** (`read_parquet('s3://...')`), **PyArrow** (`fs.S3FileSystem(anonymous=True)`), or **Amazon Athena**, or downloaded by logical experiment name with the [`globi-data`](https://github.com/MITSustainableDesignLab/globi-data) CLI.

## Provenance and licensing

- Every version directory (`v001`, `v002`, …) is immutable once published; `output-version.yml` pins the exact `bundle_sha256` of the input version that produced it.
- Released under the [MIT License](https://github.com/MITSustainableDesignLab/globi-data/blob/main/LICENSE) (see per-bundle `README.md` for partner attribution).
- Contact: `daryag@mit.edu` | GitHub: [MITSustainableDesignLab/globi-data](https://github.com/MITSustainableDesignLab/globi-data)