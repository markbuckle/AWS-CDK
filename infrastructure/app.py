from aws_cdk import (
    Stack,
    aws_lambda,
)
from constructs import Construct


class InfrastructureStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Define the Lambda function using the correct path
        random_drink_function = aws_lambda.Function(
            self,  # the logical resource that will be the owner of this lambda function
            id="RandomDrinkFunctionV2",  # give it a random name
            code=aws_lambda.Code.from_asset(
                "./compute/"
            ),  # Ensure this path is correct
            handler="random_drink.lambda_handler",  # specified handler, which is the python function and package we want Lambda to use when it is triggered
            runtime=aws_lambda.Runtime.PYTHON_3_8,  # tell it what runtime to use
        )
