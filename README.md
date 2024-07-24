## How to Build & Deploy an AWS Lambda Function in Python

In this tutorial, we turn a simple Python function into a serverless HTTP API that we can call using an HTTP endpoint from anywhere with internet access.

### Architecture

<img width=600 class="Architecture" src="https://github.com/markbuckle/AWS-Python-Deploy/blob/main/Architecture.png?raw=true">

### Writing your Python function

Create a simple python function i.e. one that suggests/prints a random drink

### Creating a Lambda function

Go to the [AWS Console](https://us-east-1.console.aws.amazon.com/console/home?region=us-east-1#) and search for ['Lambda'](https://us-east-1.console.aws.amazon.com/lambda/home?region=us-east-1#/functions).

<li>Click 'create function'.</li>

<li>There are good templates if you want to explore them, but for this tutorial we will just use 'Author from Scratch'.</li>

<li>Type in a function name of your choice and select the relevant Python Runtime.</li>

<li>Use a default function name and click 'test'.</li>

### Update Lambda function code

<li>Copy and paste function code from VS code into Lambda.</li>

<li>To use the function you have to change the handler as well.</li>

<li>Change the {message} string to a json payload object. This makes it easier to manage complex responses down the line.</li>

### Integrating Lambda with API Gateway

<li>Add a trigger so that Lambda knows when it should execute this function.</li>

<li>In this case we used a http endpoint so that we could call it from anywhere with itnernet access (i.e. terminal or browser).</li>

<li>Click 'add trigger' then choose 'API Gateway'.</li>

<li>Create a new API, then click 'HTTP APIs'.</li>

<br></br>
As per[ Amazon's website](https://aws.amazon.com/about-aws/whats-new/2019/12/amazon-api-gateway-offers-faster-cheaper-simpler-apis-using-http-apis-preview/), HTTP APIs are up to 71% cheaper compared to REST APIs, but offer only API proxy functionality. HTTP APIs are optimized for performance - they offer the core functionality of API Gateway at a lower price.

<li>For security select 'Open' then click 'Add'</li>

### Testing the API integration

<li>Scroll down and click the API Endpoint link. It should look something like this: https://ge30cp599b.execute-api.us-east-1.amazonaws.com/default/RandomDrink</li>

You can also call this in VS code using:

```sh
curl https://ge30cp599b.execute-api.us-east-1.amazonaws.com/default/RandomDrink
```

### Add a Throttling Limit

Now you have an API you can publicly use. You probably want to set some throttling limits before you start using it in any serious way. It's a bad idea to have an unbounded API because if somebody finds it or if you have a large amount of traffic then you can be stuck with a very large bill.

<li>Click on the API Gateway.</li>

<li>Scroll down on the sidebar to Protect -> Throttling.</li>

<li>Select a Stage then 'edit' the Default Route Setting.</li>

### Wrapping up

Were done. We just deployed a Python Lambda function to the cloud. Since it's serverless it should scale quite well out of the box.

The only downside of this method is that we had to set quite a few manual settings/configurations to make this work. This is quite time consuming and can be hard to audit when you have hundreds of functions or APIs to manage. Next time we will do all this as Infrastruture as Code so that we can review, audit or even commit to Github.
