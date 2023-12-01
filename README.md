# RAG Chatbot Powered by Amazon Bedrock Knowledge Base

## Prerequisites
1. Setup [Bedrock knowledge base](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html)
2. Setup [AWS CLI](https://aws.amazon.com/cli/) profile with sufficient permissions

## Running the Application

1. Configure Bedrock knowledge base ID within `app/lib.py`
2. Install requirements `pip install -r requirements.txt`
3. Run the Streamlit application using
    ```
    streamlit run app/app.py
    ```

> **Note:** You can deploy the application as container using the `Dockerfile` included in this repository.