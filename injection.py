"""
in this we create a pipeline to get the document and
make it chuncks and store into the chroma db(vector database) 
by converting the chuncks into vector 

"""
##===============================================================================


import os
import fitz
import glob
import tiktoken
import numpy as np
from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import DirectoryLoader, TextLoader,PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter



#======================================================================================
knowledge_base_path="knowledge-base/**/*.pdf"##creating the knowledge base path
files = glob.glob(knowledge_base_path, recursive=True)##return the list of file path in the list structure 
print(f"Found {len(files)} files in the knowledge base")##tells how many files detected in the knowledge base
knowledge=""
for file in files:
    pdf=fitz.open(file)
    for page in pdf:
        knowledge +=page.get_text()
        knowledge +="/n/n"
print(f"total character in the knowledge {len(knowledge)}")
#==========================================================
##here i am using the gemini sdk to my embedding because my open ai competable does not provide the correct structure for the enbedding model 
"""import google.generativeai as genai
model = genai.GenerativeModel(model)
tokens = model.count_tokens(knowledge)

token_count = tokens.total_tokens
print(f"Total tokens for {model}: {token_count:,}")"""
#=================================================================
folders=glob.glob("Knowledge-base")
documents=[]
for folder in folders:
    doc_type=os.path.basename(folder)
    loader=DirectoryLoader(folder,glob="**/*.pdf",loader_cls=PyPDFLoader)
    folder_docs = loader.load()
    for doc in folder_docs:
        doc.metadata['doc_type']=doc_type
        documents.append(doc)
print(f"Loaded {len(documents)}documents")
#=============================================================
text_spliter=RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=200)
chunks=text_spliter.split_documents(documents)
print(f"Divided into  {len(chunks)} chunks")
#=============================================================
db_name="resume_thiru.db"
embeddings=HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
if os.path.exists(db_name):
    Chroma(persist_directory=db_name,embedding_function=embeddings).delete_collection()
vectorstore=Chroma.from_documents(documents=chunks,embedding=embeddings,persist_directory=db_name)
print(f"Vectorstore created with{vectorstore._collection.count()}documents")

