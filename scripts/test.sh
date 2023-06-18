poetry lock;
poetry export -f requirements.txt > requirements.txt;
mkdir package;
poetry run pip install -r requirements.txt -t ./package;
cp -r src/ package/;
sam build --template template.yaml --use-container;
cp -r package/psycopg2/* .aws-sam/build/ChatgptTelegramBotLambda/psycopg2;
sam local invoke ChatgptTelegramBotLambda --debug --env-vars env.json --event scripts/event.json;