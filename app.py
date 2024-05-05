from langchain_community.llms import Ollama
from flask import Flask, render_template, request
from langchain_community.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader


# create a Flask app
app = Flask(__name__)

# Load the documents
loader = DirectoryLoader("./data/", glob="*.pdf", loader_cls=PyPDFLoader)
documents = loader.load()

# Split the documents into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
text_chunks = text_splitter.split_documents(documents)

# Creating the Embeddings and Vector Store
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={"device": "cuda:0"},
)

vector_store = FAISS.from_documents(text_chunks, embeddings)

# Load the model
llm = Ollama(model="llama3")

# load the memory
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# create the chain
chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    chain_type="stuff",
    retriever=vector_store.as_retriever(search_kwargs={"k": 2}),
    memory=memory,
)


# render the template
@app.route("/")
def index():
    return render_template("index.html")


# Posting the user query
@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.form["user_input"]
    result = chain({"question": user_input, "chat_history": []})
    return result["answer"]


if __name__ == "__main__":
    app.run(debug=True)
