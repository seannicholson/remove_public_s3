# remove_public_s3

This is an example script on using AWS API with Python module boto3 to query for S3 buckets in a configured region.
Script queries for the S3 bucket permissions looking for the All Users having read access. If a bucket has read access
the script then removes that grant and reapplies the S3 bucket permissions minus the All Users to the Bucket and to all
contained keys.

This script is provided with no warrantee and is provided as an example on how to accomplish making these files in Python 2.7.x

#Script configuration
default boto3 config
Create ~/.aws/config and ~/.aws/credentials

~/.aws/config

[default]

region=

~/.aws/credential

[default]

aws_access_key_id =

aws_secret_access_key =


#Script Requirements
This script is written in Python 2.7.x (X > 10)
This script requires the following PIP modules to run
Modules: sys, boto3

Example Python module install
MAC/Linux "pip install boto3"
Windows "python -m pip install boto3"
