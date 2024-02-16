import streamlit as st
import os

#page 

class App:
    def __init__(self) -> None:
        pass

    def home(self):
        st.title("My App")    
        st.text("This project is very well mak mak")
        st.header("Contact me")
        # Correct the HTML syntax for embedding links
        st.markdown("<ul><a href='https://www.facebook.com/12ize12'><li>Facebook me</li></a></ul>", unsafe_allow_html=True)

    def sidebar(self):
        pass

    # Add the 'self' parameter to the run method
    def run(self):
        self.home()
    
if __name__ == "__main__":
    App().run()
