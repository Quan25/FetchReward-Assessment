import yaml
import boto3

def createInstance():
    try:
        #get specific information from the yaml file
        a_yaml_file = open("test.yaml")
        parsed_yaml_file = yaml.load(a_yaml_file, Loader=yaml.FullLoader)

        server=parsed_yaml_file.get("server")

        volumes = server.get("volumes")

        users = server.get("users")

        # start creating an EC2 instance
        print ("Creating EC2 instance")

        resource_ec2=boto3.client("ec2")
        resource_ec2.run_instances(
            BlockDeviceMappings=[
            {
                'DeviceName': volumes[0]["device"],
                'Ebs': {
                    'DeleteOnTermination':False,
                    'VolumeSize': volumes[0]["size_gb"],
                    'VolumeType': "gp2",
                }
                },

            ],
            ImageId=server["ami_type"],
            MinCount=server["min_count"],
            MaxCount=server["max_count"],
            InstanceType=server["instance_type"],
            KeyName="ec2-key",
            TagSpecifications=[
                {
                'ResourceType': 'volume',
                'Tags': [
                  {
                      'Key': 'Name',
                      'Value': 'volume 1'
                  },
                ]
                },
            ],
            UserData='''
            #!/bin/bash
            useradd user1
            useradd user2
            '''
        )

    except Exception as e:
            print(e)

    #create a second volume as needed
    volume2=resource_ec2.create_volume(
          AvailabilityZone='us-west-1a',
          Encrypted=True,
          Size=volumes[1]["size_gb"],
          VolumeType="gp2",
          TagSpecifications=[
              {
                  'ResourceType': 'volume',
                  'Tags': [
                      {
                          'Key': 'Name',
                          'Value': 'volume 2'
                      },
                  ]
              },
          ],
    )

    #get the instance_id of the ec2 instance we just created
    ec2 = boto3.resource('ec2')
    instance_id = ""
    instances = ec2.instances.filter(
        Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
    for instance in instances:
        instance_id = instance.id


    #attach the second volume to instance
    attach_response=resource_ec2.attach_volume(Device=volumes[1]["device"],
          InstanceId=instance_id,
          VolumeId=volume2["VolumeId"]
         )

if __name__ == "__main__":
    createInstance()
