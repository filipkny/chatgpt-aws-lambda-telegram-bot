import json
import os

import requests
from models.user import User
from openai_client import OpenAIClient
from services.user_service import create_user, get_user_by_telegram_id


TOKEN = os.environ['TELEGRAM_TOKEN']
BASE_URL = "https://api.telegram.org/bot{}".format(TOKEN)
SEND_MESSAGE_URL = BASE_URL + "/sendMessage"


def extract_body(event) -> dict:
    if "body" in event:
        return json.loads(event["body"]) if type(event["body"]) == str else\
            event["body"]
    else:
        raise Exception("No body in event")


def extract_user(body) -> User:
    user_data = body["message"]["from"]
    return User(user_data)


def send_response(response: str, chat_id: int):
    data = {"text": response.encode("utf8"), "chat_id": chat_id}
    requests.post(SEND_MESSAGE_URL, data)


def build_response(message: str, first_name: str):
    chat_gpt = OpenAIClient()
    return f"ChatGPT repsonse: {chat_gpt.generate_response(message)}"


def reply(event, context):
    body = extract_body(event)
    
    message = str(body["message"]["text"])
    chat_id = body["message"]["chat"]["id"]
    from_user = extract_user(body)

    existing_user = get_user_by_telegram_id(from_user.telegram_id)
    if not existing_user:
        existing_user = create_user(from_user)

    response = build_response(message, existing_user.first_name)
    send_response(response, chat_id)

    return {"statusCode": 200}
