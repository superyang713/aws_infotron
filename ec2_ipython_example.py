# coding: utf-8
key_name = 'python_automation_key'
key_path = key_name + '.pen'
key_path = key_name + '.pem'
key = ec2.create_key_pair(KeyName=key_name)
key
type(key)
key.key_material
with open(key_path, 'w') as key_file:
    key_file.write(key.key_material)
    
get_ipython().run_line_magic('ls', '')
get_ipython().run_line_magic('ls', '-l python_automation_key.pem')
import os, stat
os.chmod(python_automation_key.pem, 400)
os.chmod(key_path, 400)
get_ipython().run_line_magic('ls', '-l python_automation_key.pem')
os.chmod(key_path, 0o400)
get_ipython().run_line_magic('ll', '')
ec2.images.filter(Owners=['amazon'])
amazon_image_list = list(ec2.images.filter(Owners=['amazon']))
len(amazon_image_list)
print(amazon_image_list[:50])
img = ec2.Image('aki-04206613')
img.name
img = ec2.Image('ami-04681a1dbd79675a5')
img.name
session.region_name
ec2_east2 = session.resource('ec2', region_name='us-east-2')
img_east2 = ec2_east2.Image('ami-04681a1dbd79675a5')
img_east2.name
img_east2 = ec2_east2.Image('ami-04681a1dbd79675fsafasdfsafadsfsdfsafasdfasdsdfsadfasasdasfa5')
img_east2.name
img.name
ami_name = 'amzn2-ami-hvm-2.0.20180810-x86_64-gp2'
filters = [{'Name': 'name', 'Value': [ami_name]}]
list(ec2.images.filter(Owners=['amazon'], Filers=filters))
list(ec2.images.filter(Owners=['amazon'], Filters=filters))
filters = [{'Name': 'name', 'Values': [ami_name]}]
list(ec2.images.filter(Owners=['amazon'], Filters=filters))
list(ec2_east2.images.filter(Owners=['amazon'], Filters=filters))
img
instances = ec2.create_instances(ImageId=img.id, MinCount=1, MaxCount=1, InstanceType='t2.micro', KeyName=key.key_name)
instances
inst = instances[0]
inst.terminate()
instances = ec2.create_instances(ImageId=img.id, MinCount=1, MaxCount=1, InstanceType='t2.micro', KeyName=key.key_name)
inst
inst = instances[0]
inst
inst.public_dns_name
inst.public_dns_name
inst.public_dns_name
inst.wait_until_running()
inst.reload()
inst.public_dns_name
inst.security_groups
sg = ec2.SecurityGroup(inst.security_groups[0]['GroupId'])
sg
inst.security_groups
inst.security_groups
inst.security_groups
inst.reload()
inst.security_groups
inst.security_groups
inst.reload()
inst.security_groups
sg
sg.authorize_ingress(IpPermissions=[{'FromPort': 22, 'ToPort': 22, 'IpProtocol': 'TCP', 'IpRanges': [{'CidrIp': '18.74.5.146/32'}]}])
get_ipython().run_line_magic('history', '')
