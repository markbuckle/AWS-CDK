## Infrastructure as Code: How to Deploy an Python Lambda Function using the AWS Cloud Development Kit (CDK)

In this tutorial, we re-created the Python Lambda function and API Gateway from the previous tutorial using "infrastructure-as-code" (with AWS CDK). We will use the Python version of CDK to allow us to manage more projects, bootstrap or migrate projects to different accounts.

### Infrastructure as code

All of the resources we created last time including the Lambda and Gateway function we refer to as **Infrastructure** 

Luckily there are tools that exist which allow us to create, deploy and maintain all of this infrastructure using code.

Most of the time this infrastructure is defined using markup formatting language such as **json** or **yaml**

But there are frameworks that allow us to do this in a scripting language such as **Python** or **Typescript** which is easier because you have thigns like type-referencing, IDE completion, loops, conditions, etc. 

This is also great because instead of having to manually click things in our console, we end up with a bunch of code that we can use to deploy our infrastructure with.

Popular Infrastructure-as-Code (IAC) Frameworks include Terraform, Ansible, Pulumi and AWS CDK. This makes the most sense since we are already on a AWS stack.

### AWS CDK

#### Architecture:

<img width=600 class="Architecture" src="https://github.com/markbuckle/AWS-Python-Deploy/blob/main/Architecture.png?raw=true">

CDK will allow us to find and deploy our Lambda function & API Gateway integration as code. 

###  Prerequisites

<ol>1. AWS CLI</ol>
<ol>2. NodeJS (with npm)</ol>

Once installed, try the following commands so that everything is setup to be working properly:

```sh
aws sts get-caller-identity
```
^ this prooves that you have AWS CLI configured and that you are using the correct account

```sh
npm --version
```
to check that you have the right node version installed

### Install and bootstrap CDK

Install the latest cdk version:
```sh
npm install -g aws-cdk@latest
```

check that it is working by typing:
```sh
cdk --version
```
Next run a boostrap CDK
```sh
cdk bootstrap aws://{account#}/{region}
```

Once you run this it will create something called a cloud formation stack in your account for that region. A cloud formation stack is essentially logical grouping for your resources.

### Create your project
Create a new folder:
```sh
mkdir infrastructure
```
Navigate to that folder:
```sh
cd infrastructure
```
Type:
```sh
cdk init --language python
```
You will see that the last command made a bunch of files for us. When we deploy these files it will create another cloud formation stack in our account.

### Create the Lambda function

Now we have to add the Lambda function and API Gateway from the first tutorial to our resources stack. 

First, add the below to the requirements.txt file:
```sh
aws-cdk.core
aws-cdk.aws_lambda
```
Install the modules using this command:
```sh
pip install -r requirements.txt
```
Once the dependencies have been installed we can move over our function from the [AWS Lambda->functions console](https://us-east-1.console.aws.amazon.com/lambda/home?region=us-east-1#/functions) into a folder within /infrastructure called /compute.

<img width=900 class="compute" src="https://github.com/markbuckle/AWS-CDK/blob/main/compute-folder.png?raw=true">

In the infrastructure_stack.py file, import the lastest aws_lambda package from the [documentation](https://docs.aws.amazon.com/lambda/) and create a new fucntion object:

```sh
from aws_cdk import aws_lambda
```

```sh
# The code that defines your stack goes here
 random_drink_function =aws_lambda.Function(
            self, # the logical resource that will be the owner of this lambda function
            id="RandomDrinkFunctionV2", # give it a random name
            code=aws_lambda.Code.from_asset("./compute/"), # where Lambda finds the code, pointed to our compute folder
            handler="random_drink_lambda_handler", # specified handler, which is the python function and package we want Lambda to use when it is triggered
            runtime=aws_lambda.Runtime.PYTHON_3_12 # tell it what runtime to use
            )
```
Finally run:
```sh
cdk deploy
```
Head to the AWS Lambda function console to see if your new function with the code is stored.

### Create the API integration

Now that we have our Lambda function in the cloud, we can add our API integration

Add the latest [gateway integration module](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_apigatewayv2-readme.html) into the requriements.txt file:

<li>aws_cdk.aws_apigatewayv2</li>
<li>aws_cdk.aws_apigatewayv2_integrations</li>

Re-run:
```sh
pip install -r requirements.txt
```

### Wrapping up
