'''importing program modules'''
import os
# import re
# import json
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.chains import llm
from .templates import prompt_temps
load_dotenv()

class LangChainAI:
    '''Company Data analysis'''

    def __init__(self):
        self.open_ai_key = os.getenv("OPENAI_API_KEY")
        self.llm_ai = OpenAI(
            temperature=0.9,
            openai_api_key=self.open_ai_key
            )

    def email_generator(
            self,
            person_json_data,
            company_data):
        ''' an email generator language model'''
        chained_llm = llm.LLMChain(
            llm=self.llm_ai,
            prompt=prompt_temps
        )
        input_data = {
            'company_data': company_data,
            'person_json_data': person_json_data
        }
        i = 0
        data = None
        # try to generate data for some number of time if data is empty
        max_iterations = 10
        while i < max_iterations and data is None:
            data = chained_llm.run(input_data)
            i += 1
        return data
