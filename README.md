# Registry of Open Data on AWS

A repository of publicly available datasets that are available for access from AWS resources. Note that datasets in this registry are available via AWS resources, but they are not provided by AWS; these datasets are owned and maintained by a variety government organizations, researchers, businesses, and individuals. 

## What is this for?

When data is shared on AWS, anyone can analyze it and build services on top of it using a broad range of compute and data analytics products, including [Amazon EC2](https://aws.amazon.com/ec2/), [Amazon Athena](https://aws.amazon.com/athena/), [AWS Lambda](https://aws.amazon.com/lambda/), and [Amazon EMR](https://aws.amazon.com/emr/). Sharing data in the cloud lets data users spend more time on data analysis rather than data acquisition. This repository exists to help people promote and discover datasets that are available via AWS resources.

## How are datasets added to the registry?

Each dataset in this repository is described with metadata saved in a YAML file in the [/datasets](/datasets) directory. We use these YAML files to provide three services:

- A [Registry of Open Data on AWS browser](https://registry.opendata.aws/).
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
DataAtWork:
  - Title: 
    URL: 
    AuthorName: 
    AuthorURL:
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
|**DataAtWork** (Optional)|List of lists|A list of links to examples of the dataset being used. May include tutorials, demos, or applications.|
|**DataAtWork > Title**|String|The title of the example usage of the data.|
|**DataAtWork > URL**|URL|A link to the example.|
|**DataAtWork > AuthorName**|String|Name of person or entity that created the example.|
|**DataAtWork > AuthorURL**|String|(Optional) URL for person or entity that created the example.|


Note also that we use the name of each YAML file as the URL slug for each dataset on the [Registry of Open Data on AWS website](https://registry.opendata.aws). E.g. the metadata from `1000-genomes.yaml` is listed at `https://registry.opendata.aws/1000-genomes/`

### Example entry

Here is an example of the metadata behind this dataset registration: https://registry.opendata.aws/gdelt/

```yaml
Name: Global Database of Events, Language and Tone (GDELT)
Description: |
  This project Project monitors the world's broadcast, print,
  and web news from nearly every corner of every country in
  over 100 languages and identifies the people, locations,
  organizations, counts, themes, sources, emotions, counts,
  quotes, images and events driving our global society every
  second of every day.
Documentation: http://www.gdeltproject.org/
Contact: http://www.gdeltproject.org/about.html#contact
UpdateFrequency: Daily
Tags:
  - aws-pds
  - events
License: http://www.gdeltproject.org/about.html#termsofuse
Resources:
  - Description: Project data files
    ARN: arn:aws:s3:::gdelt-open-data
    Region: us-east-1
    Type: S3 Bucket
  - Description: Notifications for new data
    ARN: arn:aws:sns:us-east-1:928094251383:gdelt-csv
    Region: us-east-1
    Type: SNS Topic
DataAtWork:
  - Title: Exploring GDELT with Athena
    URL: http://blog.julien.org/2017/03/exploring-gdelt-data-set-with-amazon.html
    AuthorName: Julien Simon
    AuthorURL: https://twitter.com/julsimon
  - Title: Running R on Amazon Athena
    URL: https://aws.amazon.com/blogs/big-data/running-r-on-amazon-athena/
    AuthorName: Gopal Wunnava
    AuthorURL: https://www.linkedin.com/in/gopal-wunnava-b11a77/
  - Title: Bootstrapping GeoMesa HBase on AWS S3
    URL: http://www.geomesa.org/documentation/tutorials/geomesa-hbase-s3-on-aws.html
    AuthorName: Commonwealth Computer Research, Inc.
    AuthorURL: https://www.ccri.com
  - Title: Creating PySpark DataFrame from CSV in AWS S3 in EMR
    URL: https://gist.github.com/jakechen/6955f2de51212163312b6430555b8e0b
    AuthorName: Jake Chen
    AuthorURL: https://github.com/jakechen
```

## How can I contribute?

You are welcome to contribute dataset entries or usage examples to the Registry of Open Data on AWS. Please review our [contribution guidelines](CONTRIBUTING.md). 
