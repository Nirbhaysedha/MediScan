from runtime_ocr import docr_read
from dotenv import load_dotenv,find_dotenv
load_dotenv()
from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

import os
from langchain.llms import OpenAI

def llmp():
    llm=OpenAI(temperature=0.1,openai_api_key=os.environ['openai_api_key'])
    l1=docr_read()
    a=llm.predict(f"you are medicine advisor provide all details of this medicine i am giving you context {l1}")
    return a
a=llmp()
print(a)



