# Updated imports
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain_community.llms import OpenAI
import tempfile
import os
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def process_pdf(file_contents):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
        temp_file.write(file_contents)
        temp_file_path = temp_file.name

    loader = PyPDFLoader(temp_file_path)
    pages = loader.load_and_split()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    texts = text_splitter.split_documents(pages)

    embeddings = OpenAIEmbeddings()
    vector_store = FAISS.from_documents(texts, embeddings)

    os.remove(temp_file_path)
    return vector_store

def get_answer(soru, sohbet_gecmisi):
    embeddings = OpenAIEmbeddings()
    vector_store = FAISS.load_local("vektor_deposu", embeddings, allow_dangerous_deserialization=True)

    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True
    )

    for giris, cikis in sohbet_gecmisi:
        memory.save_context({"input": giris}, {"output": cikis})

    logging.info(f"Question being asked: {soru}")
    logging.info(f"Chat history being used: {sohbet_gecmisi}")
    logging.info(f"Current Memory: {memory.load_memory_variables({})}")  # Log the memory contents

    qa = ConversationalRetrievalChain.from_llm(
        OpenAI(temperature=0),
        vector_store.as_retriever(),
        memory=memory
    )

    result = qa({"question": soru, "chat_history": sohbet_gecmisi})
    return result["answer"]