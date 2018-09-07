# coding: utf-8
import boto3
session = boto3.Session(profile_name='pythonAutomation')
as_client = session.client('autoscaling')
as_client.describe_auto_scaling_groups()
get_ipython().run_line_magic('pprint', '')
get_ipython().run_line_magic('pprint', '')
as_client.describe_auto_scaling_groups()
as_client.describe_policies()
