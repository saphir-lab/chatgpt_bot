import openai
import os
from dotenv import load_dotenv

class Chatbot:
    def __init__(self):
        load_dotenv()
        openai.api_key=os.getenv("OPENAI_API_KEY")
    
    def get_response(self, user_input):
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=user_input,
                max_tokens=2000,    # number of words in the response
                temperature=0.5     # value from 0 to 1  (number near zero: best accuracy but response less diverse. Near 1, the opposite)
            ).choices[0].text
        except Exception as e:
            response = f"ERROR: {str(e)}"
        return response

if __name__ == "__main__":
    question = "Suggest three names for an animal that is a superhero"
    question = "Suggest three names for a black horse that is a superhero"
    # question = "timeout"

    chatbot = Chatbot()
    response = chatbot.get_response(question)
    print(response)