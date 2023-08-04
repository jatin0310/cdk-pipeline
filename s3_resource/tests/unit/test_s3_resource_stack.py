import aws_cdk as core
import aws_cdk.assertions as assertions

from s3_resource.s3_resource_stack import S3ResourceStack

# example tests. To run these tests, uncomment this file along with the example
# resource in s3_resource/s3_resource_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = S3ResourceStack(app, "s3-resource")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
