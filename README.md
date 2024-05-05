# PetCare AI Chatbot using Langchain, llama3, and Flask

This project implements an AI Chatbot that can answer queries based on PDF files from a dataset. The chatbot utilizes Langchain, Ollama, and Flask frameworks, along with the RAG (Retrieval Augmentation Generation) technique for generating answers.

<p><img height="300" width="1000" src="https://github.com/rajveersinghcse/rajveersinghcse/blob/master/img/PetCare-AI-Chatbot.gif" alt="gif"></p>

## Core Concept

The core concept behind this AI Chatbot lies in leveraging advanced natural language processing (NLP) techniques to provide accurate and context-aware responses to user queries. Here's a brief overview of the key components:

- **Langchain**: Langchain is a powerful framework that integrates various NLP tools and libraries, making it easier to build complex conversational systems. In this project, Langchain is used for document loading, text splitting, embeddings, and more.

- **Ollama**: Ollama is an advanced language model (LLM) that enables the chatbot to understand and generate human-like responses. By incorporating Ollama into the conversational chain, the chatbot gains a deeper understanding of user queries and context.

- **Flask**: Flask is a lightweight web framework used for building web applications, including APIs and web-based interfaces. In this project, Flask serves as the backend server for hosting the chatbot and handling user interactions.

- **RAG (Retrieval Augmentation Generation)**: RAG is a methodology that combines information retrieval (retrieval) with language generation (generation) to produce high-quality responses. By retrieving relevant information from PDF documents using Langchain's retrieval capabilities and augmenting it with Ollama's generation, the chatbot can provide accurate and informative answers.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/rajveersinghcse/PetCare-AI-Chatbot.git
   cd your_repository
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Ensure you have the necessary PDF files in the `data/` directory. Supported PDF files include:
   - `dog_care_encyclopedia.pdf`
   - `Veterinary_Clinical_Pathology.pdf`
   - You can add more pdf files. But it will take a lot of computational resources.

2. You have to run your llama model from Ollama.
   ```bash
   Ollama serve
   ```

4. Run the Flask application:
   ```bash
   python app.py
   ```

5. Access the chatbot interface by navigating to `http://localhost:5000` in your web browser.

## Project Structure

- `app.py`: Flask application for running the chatbot server.
- `templates/index.html`: HTML template for the chatbot interface.
- `data/`: Directory containing PDF files used for answering queries.
- `requirements.txt`: List of Python dependencies.

## Configuration

- `loader`: Loads PDF documents from the `data/` directory using Langchain's `DirectoryLoader`.
- `text_splitter`: Splits PDF documents into chunks for processing.
- `embeddings`: Utilizes Hugging Face embeddings for text representation.
- `vector_store`: Stores text chunks using FAISS for efficient retrieval.
- `llm`: Implements Ollama's Large Language Model for conversational context.
- `memory`: Manages conversation history for context-aware responses.
- `chain`: Constructs the Conversational Retrieval Chain using the configured components.

## Contributing

Contributions to enhance the chatbot's functionality, add new features, or improve documentation are welcome. Please fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
