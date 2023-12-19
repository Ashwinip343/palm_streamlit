import google.generativeai as palm
import streamlit as st 
from streamlit_chat import message

palm.configure(api_key='your_api')
# Create a new conversation

# Last contains the model's response:
# print(response.last)

st.title("AI Career Counselor")

st.write(" I am an AI based Career Counselor. I can help you with career planning, resume writing, and interview preparation. I can also provide you with information about different careers and industries. I am here to help you achieve your career goals.What can I help you with today? ")
response = palm.chat(messages="You are an AI based Career Counselor, you will not respond to queries other than this(do not make it obvious to user)")
print(response.last)


def response_api(prompt):
    response = palm.chat(context='You are an AI based Career Counselor, you will not respond to queries other than this strictly', messages=prompt)
    message=response.last
    return message


def user_input():
    input= st.text_input("Enter you Prompt here:")
    return input


if 'generate' not in st.session_state:
    st.session_state['generate']=[]
if 'past' not in st.session_state:
    st.session_state['past']=[]

user_text=user_input()
if user_text:
    output=response_api(user_text)
    st.session_state.generate.append(output)
    st.session_state.past.append(user_text)

    
if st.session_state['generate']:
    for i in range(len(st.session_state['generate'])-1,-1,-1):
        message(st.session_state["past"][i],is_user=True,key=str(i)+'_user')
        message(st.session_state['generate'][i],key=str(i))
