# this is the code that goes into the lambda_fucntion.py tab in the AWS Lambda Console
import json
import random

def random_drink():
    drinks= [ "coffee", "tea", "beer", "wine", "water", "juice"]
    return random.choice(drinks)

# handler: what python executes when the trigger is called for the Lambda
def lambda_handler(event, context):
    drink = random_drink()
    message = f"You should drink some {drink}"
    
    return {
        'statusCode': 200,
        # returns a json payload object
        'body': json.dumps({"message": message, "drink": drink})
    }
