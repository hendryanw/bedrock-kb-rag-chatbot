import streamlit as st #all streamlit commands will be available through the "st" alias
import lib as glib #reference to local lib script

st.set_page_config(page_title="Virtual Assistant Powered by AWS Bedrock Knowledge Base") #HTML title
st.title("Virtual Assistant Powered by AWS Bedrock Knowledge Base") #page title

if 'memory' not in st.session_state: #see if the memory hasn't been created yet
    st.session_state.memory = glib.get_memory() #initialize the memory

if 'chat_history' not in st.session_state: #see if the chat history hasn't been created yet
    st.session_state.chat_history = [] #initialize the chat history

#Re-render the chat history (Streamlit re-runs this script, so need this to preserve previous chat messages)
for message in st.session_state.chat_history: #loop through the chat history
    with st.chat_message(message["role"]): #renders a chat line for the given role, containing everything in the with block
        st.markdown(message["text"]) #display the chat content

input_text = st.chat_input("Chat with your bot here") #display a chat input box

if input_text: #run the code in this if block after the user submits a chat message
    
    with st.chat_message("user"): #display a user chat message
        st.markdown(input_text) #renders the user's latest message
    
    st.session_state.chat_history.append({"role":"user", "text":input_text}) #append the user's latest message to the chat history
    
    chat_response = glib.get_rag_chat_response(input_text=input_text, memory=st.session_state.memory) #call the model through the supporting library
    answer = chat_response['answer']
    with st.chat_message("assistant"): #display a bot chat message
        st.markdown(answer) #display bot's latest response
        with st.expander("See references"): #display the references
            url_count = 0
            for document in chat_response['source_documents']:
                url_count = url_count + 1
                metadata = document.metadata
                st.markdown('**[**' + f"**{url_count}**" + '**]**' + ' ' + f"**{metadata['location']['s3Location']['uri']}**" + '  \n' + document.page_content)
    
    st.session_state.chat_history.append({"role":"assistant", "text":answer}) #append the bot's latest message to the chat history
    
    