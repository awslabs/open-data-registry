# open-data-registry

A repository of publicly available datasets available on AWS. 

## What is this for?

When data is staged for analysis on AWS, it is available for fast access using AWS APIs and SDKs and relieves data users from needing to download and store their own copies of the data. This repository exists to help people promote and discover datasets that are available on AWS.

## How are datasets added to the registry?

Each dataset in this repository is described with metadata saved in a YAML file in the [/datasets](/datasets) directory. We use these YAML files to provide three services:

- A Registry of Open Data on AWS website.
- A hosted YAML file listing all of the dataset entries.
- Hosted YAML files for each dataset.

The YAML files use this structure:

```yaml
Name:
Description:
Contact:
UpdateFrequency:
Tags:
  - 
License: 
Resources:
  - Description: 
    ARN: 
    Region: 
    Type:
```

The metadata required for each dataset entry is as follows:

| Field | Type | Description |
| --- | --- | --- |
| **Name** | String | The public facing name of the dataset |
|**Description**|String|A high-level description of the dataset|
|**Documentation**|URL|A link to documentation of the dataset|
|**Contact**|String|May be an email address, a link to contact form, a link to GitHub issues page, or any other instructions to contact the producer of the dataset|
|**UpdateFrequency**|String|An explanation of how frequently the dataset is updated|
|**Tags**|List of strings|Tags that topically describe the dataset. A list of supported tags is maintained in the [tags.yaml](tags.yaml) file in this repo. If you want to recommend a tag that is not included in [tags.yaml](tags.yaml), please submit a pull request to add it to that file.|
|**License**|String|An explanation of the dataset license and/or a URL to more information about data terms of use of the dataset|
|**Resources**|List of lists|A list of AWS resources that users can use to consume the data. Each resource entry requires the metadata below:|
|**Resources > Description**|String|A technical description of the data available within the AWS resource, including information about file formats and scope.|
|**Resources > ARN**|String|Amazon Resource Name for resource, e.g. arn:aws:s3:::commoncrawl|
|**Resources > Region**|String|AWS region unique identifier, e.g. us-east-1|
|**Resources > Type**|String|Can be _CloudFront Distribution_, _DB Snapshot_, _S3 Bucket_, or _SNS Topic_. A list of supported resources is maintained in the [resources.yaml](resources.yaml) file in this repo. If you want to recommend a resource that is not included in [resources.yaml](resources.yaml), please submit a pull request to add it to that file.|

Note also that we use the name of each YAML file as the URL slug for each dataset on the Registry of Open Data on AWS website. E.g. the metadata from `1000-genomes.yaml` is listed at `http://url/1000-genomes/`

### Example entry

Here is an example of the metadata behind this dataset: https://URL/hirlam/

```yaml
Name: HIRLAM Weather Model
Description: HIRLAM (High Resolution Limited Area Model) is an operational synoptic and mesoscale weather prediction model managed by the Finnish Meteorological Institute.
Documentation: http://en.ilmatieteenlaitos.fi/open-data-on-aws-s3
Contact: avoin-data@fmi.fi
UpdateFrequency: The data is updated four times a day with analysis hours 00, 06, 12 and 18. Corresponding model runs are available roughly five hours after analysis time (~ after model run has started).
Tags:
  - earth observation
  - weather
  - meteorological
License: Creative Commons Attribution 4.0 International (CC BY 4.0)
Resources:
  - Description: Surface GRIB files
    ARN: arn:aws:s3:::fmi-opendata-rcrhirlam-surface-grib
    Region: eu-west-1
    Type: S3 Bucket
  - Description: Pressure GRIB files
    ARN: arn:aws:s3:::fmi-opendata-rcrhirlam-pressure-grib
    Region: eu-west-1
    Type: S3 Bucket
  - Description: Notifications for new surface data
    ARN: arn:aws:sns:eu-west-1:916174725480:new-fmi-opendata-rcrhirlam-surface-grib
    Region: eu-west-1
    Type: SNS Topic
  - Description: Notifications for new pressure data
    ARN: arn:aws:sns:eu-west-1:916174725480:new-fmi-opendata-rcrhirlam-pressure-GRIB
    Region: eu-west-1
    Type: SNS Topic
```
