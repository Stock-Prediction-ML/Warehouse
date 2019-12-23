# NiFi Templates

A collection of NiFi templates for this project.

## List

* **Basic_Twitter_Template**: A basic twitter flow that collects from twitter and puts JSON in S3

## Template Details

Details on templates

### Basic_Twitter_Template

**Description**: A basic twitter flow that collects from twitter and puts JSON in S3.

#### Required inputs

The following values require input for operation of this template.

Note: Programmatic access for NiFi is required.

* S3
  * Bucket: The name of the bucket where files will be stored
  * Access Key: AWS credentails for NiFi programmatic access
  * Secret Key: AWS credentails for NiFi programmatic access
* Twitter
  * Consumer Key: Twiiter App API credientials
  * Consumer Secret: Twiiter App API credientials
  * Access Token: Twiiter App API credientials
  * Access Token Secret: Twiiter App API credientials
