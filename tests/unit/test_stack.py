import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk.stack import Stack

def test_sqs_queue_created():
    app = core.App()
    stack = Stack(app, "app-name")
    template = assertions.Template.from_stack(stack)

    template.has_resource_properties("AWS::SQS::Queue", {
        "VisibilityTimeout": 300
    })
