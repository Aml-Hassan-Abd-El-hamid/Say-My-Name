import streamlit as st
from gtts import gTTS 
import os 
from playsound import playsound

def st_layout():
    st.title('Say My Name')
    txt=st.text_area("enter your text here")
    model_name = st.radio(
    "What's your model of choise",
    ["gtts"],
    index=None,
    )
    btn=st.button("Turn my text into speach")
    return txt,btn,model_name
def turn_txt_to_speach(txt,model_name="gtts"):
    if model_name=="gtts":
        language = 'ar'
        myobj = gTTS(text=txt, lang=language, slow=False) 
        myobj.save("output.mp3") 
        playsound("output.mp3") 
def main():
    txt,btn,model_name=st_layout()
    if btn:
        turn_txt_to_speach(txt,model_name)
        st.write(model_name)

if __name__ == "__main__":
    main()
