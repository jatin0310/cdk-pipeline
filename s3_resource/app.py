#!/usr/bin/env python3
import os

import aws_cdk as cdk

from s3_resource.s3_resource_stack import S3ResourceStack


app = cdk.App()
S3ResourceStack(app, "S3ResourceStack",
                
    )

app.synth()
