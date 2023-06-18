## Description
This repository contains the template for deploying your own telegram ChatGPT powered chatbot. Features include:

- Poetry package managment set up
- OpenAI API integration
- SQLAlchemy integration
- AWS Lambda Test/Deploy scripts
- Github CI/CD AWS Lambda deployment
 
# Set up steps
0. Get you Telegram bot token (https://core.telegram.org/bots#how-do-i-create-a-bot) and add it to env.json and template.yaml env variables
1. Get your OpenAI API key (https://platform.openai.com/account/api-keys) and add it to env.json and template.yaml env variables
2. Install and download AWS SAM (https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html)
3. Set up your repo secrets 'AWS_ACCESS_KEY_ID' and 'AWS_SECRET_ACCESS_KEY' (https://docs.github.com/en/actions/security-guides/encrypted-secrets)
4. Add your DB env variables to env.json and template.yaml env variables.

# Quick testing
0. Make sure you have a clean local enviornment by running
'''
sh scripts/clean.sh
'''
1. Run test.sh to test your telegram bot lambda:
'''
sh scripts/test.sh
'''
If there are no errors, you can be confident that your lambda will work correctly when deployed.

# Quick delpoy
0. Make sure you have a clean local enviornment by running
'''
sh scripts/clean.sh
'''
1. If you don't have one, create an s3 bucket in your aws region 
'''
aws s3api create-bucket --bucket chatgpt-telegram-bot-lambda --region us-east-1
'''

2. Run test.sh to test your telegram bot lambda:
'''
sh scripts/deploy.sh
'''

3. Replace <YOUR_LAMBDA_ARN> and run:
'''
sh scripts/create_api_endpoint.sh
'''
Note: in these scripts it is assumed your region us-east-1. For a different region just replace 'us-east-1' with your region
If step 3 is successful, you should be able to call your lambda at:
https://{restapi_id}.execute-api.{region}.amazonaws.com/{stage_name}/{resource_path}

4. Add AWSLambdaVPCAccessExecutionRole role to the your Lambda's security group by running:
'''
sh scripts/lambda_permission.sh
'''

5. At this point you can try to make a POST request to your lambda endpoint. You can find the body at scripts/event.json. If you get an 
error, it is likely that it's related to permissions, and you can solve it following this (https://stackoverflow.com/questions/54067224/execution-failed-due-to-configuration-error-invalid-permissions-on-lambda-funct)

6. Once you confirm that the previous step is working correctly, you need to set the telegram bot webhook:
'''
curl --location 'https://api.telegram.org/bot<YOUR_TELEGRAM_BOT_TOKEN>/setWebhook' \
--header 'Content-Type: application/json' \
--data '{
    "url": "<YOUR_API_GATEWAY_ENDPOINT_URL>"
}'
'''

And you are done! At this point you should be able to communicate with you ChatGPT integrated telegram bot. Try it out!
Note: You may have to wait some minutes for the whole set up to be ready.