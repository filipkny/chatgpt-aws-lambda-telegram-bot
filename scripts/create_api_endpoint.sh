
aws apigateway create-rest-api --name 'ChatgptTelegramBot2' &&
REST_API_ID=$(aws apigateway get-rest-apis --query 'items[?name==`ChatgptTelegramBot2`].id' --output text) &&
PARENT_RESOURCE_ID=$(aws apigateway get-resources --rest-api-id $REST_API_ID --query 'items[?path==`/`].id' --output text) &&
aws apigateway create-resource --rest-api-id $REST_API_ID --parent-id $PARENT_RESOURCE_ID --path-part 'sendMessage' &&
RESOURCE_ID=$(aws apigateway get-resources --rest-api-id $REST_API_ID --query 'items[?path==`/sendMessage`].id' --output text) &&
aws apigateway put-method --rest-api-id $REST_API_ID --resource-id $RESOURCE_ID --http-method 'POST' --authorization-type 'NONE' &&
aws apigateway put-integration --rest-api-id $REST_API_ID --resource-id $RESOURCE_ID --http-method 'POST' --type 'AWS_PROXY' --integration-http-method 'POST' --uri 'arn:aws:apigateway:us-east-1:lambda:path/2015-03-31/functions/<YOUR_LAMBDA_ARN>/invocations' &&
aws apigateway create-deployment --rest-api-id $REST_API_ID --stage-name 'prod'
echo "https://$REST_API_ID.execute-api.us-east-1.amazonaws.com/prod/sendMessage"