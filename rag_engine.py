from langchain_openai import ChatOpenAI
from langchain_chroma import Chroma
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_huggingface import HuggingFaceEmbeddings
import gradio as gr
from dotenv import load_dotenv
import os
DB_NAME="resume_thiru.db"
load_dotenv(override=True)
gemini_api=os.getenv("GEMINI_API")
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vectorstore = Chroma(persist_directory=DB_NAME, embedding_function=embeddings)
##CREATING THE MAIN CORE TWO OBJECT 
retriever = vectorstore.as_retriever()
MODEL="gemini-3.1-flash-lite"
llm = ChatOpenAI(temperature=0, model_name=MODEL,api_key=gemini_api,base_url="https://generativelanguage.googleapis.com/v1beta/openai/")
SYSTEM_PROMPT_TEMPLATE="""
        You are a Thirumaran's rag chat bot you provided with the content of the Thirumaran's resuma the user question about him you  want to answer only the correct answer with this provided context{context}
"""
def answer(user_question,history):
    docs=retriever.invoke(user_question)
    context="\n\n".join(doc.page_content for doc in docs)
    system_prompt=SYSTEM_PROMPT_TEMPLATE.format(context=context)
    response=llm.invoke([SystemMessage(content=system_prompt),HumanMessage(content=user_question)])
    return response.content
import gradio as gr

gr.ChatInterface(
    fn=answer,
    title="🤖 Thirumaran Resume AI Assistant",
    description="Ask anything about Thirumaran's skills, projects, and experience.",
    

    examples=[
        "What are Thirumaran's AI skills?",
        "What projects has he built?",
        "Does he know FastAPI?"
    ],
    chatbot=gr.Chatbot(height=500),
).launch(inbrowser=True)


