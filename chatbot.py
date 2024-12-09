import google.generativeai as genai

from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()


class Chatbot:
    def __init__(self):
        # Access environment variables
        self.GOOGLE_API_KEY = os.getenv("API_KEY")
        self.debug_mode = os.getenv("DEBUG")
        genai.configure(api_key=self.GOOGLE_API_KEY)
        self.model = genai.GenerativeModel('gemini-1.5-flash')

    def get_response(self, prompt):
        prompt = f"""You are an Artificial Intelligence expert. 
                    You can reply about AI, programming, softwares related topics only.
                    Your reploy should be limited max 150 words.
                    if anything asked other than these fields you should reply "Please ask me about Artificial Intellignece only".
                    Here is the prompt to respond '{prompt}'
                """
        response = self.model.generate_content(prompt)
        return response.text
    def get_chat_history(self, prompt):
        chat = self.model.start_chat(history=[])
        prompt = f"""You are an Artificial Intelligence expert. 
                    You can reply about AI, programming, softwares related topics only.
                    Your reploy should be limited max 150 words.
                    if anything asked other than these fields you should reply "Please ask me about Artificial Intellignece only".
                    Here is the prompt to respond '{prompt}'
                """
        response = chat.send_message(prompt)
        response = chat.history
        return response
        # for entry in response:
        #     for part in entry.parts:
        #         print(entry.role, ":", part.text)