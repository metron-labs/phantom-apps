# File: awscloudtrail_consts.py
# Copyright (c) 2019-2021 Splunk Inc.
#
# Licensed under Apache 2.0 (https://www.apache.org/licenses/LICENSE-2.0.txt)
#
AWS_CLOUDTRAIL_REGIONS = {
    "US East (Ohio)": "us-east-2",
    "US East (N. Virginia)": "us-east-1",
    "US West (N. California)": "us-west-1",
    "US West (Oregon)": "us-west-2",
    "Asia Pacific (Hong Kong)": "ap-east-1",
    "Canada (Central)": "ca-central-1",
    "Asia Pacific (Mumbai)": "ap-south-1",
    "Asia Pacific (Osaka-Local)": "ap-northeast-3",
    "Asia Pacific (Seoul)": "ap-northeast-2",
    "Asia Pacific (Singapore)": "ap-southeast-1",
    "Asia Pacific (Sydney)": "ap-southeast-2",
    "Asia Pacific (Tokyo)": "ap-northeast-1",
    "China (Beijing)": "cn-north-1",
    "China (Ningxia)": "cn-northwest-1",
    "EU (Frankfurt)": "eu-central-1",
    "EU (Stockholm)": "eu-north-1",
    "EU (Ireland)": "eu-west-1",
    "EU (London)": "eu-west-2",
    "EU (Paris)": "eu-west-3",
    "Middle East (Bahrain)": "me-south-1",
    "AWS GovCloud (US-East)": "us-gov-east-1",
    "AWS GovCloud (US-West)": "us-gov-west-1",
    "South America (São Paulo)": "sa-east-1"
}
AWSCLOUDTRAIL_DICT_MAP = {
            'describe_trails': 'trailList',
            'lookup_events': 'Events'
        }
AWSCLOUDTRAIL_INVALID_LIMIT = 'Please provide a non-zero positive integer in the max_results'
AWSCLOUDTRAIL_BAD_ASSET_CONFIG_MSG = 'Please provide access keys or select assume role check box in asset configuration'
