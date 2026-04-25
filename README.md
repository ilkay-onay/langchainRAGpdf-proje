# langchainRAGpdf-proje

This project implements a robust PDF Question Answering system leveraging the power of Langchain and a Retrieval-Augmented Generation (RAG) approach. It allows users to upload PDF documents and then query them in natural language, receiving contextually relevant answers.

## Overview

The `langchainRAGpdf-proje` is designed to provide an intelligent interface for interacting with PDF documents. It addresses the common challenge of extracting specific information from large or complex PDF files. By employing a RAG architecture, the system first processes the PDF content to create a searchable vector store. When a user asks a question, the system retrieves the most relevant text chunks from this store and then uses a Large Language Model (LLM) to generate a concise and accurate answer based on the retrieved context and the conversation history. This ensures that the answers are not only informative but also maintain conversational coherence.

The project is structured into two main components: a backend API built with FastAPI for handling PDF processing and query responses, and a frontend interface built with Streamlit for user interaction.

## Features

*   **PDF Upload and Processing:** Securely upload PDF documents for analysis. The system extracts text, splits it into manageable chunks, generates embeddings, and stores them in a FAISS vector database.
*   **Contextual Question Answering:** Ask natural language questions about the uploaded PDF content.
*   **Retrieval-Augmented Generation (RAG):** Utilizes Langchain's RAG capabilities to retrieve relevant document segments and feed them to an LLM for answer generation.
*   **Conversational Memory:** Maintains a history of the conversation to provide contextually aware responses and follow-up questions.
*   **Web-based Interface:** A user-friendly Streamlit application for easy interaction.
*   **API Backend:** A FastAPI backend provides a robust API for PDF handling and querying.
*   **OpenAI Integration:** Leverages OpenAI's embedding models and LLMs for advanced natural language processing.

## Project Structure

```
├── LICENSE
└── backend/
    ├── main.py
    └── utils.py
└── frontend/
    └── app.py
```

*   **`LICENSE`**: Contains the GNU General Public License v3.0.
*   **`backend/`**:
    *   **`main.py`**: The main FastAPI application file, handling API endpoints for PDF upload and chat.
    *   **`utils.py`**: Contains utility functions for PDF processing, vector store creation, and answer generation using Langchain.
*   **`frontend/`**:
    *   **`app.py`**: The Streamlit application file, providing the user interface for uploading PDFs and interacting with the chat assistant.

## Getting Started

To run this project, you will need to have Python installed and set up with the necessary dependencies.

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd langchainRAGpdf-proje
    ```

2.  **Install backend dependencies:**
    Navigate to the `backend` directory and install the required Python packages. You will need to set your OpenAI API key as an environment variable.
    ```bash
    cd backend
    pip install -r requirements.txt # Assuming a requirements.txt exists, otherwise install manually
    export OPENAI_API_KEY='your-openai-api-key'
    ```
    *Note: The provided code snippets do not explicitly include a `requirements.txt`. You will need to install the dependencies manually based on the imports in `backend/main.py` and `backend/utils.py`. Key dependencies include `fastapi`, `uvicorn`, `langchain-community`, `langchain`, `pydantic`, `streamlit`, and `requests`.*

3.  **Run the backend server:**
    From the `backend` directory, start the FastAPI application.
    ```bash
    uvicorn main:app --reload
    ```
    This will start the backend server, typically on `http://127.0.0.1:8000`.

4.  **Install frontend dependencies and run the frontend application:**
    Navigate to the `frontend` directory and install the required Python packages.
    ```bash
    cd ../frontend
    pip install -r requirements.txt # Assuming a requirements.txt exists, otherwise install manually
    ```
    Then, run the Streamlit application:
    ```bash
    streamlit run app.py
    ```
    This will launch the Streamlit interface in your web browser, typically at `http://localhost:8501`.

5.  **Usage:**
    *   Use the "PDF Yükle" button in the Streamlit app to upload your PDF document.
    *   Once the PDF is processed, you can start asking questions in the chat input field.

## License

This project is licensed under the **GNU General Public License v3.0**. See the `LICENSE` file for more details.