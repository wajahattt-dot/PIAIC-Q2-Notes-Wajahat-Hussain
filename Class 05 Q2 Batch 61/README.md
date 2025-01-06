# PIAIC Class 05 (Batch 61) Q2 Notes By Wajahat

>INSTRUCTOR: **Wajahat Hussain**
## 1. LLM Leaderboards 🚀

**LLM** stands for **Large Language Model**. An LLM leaderboard is a place (often a website or research portal) where different models are ranked based on performance in tasks like question answering, summarization, etc. These leaderboards help researchers pick the best models for specific tasks.

---

## 2. Retrieval-Augmented Generation (RAG) 📚

**RAG** is a framework that uses external data (e.g., from a vector database) to help generate more accurate and context-rich answers.  
It works like this:

1. **Query**: You ask a question.  
2. **Vector Database**: The query is turned into a numerical embedding. The database finds the most relevant pieces of information.  
3. **Retrieval**: The relevant info is retrieved from the database.  
4. **LLM Generation**: The retrieved info + your query go into the language model, which then generates an answer.

```
        ┌─────────────────┐   
        │   (Your Query)  │
        └─────────────────┘
                   ↓
            [Vector Database]
                   ↓
        ┌──────────────────┐   
        │       RAG        │
        └──────────────────┘
                   ↓
       ┌──────────────────┐   
       │       LLM        │
       └──────────────────┘
                   ↓
        ┌─────────────────┐   
        │    (Output)     │
        └─────────────────┘
```


## 3. Vector Databases (e.g., Pinecone) 💾

A **vector database** is specialized to store and query **embeddings** (vectors). These embeddings capture the meaning of words, sentences, or images. The database also stores **metadata** (like URLs, labels, categories) for better filtering and retrieval.

- **Example**: [Pinecone](https://www.pinecone.io/)  
- **Visualization Tool**: [TensorFlow Projector](https://projector.tensorflow.org/) (a tool to visualize embeddings in 2D or 3D)

### How Vector Databases Integrate with RAG

1. **Embedding**: Convert a user’s query into a vector.  
2. **Search**: Look up similar vectors in the database.  
3. **Retrieve**: Pull out the top relevant documents or data.  
4. **Generate**: Supply the data to the LLM to produce a final answer.


## 4. Tokenization and Word Embeddings ✏️

1. **Tokenization**: Splitting text into smaller units called **tokens** (words, subwords, or characters).  
2. **Word Embeddings**: Numerical vector representations of words that capture their meaning. Words with similar meanings end up close to each other in the vector space.  
3. **Corpus**: A collection of text. In NLP, we often store each unique word/token in a vocabulary list derived from the corpus.


## 5. Autoencoders 🔄

An **autoencoder** is a type of neural network that learns to compress data into a smaller representation and then reconstruct it. It has two parts:

- **Encoder**: Compresses the input (e.g., an image) into a **latent vector**.  
- **Decoder**: Reconstructs the original data from the latent vector.  

Autoencoders are useful for dimensionality reduction, feature extraction, and denoising.

## 6. Different Systems in RAG 🔍

1. **Retrieval & Document**: Fetch relevant documents to enhance generated answers.  
2. **Semantic Similarity**: Focus on finding the most meaningfully similar pieces of text.  
3. **Classification**: Categorize content (e.g., spam vs. not spam).  
4. **Clustering**: Group similar items or documents based on their embeddings.


## 7. Face Detection and Embedding Practical (LangChain, RAG, Google Gemini) 🤖

### 7.1 RAG Flow for Face Tasks

1. **Face Embedding**: Convert faces to vector form.  
2. **Storage**: Put these embeddings into a vector database.  
3. **Query**: On a new image, generate its embedding and compare with existing ones.  
4. **Augment**: Use RAG to retrieve any extra info from the database, then pass it to an LLM to generate richer answers.

### 7.2 Example Code Snippet (Face Detection & Embedding)

```python
# Install packages first if needed:
# pip install face_recognition opencv-python

import cv2
import face_recognition
import numpy as np

# 1. Load an image (use a valid image path)
image_path = "person1.jpg"
image = face_recognition.load_image_file(image_path)

# 2. Detect face locations in the image
face_locations = face_recognition.face_locations(image)

# 3. Generate face embeddings (128-d vector by default)
face_embeddings = face_recognition.face_encodings(image, face_locations)

# 4. Print out embedding vectors
for i, embedding in enumerate(face_embeddings):
    print(f"Face {i+1} Embedding Vector: {embedding}")

# 5. Compare with a second image
known_face_embedding = face_embeddings[0]  # assume one face in first image

unknown_image = face_recognition.load_image_file("person2.jpg")
unknown_face_locations = face_recognition.face_locations(unknown_image)
unknown_face_embeddings = face_recognition.face_encodings(unknown_image, unknown_face_locations)

if len(unknown_face_embeddings) > 0:
    result = face_recognition.compare_faces([known_face_embedding], unknown_face_embeddings[0])
    if result[0]:
        print("It's a match! ✔️")
    else:
        print("No match found. ❌")
```

### 7.3 Integrating LangChain, RAG, and Google Gemini

- **LangChain**: Helps build a “chain” that retrieves embeddings from a vector DB, then uses an LLM to analyze or answer.  
- **RAG**: The system retrieves relevant embeddings/info and feeds them to the model for context.  
- **Google Gemini**: Google’s advanced upcoming LLM—can be integrated similarly to GPT, sending queries and receiving generated text.

## 8. Additional Concepts for Better Understanding 💡

1. **Distance Metrics**: Cosine similarity, Euclidean distance, etc., measure how “close” embeddings are.  
2. **Indexing**: Vector databases often create special indexes (like ANN indexes) to speed up searches.  
3. **Prompt Engineering**: Crafting the right prompt so the LLM effectively uses retrieved info.  
4. **Fine-tuning vs. In-context Learning**: With RAG, you often don’t need to fully re-train your model; you just provide extra context at runtime.


## Final Wrap-Up 🎉

- **LLM Leaderboards** help rank large language models.  
- **RAG** improves answers by retrieving external context from vector databases.  
- **Vector Databases** (e.g., Pinecone) store embeddings and metadata.  
- **Tokenization & Embeddings** transform text into numerical form for ML.  
- **Autoencoders** compress and reconstruct data, useful for dimensionality reduction.  
- **RAG Systems** use different techniques like retrieval, semantic similarity, classification, and clustering.  
- **Face Detection & Embedding** can integrate with RAG + LLMs to identify faces and deliver richer insights.

---
