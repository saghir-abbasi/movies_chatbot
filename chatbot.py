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

    # def get_response(self, prompt):
    #     prompt = f"""You are an Artificial Intelligence expert. 
    #                 You can reply about AI, programming, softwares related topics only.
    #                 Your reploy should be limited max 150 words.
    #                 if anything asked other than these fields you should reply "Please ask me about Artificial Intellignece only".
    #                 Here is the prompt to respond '{prompt}'
    #             """
    #     response = self.model.generate_content(prompt)
    #     return response.text
    # def get_chat_history(self, prompt):
    #     chat = self.model.start_chat(history=[])
    #     prompt = f"""You are an Artificial Intelligence expert. 
    #                 You can reply about AI, programming, softwares related topics only.
    #                 Your reploy should be limited max 150 words.
    #                 if anything asked other than these fields you should reply "Please ask me about Artificial Intellignece only".
    #                 Here is the prompt to respond '{prompt}'
    #             """
    #     response = chat.send_message(prompt)
    #     response = chat.history
    #     return response
        
    
    def get_response(self, prompt):
        prompt = f"""You are a Movies Expert having encyclopedia about movies. 
                    you are required to search all details about the movie '{prompt}'
                    provide your reply in following list format:
                    [Movie Name: movie name]
                    [Director: director name]
                    [Year: year of launching]
                    [Country: name of country where it was launched]
                    [Cast: major 5 actors names]
                    [Plot: write 100 words explaining theme and story of the movie]
                    [Recommended Movies: write list of 5 movies which are relevant to the given movie]
                """
        response = self.model.generate_content(prompt)
        return response.text
    def get_chat_history(self, prompt):
        chat = self.model.start_chat(history=[])
        prompt = f"""You are a Movies Expert having encyclopedia about movies. 
                    you are required to search all details about the movie '{prompt}'
                    provide your reply in following list format:
                    [Movie Name: movie name]
                    [Director: director name]
                    [Year: year of launching]
                    [Country: name of country where it was launched]
                    [Cast: major 5 actors names]
                    [Plot: write 100 words explaining theme and story of the movie]
                    [Recommended Movies: write list of 5 movies which are relevant to the given movie]
                """
        response = chat.send_message(prompt)
        response = chat.history
        return response