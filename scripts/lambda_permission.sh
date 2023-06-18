#!/bin/bash

# specify the prefix you're looking for
prefix="ChatgptTelegramBotLambda"

# get all Lambda functions
lambdas=$(aws lambda list-functions --query 'Functions[*].FunctionName' --output text)

# loop through the functions
for lambda in $lambdas; do
  # check if the function name starts with the prefix
  if [[ $lambda == $prefix* ]]; then
    # print the function name
    FUNCTION_NAME=$lambda
  fi
done

ROLE_ARN=$(aws lambda get-function --function-name ${FUNCTION_NAME} --query 'Configuration.Role' --output text)
role_name=$(echo $ROLE_ARN | cut -d'/' -f2)
policy_arn="arn:aws:iam::aws:policy/service-role/AWSLambdaVPCAccessExecutionRole"
aws iam attach-role-policy --role-name $role_name --policy-arn $policy_arn

echo "Attached AWSLambdaVPCAccessExecutionRole policy to ${ROLE_ARN}"

