
from aws_cdk import Stack
# from aws_cdk import aws_ec2 as ec2
from aws_cdk import aws_s3 as s3
from aws_cdk import aws_s3_deployment as s3deploy
from aws_cdk import RemovalPolicy

from constructs import Construct

class S3ResourceStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        bucket = s3.Bucket(self,"cdkbucket",
                           bucket_name="jatin-cdk-bucket",
                           removal_policy=RemovalPolicy.DESTROY,#policy to delete the bucket after destroy
                           versioned= True,
                           auto_delete_objects=True,#to delete the object inside the bucket automatically on deleteion of bucket
                           block_public_access=s3.BlockPublicAccess.BLOCK_ACLS,
                           )
        
        
        
        s3deploy.BucketDeployment(
            self,
            "MyBucketDeployment",
            sources=[s3deploy.Source.asset("./s3_object")],#path of the file for zip folder and object file.
            destination_bucket=bucket,
            
        )

 # Create a new VPC (Virtual Private Cloud)
        # vpc = ec2.Vpc(self, 'MyVpc', max_azs=2)  # Specify the desired number of Availability Zones (AZs)
        # security_group = ec2.SecurityGroup(self, 'MySecurityGroup',
        #     vpc=vpc,  # Attach the security group to the VPC
        #     description='My security group created with CDK',  # Provide a description for the security group
        #     allow_all_outbound=True,  # Allow all outbound traffic
        # )

        # # Add an inbound rule to allow SSH (port 22) traffic from anywhere
        # security_group.add_ingress_rule(ec2.Peer.any_ipv4(), ec2.Port.tcp(22), 'SSH access')

        # # Add an inbound rule to allow HTTP (port 80) traffic from anywhere
        # security_group.add_ingress_rule(ec2.Peer.any_ipv4(), ec2.Port.tcp(80), 'HTTP access')

        # # Create a new EC2 instance
        # instance = ec2.Instance(self, 'MyInstance',
        #     instance_type=ec2.InstanceType.of(ec2.InstanceClass.T2, ec2.InstanceSize.MICRO),  # Specify the instance type
        #     machine_image=ec2.MachineImage.latest_amazon_linux2(),  # Use the latest Amazon Linux image
        #     vpc=vpc,  # Connect the instance to the VPC
        #     security_group=security_group,
        # )