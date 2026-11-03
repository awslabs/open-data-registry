# NASA PDS Geosciences Node Planetary Science Archive on AWS

Documentation for the [NASA Planetary Data System (PDS) Geosciences Node](https://pds-geosciences.wustl.edu/) archive on the [Registry of Open Data on AWS](https://registry.opendata.aws/). Facts below are taken from official PDS Geosciences Node and PDS program pages (linked inline).

> **Publishing note:** This content is staged in [fossettlab/open-data-registry](https://github.com/fossettlab/open-data-registry/tree/main/pds-geosciences-opendata) until the dedicated repository [fossettlab/pds-geosciences-opendata](https://github.com/fossettlab/pds-geosciences-opendata) is created; then the registry `Documentation` URL will be updated to that repository's `README.md`.

## Overview

The Geosciences Node is one of the discipline-specific nodes of NASA's Planetary Data System. It archives and distributes data sets relevant to the **geosciences discipline**, defined as the study of the **surfaces and interiors of terrestrial planetary bodies**. The node consists of a lead node at Washington University in St. Louis and three data nodes (TES at Arizona State University, GRS at the University of Arizona, and LOLA at MIT). The node also restores data sets from past missions that are in danger of being lost.

Sources: [About the Geosciences Node](https://pds-geosciences.wustl.edu/about/default.htm)

## Coverage

Data are organized by target, mission, and instrument. The node maintains online holdings for Mars, Venus, Mercury, the Moon, Earth analog and laboratory data (including the Geosciences Spectral Library), asteroids, and other planetary targets. Browse the full inventory via [Data and Services](https://pds-geosciences.wustl.edu/dataserv/default.htm) and the [holdings list](https://pds-geosciences.wustl.edu/dataserv/holdings.html).

## Data formats (PDS3 and PDS4)

- Archives follow **PDS3** and **PDS4** standards. Both include science data, documentation, and ancillary products, with metadata in a **PDS label** (PDS3: keyword=value labels; PDS4: XML labels).
- Missions confirmed for flight after **November 1, 2011** must archive in **PDS4**. Older PDS3 archives are being migrated to PDS4 under PDS migration policy.
- On the Geosciences Node website, PDS4 archives are marked **"(PDS4)"** and use directory names beginning with `urn-nasa-pds`.
- PDS4 uses descriptive processing levels (for example Raw, Calibrated, Derived) rather than the numeric PDS3 level schemes.

Sources: [About PDS4 (Geosciences Node)](https://pds-geosciences.wustl.edu/dataserv/pds4.html), [PDS data standards](https://pds.nasa.gov/datastandards/about/)

## Directory layout (current node archive)

On the Geosciences Node servers, each data set is stored under a path of the form **target / data set / volume**. A checksum file is provided in the root of each archive volume. See [Anonymous FTP Access](https://pds-geosciences.wustl.edu/dataserv/anonftp.html) for path examples and checksum usage.

## Finding data

- **[Orbital Data Explorer (ODE)](https://pds-geosciences.wustl.edu/dataserv/default.htm)** — search, display, and download orbital data for [Mars](https://ode.rsl.wustl.edu/mars/), [Moon](https://ode.rsl.wustl.edu/moon/), [Mercury](https://ode.rsl.wustl.edu/mercury/), and [Venus](https://ode.rsl.wustl.edu/venus/).
- **Analyst's Notebooks** — integrated landed-mission data with sequence, engineering, and documentation (see [Data and Services](https://pds-geosciences.wustl.edu/dataserv/default.htm)).
- **[Help for Data Users](https://pds-geosciences.wustl.edu/dataserv/default.htm)** explains standard PDS archive structure.

## License and citation

- **License:** Data sets archived in the PDS are in the **public domain** and may be downloaded freely. See the [Geosciences Node FAQ](https://pds-geosciences.wustl.edu/faq.html).
- **Citation:** Cite the most granular product; PDS4 bundles have DOIs. See [Citing PDS4 Data](https://pds.nasa.gov/datastandards/citing/) and the [Geosciences Node DOI list](https://pds-geosciences.wustl.edu/dataserv/doi.htm) (updated as new DOIs are acquired).

## Contact

| Topic | Email |
| --- | --- |
| Data and website | geosci@wunder.wustl.edu |
| Orbital Data Explorer | ode@wunder.wustl.edu |
| Analyst's Notebooks | an@wunder.wustl.edu |
| Spectral Library | speclib@wunder.wustl.edu |

Source: [Contact](https://pds-geosciences.wustl.edu/contact/default.htm)

## AWS Open Data registry entry

Registry metadata (draft) is maintained in [fossettlab/open-data-registry](https://github.com/fossettlab/open-data-registry) as `datasets/pds-geosciences.yaml`.
