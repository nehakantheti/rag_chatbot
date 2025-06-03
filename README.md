## **RAG Chatbot**
A Retrieval-Augmented Generation (RAG) chatbot that leverages large language models (LLMs) to provide context-aware responses by retrieving relevant information from a custom knowledge base.

**Features**

- **Retrieval-Augmented Generation:** Combines information retrieval with generative AI to produce accurate and contextually relevant answers.

- **Custom Knowledge Base:** Ingest and index your documents (e.g., PDFs, text files) to tailor the chatbot's responses to your specific data.

- **Interactive Chat Interface:** Engage in dynamic conversations with the chatbot through a user-friendly interface.

- **Modular Architecture:** Easily extend or replace components like the vector store, embedding model, or frontend interface.



What is RAG?
Retrieval-Augmented Generation (RAG) enhances the capabilities of LLMs by supplementing them with external knowledge sources. Instead of relying solely on pre-trained data, RAG retrieves pertinent information from a knowledge base and feeds it into the LLM to generate informed responses.


**Tech Stack:**
- **Backend:** Python, FastAPI
- **Frontend:** Streamlit
- **Embeddings:** Google GenAI
- **Vector Store:** ChromaDB
- **Document Processing:** LangChain, Unstructured

- Creating a Virtual Environment is recommended
```bash
  python -m venv venv
  source venv/bin/activate  # On Windows: venv\Scripts\activate
```
- Install Dependencies using
```bash
  pip install -r requirements.txt
```

- Set Up Environment Variables
Create a .env file in the root directory and add your API keys:
```env
GOOGLE_API_KEY=your_google_api_key
```
**Run the Application**
**Backend API:**
```bash
uvicorn app.main:app --reload
```

**Frontend Interface:**
```bash
streamlit run frontend/app.py
```

**Usage**

- Ingest Documents

- Place your documents (e.g., PDFs, text files) into the data/ directory. The application will process and index these documents to build the knowledge base.

- Access the Streamlit interface at http://localhost:8501 to start chatting. The chatbot will retrieve relevant information from your documents to answer queries.

- Interact with the Chatbot

**Example:**

_**User:**_ "What is the refund policy mentioned in the company handbook?"

_**Chatbot:**_ "According to the company handbook, the refund policy states that customers can request a refund within 30 days of purchase, provided they have a valid receipt."
