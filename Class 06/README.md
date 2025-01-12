# PIAIC Sunday Class 06 (Batch 61 Q2 - Karachi Morning) 🚀
**Instructor**: Wajahat Hussain

## Overview ✏️
This document summarizes our discussion about **CAG (Cache-Augmented Generation)**, **RAG (Retrieval-Augmented Generation)**, and **Tool/Function Calling**. It also covers advantages, disadvantages, and limitations of each approach, plus some examples of how function calling works in Python and Google GenAI.



## Projects 1 and 2 ⚙️
1. **“Hello World” of LangChain**  
   - A simple project to get started with LangChain by creating a minimal “Hello World” application.

2. **RAG System using Pinecone and LangChain**  
   - A system utilizing **Retrieval-Augmented Generation** with Pinecone (vector database) and LangChain.  
   - The goal is to store information in vector form and retrieve relevant data on the fly.


## CAG (Cache-Augmented Generation) 💾

### What is CAG?
- **Cache-Augmented Generation** uses a **cache**—a type of fast memory—to provide quick context or suggestions to a Large Language Model (LLM).  
- Instead of reaching out to an external database, the LLM can look up relevant responses in the cache, reducing **latency**.

### Why Use a Cache?
- **Speed** ⚡: Caches have very fast read and write speeds.  
- **Reduced Latency** ⏱️: By storing relevant responses, the LLM can skip repeating queries to external sources.


## RAG (Retrieval-Augmented Generation) 📚

### What is RAG?
- **Retrieval-Augmented Generation** relies on a vector database (e.g., Pinecone) to fetch the most relevant information in real-time.  
- Embeddings are used to search for context, enabling the LLM to find and use the correct data quickly.

### Benefits of RAG ✅
1. **Higher Accuracy**: Fetches factual context, reducing guesswork.  
2. **Scalability**: Handles large or frequently changing datasets effectively.

### Drawbacks of RAG ❌
- **Higher Latency**: Involves external database lookups.  
- **Complex Setup**: Requires additional components such as vector databases and embeddings.


## CAG vs. RAG ⚖️

| Feature                  | RAG (Retrieval-Augmented Generation)    | CAG (Cache-Augmented Generation)  |
|--------------------------|------------------------------------------|------------------------------------|
| **Data Retrieval**       | Real-time retrieval from a database     | Preloaded context in a cache       |
| **Latency**              | Higher, due to external fetch           | Lower, due to memory-based lookup  |
| **Scalability**          | Good for large, dynamic data            | Good for static datasets           |
| **Complexity**           | Higher (requires external DB & setup)   | Lower (no external retrieval)      |

### Key Points
- **RAG** is more flexible and accurate for evolving data but can be slower.  
- **CAG** is faster for repeated queries on static or stable data.



## Latency 🕒
- **Latency** refers to the time from when the LLM is prompted until it provides a response.  
- In RAG, latency is higher because of database lookups. In CAG, latency is generally lower because it uses a cache.



## Tool (Function) Calling 🔧

### What is Tool Calling?
- The LLM delegates specialized tasks or queries to a **function** you define.  
- This could be a simple Python function for math operations, color conversions, database lookups, etc.

### Example in Python 🐍

```python
def convert_rgb_to_hex(r, g, b):
    """Converts RGB color values to a Hex color code."""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def convert_hex_to_rgb(hex_code):
    """Converts a Hex color code to RGB color values."""
    hex_code = hex_code.strip('#')
    r = int(hex_code[0:2], 16)
    g = int(hex_code[2:4], 16)
    b = int(hex_code[4:6], 16)
    return (r, g, b)

user_input = "Please change the light color to #FF5733"
rgb_values = convert_hex_to_rgb("#FF5733")
print(f"Change the lights to RGB {rgb_values}")
# Output: "Change the lights to RGB (255, 87, 51)"
```

### Tool Calling vs. RAG 🤔
- **Tool Calling**: The LLM calls specific functions for tasks (e.g., color conversion), not necessarily retrieving large text data.  
- **RAG**: Focused on finding relevant text-based context in a database to include in responses.


## Google GenAI Function Calling 🌐

### Basic Steps
1. **Model Setup**  
2. **Helper Functions** for setting `function_calling_config` in tool calling  
3. **Modes**:
   - **NONE**: Text-only mode (no function calling)  
   - **AUTO**: Automatic function calling if needed  
   - **ANY**: Permissive function-calling mode (the model decides when to call functions)

### Example Scenario (Light Control) 💡
1. User says, “Set bedroom light to a relaxing color.”  
2. The LLM calls `change_light_color()` to actually change the light’s color.  
3. The function is executed, and the light changes in real life.


## Advantages, Disadvantages & Limitations ⚠️

### Advantages
- **Tool Calling**  
  - Extends LLM functionality with precise functions (e.g., calculations, APIs).  
  - Ensures accuracy if specialized tasks are needed.

- **RAG**  
  - Enhances factual correctness by retrieving data instead of relying on guesses.  
  - Scales well for large datasets.

- **CAG**  
  - Quick responses from in-memory data.  
  - Simpler setup than RAG.

### Disadvantages / Limitations
- **Tool Calling**  
  - Depends on well-defined functions.  
  - If the function is limited or buggy, performance suffers.

- **RAG**  
  - Complex to set up (embedding generation, vector DB).  
  - Higher latency from external lookups.

- **CAG**  
  - Limited to pre-cached data.  
  - Not suitable for frequently changing information unless you update the cache often.



## Final Summary 🌟
1. **CAG vs. RAG**: Use CAG for static data and fast lookup; use RAG for large, evolving data.  
2. **Latency**: RAG may have higher latency; CAG is quicker.  
3. **Tool Calling**: Extends the LLM’s capabilities by offloading certain tasks to specialized functions.  
4. **Google GenAI Function Calling**: Automates the decision to call functions, bridging natural language requests to real-world actions.



**Instructor**: Wajahat Hussain

*Feel free to contribute additional examples, corrections, or notes via pull requests.*
