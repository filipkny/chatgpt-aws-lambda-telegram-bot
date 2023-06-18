poetry lock;
poetry export -f requirements.txt > requirements.txt;
mkdir package;
poetry run pip install -r requirements.txt -t ./package;
cp -r src/ package/;
sam build --template template.yaml --use-container;
cp package/psycopg2/* .aws-sam/build/ChatgptTelegramBotLambda/psycopg2;
sam package --output-template-file packaged.yaml --s3-bucket chatgpt-telegram-bot-lambda;
sam deploy --no-confirm-changeset --no-fail-on-empty-changeset --template-file packaged.yaml --region us-east-1 --capabilities CAPABILITY_IAM --stack-name ChatgptTelegramBotLambda;