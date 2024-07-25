from aws_cdk import (
    Stack,
    aws_lambda,
    aws_apigatewayv2 as apigwv2,
    aws_apigatewayv2_integrations as integrations,
    aws_iam,
)
from constructs import Construct


class InfrastructureStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Define the Lambda function using the correct path
        random_drink_lambda = aws_lambda.Function(
            self,  # the logical resource that will be the owner of this lambda function
            id="RandomDrinkFunctionV2",  # give it a random name
            code=aws_lambda.Code.from_asset(
                "./compute/"
            ),  # Ensure this path is correct
            handler="random_drink.lambda_handler",  # specified handler, which is the python function and package we want Lambda to use when it is triggered
            runtime=aws_lambda.Runtime.PYTHON_3_8,  # tell it what runtime to use
        )

        # Create the HTTP API
        http_api = apigwv2.HttpApi(self, "RandomDrinkHttpApi")

        # Create the Lambda integration
        random_drink_integration = integrations.HttpLambdaIntegration(
            "RandomDrinkIntegration", handler=random_drink_lambda
        )

        # Add routes to the HTTP API
        http_api.add_routes(
            path="/random_drink",
            methods=[apigwv2.HttpMethod.GET],
            integration=random_drink_integration,
        )
        http_api.add_routes(
            path="/random_drink",
            methods=[apigwv2.HttpMethod.ANY],
            integration=random_drink_integration,
        )

        # Add permission for API Gateway to invoke the Lambda function
        random_drink_lambda.add_permission(
            "ApiGatewayInvoke",
            principal=aws_iam.ServicePrincipal("apigateway.amazonaws.com"),
            source_arn=f"arn:aws:execute-api:us-east-1:975050337340:{http_api.http_api_id}/*",
        )
