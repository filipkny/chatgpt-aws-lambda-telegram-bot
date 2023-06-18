import openai
import os


class OpenAIClient:
    def __init__(self):
        openai.api_key = os.environ['OPENAI_API_KEY']
        self.model_engine = "text-davinci-002"
        self.prompt = "User: Hello, how are you?\nChatGPT: I'm fine, thank you. How can I help you today?\nUser: "

    def generate_response(self, user_input: str) -> str:
        prompt = self.prompt + user_input + "\nChatGPT:"
        response = openai.Completion.create(
            engine=self.model_engine,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        return response.choices[0].text.strip()