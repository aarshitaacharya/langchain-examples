# LangChain Examples

A collection of small LangChain implementations exploring various features and capabilities of the framework.

## Contents

### 1. Chat Models & Prompt Templates
**`1.chat_model.ipynb`**
- Demonstrates LangChain's built-in chat models
- Shows usage of prompt templates for structured interactions
- Basic foundation for LLM integration

### 2. Hugging Face Integration
**`2.hugging_face.ipynb`**
- Connects to Hugging Face models
- Uses Microsoft Phi 3 Mini 4K Instruct model
- Compares single vs multiple question handling
- Performance comparison with Gemini

### 3. Chat Bot with Memory
**`3.chat_bot.ipynb`**
- Explores conversation memory in chatbots
- Demonstrates memory-less interactions
- Implements conversation history passing
- Uses LangGraph with MemorySaver for persistent memory
- Configures thread management for multi-user scenarios

### 4. Research Tool
**`4.research_tool.py`**
- Compares static vs dynamic prompting approaches
- Dynamic tool accepts three parameters:
  - Paper content
  - Input style
  - Desired length
- Generates context-aware summaries based on input parameters

### 5. PDF Document Processing
**`5.pdf_splitter.ipynb`**
- PDF text extraction using PyMuPDF
- Text chunking with RecursiveCharacterTextSplitter
- Chunk statistics (average, min, max sizes)
- Foundation for document-based RAG applications

📖 **Read more**: [My LLM Learning Journey - Day 4: Document Loaders and Text Splitters](https://medium.com/@aarshita08/my-llm-learning-journey-day-4-document-loaders-and-text-splitters-571da8e7fff9)

## Getting Started

Each notebook/script is self-contained and includes the necessary imports and setup instructions. Make sure to install required dependencies:

```bash
pip install langchain langchain-community langchain-huggingface pymupdf
```

## Purpose

These examples serve as practical learning materials for understanding LangChain's core concepts and building blocks for more complex AI applications.

## Notes

- Examples are kept simple for learning purposes
- Each implementation focuses on specific LangChain features
- Perfect starting point for beginners exploring LangChain capabilities