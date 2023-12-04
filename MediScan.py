import cv2
import streamlit as st
import easyocr
from runtime_ocr import docr_read
from dotenv import load_dotenv,find_dotenv
load_dotenv()
from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

import os
from langchain.llms import GooglePalm
from langchain.llms import OpenAI

reader = easyocr.Reader(['en'])  


def perform_ocr(frame):
    result = reader.readtext(frame)
    global response
    for detection in result:
        response += detection[1] + "\n"
    return result

def main():
    global response

    st.title("MediScan!")

    cap = cv2.VideoCapture(0)  
    show_video = st.empty()
    start_recording = st.button("Start Recording")
    stop_recording = st.button("Stop Recording")

    recording = False

    if not cap.isOpened():
        st.error("Unable to access the camera.")
        return

    while True:
        ret, frame = cap.read()

        if start_recording:
            response = "" 
            recording = True
            start_recording = False

        if stop_recording:
            recording = False
            stop_recording = False

        if recording and ret:
            result = perform_ocr(frame)
            for detection in result:
                pts = detection[0]
                x1, y1, x2, y2 = map(int, (pts[0][0], pts[0][1], pts[2][0], pts[2][1]))
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, detection[1], (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            show_video.image(frame, channels="RGB", use_column_width=True)
            llm=OpenAI(temperature=0.1,openai_api_key=os.environ['openai_api_key'])
            
            a=llm.predict(f"give details of this medicine in all aspects in pointers and try to integrate emojis  {response}")
            st.write(a)


        else:
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                show_video.image(frame, channels="RGB", use_column_width=True)

        if not recording:
            break

    cap.release()

if __name__ == "__main__":
    main()

