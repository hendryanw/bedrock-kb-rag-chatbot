from langchain.memory import ConversationBufferWindowMemory
from langchain.chains import ConversationalRetrievalChain

from langchain.llms.bedrock import Bedrock
from langchain.retrievers import AmazonKnowledgeBasesRetriever
from langchain.chains import RetrievalQA

retriever = AmazonKnowledgeBasesRetriever(
    knowledge_base_id = "", #configure your knowledge base ID here
    retrieval_config = {
        "vectorSearchConfiguration": {
            "numberOfResults": 5 #return 5 results from knowledge base
        }
    }
)

model_kwargs = { #Claude
    "max_tokens_to_sample": 3000, 
    "temperature": 0, 
    "top_k": 10
}
llm = Bedrock(
    model_id="anthropic.claude-instant-v1",
    model_kwargs=model_kwargs)

def get_memory(): #create memory for this chat session
    memory = ConversationBufferWindowMemory(
        memory_key = "chat_history", 
        output_key = 'answer',
        k = 10, #number of messages to store in buffer
        return_messages = True) #maintains a history of previous messages
    return memory
    
def get_rag_chat_response(input_text, memory): #chat client function
    conversation_with_retrieval = ConversationalRetrievalChain.from_llm(
        llm, 
        retriever, 
        output_key= 'answer',
        memory = memory,
        return_source_documents = True)
    
    chat_response = conversation_with_retrieval({"question": input_text}) 
    return chat_response