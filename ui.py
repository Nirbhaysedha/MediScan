import streamlit as st
from runtime_ocr import docr_read
from dotenv import load_dotenv,find_dotenv
load_dotenv()
from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
import os
from test import llmp
import time
import cv2
from easyocr import Reader    




