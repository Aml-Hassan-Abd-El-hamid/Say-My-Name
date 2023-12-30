import streamlit as st
from gtts import gTTS 
import os 
from playsound import playsound

def st_layout():
    st.title('Say My Name')
    txt=st.text_area("enter your text here")
    btn=st.button("Turn my text into speach")
    return txt,btn
def turn_txt_to_speach(txt):
    language = 'ar'
    myobj = gTTS(text=txt, lang=language, slow=False) 
    myobj.save("output.mp3") 
    playsound("output.mp3") 
def main():
    txt,btn=st_layout()
    if btn:
        turn_txt_to_speach(txt)

if __name__ == "__main__":
    main()
