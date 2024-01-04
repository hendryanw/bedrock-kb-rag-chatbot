import streamlit as st 
import lib as glib
import os

bedrock_kb_ids = os.environ.get('BEDROCK_KB_IDS').split(',')

st.set_page_config(page_title="Virtual Assistant Powered by AWS Bedrock Knowledge Base")
st.title("Virtual Assistant Powered by AWS Bedrock Knowledge Base")

if 'memory' not in st.session_state:
    st.session_state.memory = glib.get_memory()

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

if 'select_kb_disabled' not in st.session_state:
    st.session_state.select_kb_disabled = False

bedrock_kb_id = st.selectbox('Select Bedrock Knowledge Base ID to query', bedrock_kb_ids, disabled=st.session_state.select_kb_disabled)

for message in st.session_state.chat_history:
    with st.chat_message(message["role"]): 
        st.markdown(message["text"]) 

input_text = st.chat_input("Chat with your bot here") 

if input_text: 
    if 'retriever' not in st.session_state:
        st.session_state.retriever = glib.get_retriever(bedrock_kb_id)
        st.session_state.select_kb_disabled = True

    with st.chat_message("user"):
        st.markdown(input_text)
    
    st.session_state.chat_history.append({"role":"user", "text":input_text})
    
    chat_response = glib.get_rag_chat_response(input_text=input_text, memory=st.session_state.memory, retriever=st.session_state.retriever)
    answer = chat_response['answer']
    with st.chat_message("assistant"):
        st.markdown(answer)
        with st.expander("See references"): #display the references
            url_count = 0
            for document in chat_response['source_documents']:
                url_count = url_count + 1
                metadata = document.metadata
                st.markdown('**[**' + f"**{url_count}**" + '**]**' + ' ' + f"**{metadata['location']['s3Location']['uri']}**" + '  \n' + document.page_content)
    
    st.session_state.chat_history.append({"role":"assistant", "text":answer})