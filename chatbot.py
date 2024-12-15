import google.generativeai as genai

from dotenv import load_dotenv
import os
import json
import re
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
        prompt = f"""You are a Movies Expert having encyclopedia about movies. 
                    you are required to search all details about the movie '{prompt}'
                    if no relevant record is found simply answer "Sorry. No movie found".
                    if found then provide your reply in json format:
                    Movie Name: movie name
                    Director: director name
                    Year: year of launching
                    Genre: genre of the movie
                    Country: name of country where it was launched
                    Cast: major 5 actors names
                    Plot: write 100 words explaining theme and story of the movie
                    Recommended Movies: write list of 5 movies which are relevant to the given movie
                """
        response = self.model.generate_content(prompt)
        
        # return response.text
        input_text = response.text

        json_match = re.search(r"{.*}", input_text, re.DOTALL)

        if json_match:
            json_text = json_match.group(0)  # Extract the JSON part

            try:
                # Step 2: Parse the cleaned JSON
                parsed_data = json.loads(json_text)
                output_json = json.dumps(parsed_data, indent=2)
                data = json.loads(output_json)
                return(data)
            except json.JSONDecodeError as e:
                return("Failed")
        else:
            return("Failed")