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

### Install and bootstrap CDK

### Create your project

### Create the Lambda function

### Create the API integration

### Wrapping up
