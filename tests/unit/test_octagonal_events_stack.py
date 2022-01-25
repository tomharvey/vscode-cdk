import aws_cdk as core
import aws_cdk.assertions as assertions

from octagonal_events.octagonal_events_stack import OctagonalEventsStack

# example tests. To run these tests, uncomment this file along with the example
# resource in octagonal_events/octagonal_events_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = OctagonalEventsStack(app, "octagonal-events")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
