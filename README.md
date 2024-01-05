# RAG Chatbot Powered by Amazon Bedrock Knowledge Base

## Prerequisites
1. Setup [Bedrock knowledge base](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html)
2. Setup [AWS CLI](https://aws.amazon.com/cli/) profile with sufficient permissions

## Running the Application

1. Set your Bedrock knowledge base using comma-delimited string in `BEDROCK_KB_IDS` environment variable. This will be displayed as knowledge base options when you interact with the chatbot. The first 10 characters of each value must be the ID of the knowledge base.
    ```
    export BEDROCK_KB_IDS="ABC1D2EFGH - ABC Knowledge Base,OPQRSTUVW1 - Others info"
    ```
2. Install requirements `pip install -r requirements.txt`
3. Run the Streamlit application using
    ```
    streamlit run app/app.py
    ```

> **Note:** You can deploy the application as container using the `Dockerfile` included in this repository.