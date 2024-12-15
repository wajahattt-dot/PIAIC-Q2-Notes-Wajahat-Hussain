## **PIAIC Q2 Batch 61 - Class 03 Notes (Karachi)** 📚

INSTRUCTOR: **Wajahat Hussain**
#### **Today’s Agenda:**
1. **Introduction to the Experimental Gemini 2.0 Flash Model** 🌟
2. **Review of APIs and GUIs** 🔗💻
3. **Understanding SDK vs. API** 🛠️ vs. 🔌
4. **Steps of Prompt Engineering for Chatbots** 🤖
5. **Using the Google Generative AI Python SDK in Google Colab** 🐍☁️
6. **Working with Gemini Models and Their Parameters (Tokens, Temperature)** 🧮🔥
7. **Using Stateless vs. Stateful Chat Modes** 💬🤔
8. **Example: Image Analysis Using the Gemini Model** 🖼️🔍
9. **Brief Overview of OpenAI API** 🌐
10. **Final Task: Complete the “Hello World” of Gemini** 👋🌍

#### **Repo Link:**  
[www.github.com/panaversity/learn-agentic-ai](https://www.github.com/panaversity/learn-agentic-ai)

#### **Codes Run in Class Today:**  
- [**PIAIC Class 03 Batch 61 Q2 Colab File**](https://github.com/wajahattt-dot/PIAIC-Q2-Notes-Wajahat-Hussain/blob/main/Class%2003%20Q2%20Batch%20%2061/PIAIC_Class_03_Q2_B61.ipynb) ☁️

### **1. Gemini 2.0 Flash (Experimental)** 🚀

**What is Gemini 2.0 Flash?**  
Gemini 2.0 Flash is an **experimental** version of Google’s **Gemini model**. It's available as a preview through the **Gemini Developer API** and **Google AI Studio**. 🌐✨

**Key Features:**
- **Multimodal Live API:** Supports **real-time vision** and **audio streaming** applications, plus **integration with tools**. 👁️🔊
- **Performance:** **Faster response time** than Gemini 1.5 Flash (better **time to first token**). ⚡️
- **Quality:** Outperforms Gemini 1.5 Pro in benchmarks 🏆.
- **Agentic Capabilities:** Better at **multimodal understanding** (images, audio), **coding tasks**, and **following complex instructions**. 💻💬
- **New Modalities:** Can **generate images** and has **text-to-speech** features. 🖼️🎙️

### **2. Review of APIs and GUIs** 🔌🖥️

- **API (Application Programming Interface):**
  - A **set of rules** that lets different software talk to each other. 🗣️💻
  - Allows **remote** access to a program's **functionalities** without storing the program itself.  
  - **Example:** Sending a request to **Gemini API** for a response. 🔄

- **GUI (Graphical User Interface):**
  - The **visual interface** (buttons, icons, windows) that users click to interact with software. 🖱️🎮
  - Allows **direct interaction** with the program on the frontend.

**Key Difference:**  
- **API** is the **backend communicator**; **GUI** is the **frontend interface** for user interaction. 🌐 vs. 🖼️

### **3. SDK vs. API** 🛠️ vs. 🔌

- **API (Application Programming Interface):**
  - **End points** that let you interact with a service or system remotely. 🌍
  - **No need to download** anything, just send **requests** online. 📨  
  - **Example:** Requesting data from Gemini’s API to generate responses.

- **SDK (Software Development Kit):**
  - A **toolbox** of tools, libraries, and documentation that helps you **build** software for a specific platform. 🧰⚙️
  - Usually requires **downloading** and **installing** on your system. 🖥️
  - **Example:** Google Generative AI Python SDK to make it easier to work with the Gemini API.

**Feature Comparison:**  

| Feature | **API** 🌐 | **SDK** 🛠️ |
|---------|-----------|------------|
| **Definition** | Set of rules for software communication | Collection of tools for development |
| **Access** | Remote (no download needed) | Requires download and installation |
| **Components** | Endpoints, methods, protocols | Libraries, documentation, tools, code samples |
| **Usage** | Interact with external services | Build apps with integrated tools |
| **Example** | Gemini API for generating text | Google Generative AI Python SDK |

### **4. Prompt Engineering Steps for Chatbots** 🤖💬

**Steps to create effective prompts:**
1. **Instruction:** Tell the model **what you want it to do**. ✍️
2. **Context:** Provide **necessary background information**. 📚
3. **Input Data:** Give the model the **data it needs** (text, image, etc.). 📊
4. **Output Format:** Specify how you want the response (list, JSON, or paragraph). 📝

### **5. Using the Google Generative AI Python SDK in Google Colab** 🐍☁️

- **Installation:**  
  ```bash
  !pip install -U -q "google-generativeai>=0.7.2"
  ```

- **Importing the SDK:**  
  ```python
  import google.generativeai as genai
  ```

- **Setup API Key:**  
  - Get your **API key** from **Google AI Studio** and configure it:  
  ```python
  genai.configure(api_key="YOUR_API_KEY")
  ```

### **6. Working with Gemini Models** 🌌

**Example: Using Gemini 1.5 Flash**

```python
model = genai.GenerativeModel('gemini-1.5-flash')
response = model.generate_content("Give me python code to sort a list")
print(response.text)
```

- This will generate **Python code** to sort a list. 🐍➡️📜

**Inspecting the Response:**
- `response.candidates`: Shows the **raw responses** from the model. 💬
- `response.usage_metadata.candidates_token_count`: Shows how many **tokens** were used. 🧮

### **7. Adding Images in Colab and Using Image Recognition** 🖼️🔍

1. **Loading an Image:**
   - Use `!wget` or `curl` to **fetch an image** from a URL and save it.  
   - Load it using **PIL (Python Imaging Library):**
   ```python
   from PIL import Image
   image = Image.open("image.jpg")
   image.show()
   ```

2. **Image Recognition with Gemini:**  
   - Pass the **image** to Gemini and ask it to **describe** or **identify** objects.  
   - The model can provide the response in **JSON** or any format you choose. 📊

### **8. Stateless vs. Stateful Chat** 💬🤔

- **Stateless Mode:**  
  - The model doesn’t remember past interactions. Each query is **independent**. ⚡️  
  - **Example:** Asking questions without context.

- **Stateful Mode:**  
  - The model remembers the **conversation history**, making interactions feel like a **continuous dialogue**. 📜💭  
  - **Example:** Chatting back-and-forth where the model recalls previous messages.

**Checking Chat History:**  
```python
print(chat.history)
```
### **9. Tokens and Temperature** 🧮🔥

- **Tokens:**  
  - Tokens are pieces of **text** counted by the model when generating responses. 🧾  
  - **Limiting tokens** can control the **length** and **cost** of responses. 💰

- **Temperature:**  
  - Controls how **creative** or **random** the model’s responses are:  
    - **Low temperature** = Predictable, focused answers. 🎯  
    - **High temperature** = Creative, varied answers. 🎨

### **10. OpenAI API (Not Used Now By Us)** 🌐

- We discussed that we **could** use the **OpenAI API** (like ChatGPT or GPT-4), but since it's **not free** at the moment, we’re focusing on **Gemini API** for our course. 💡

### **Final Task: Complete the “Hello World” of Gemini** 👋🌍

- **Task:** Write a **simple prompt** and **generate a response** using Gemini.  
  This will help you understand how to integrate the model and generate basic responses. 💬

### **Summary** 📝

1. **Gemini 2.0 Flash:** Advanced **multimodal** model with improved speed, performance, and new capabilities (image, audio, text-to-speech). 🚀
2. **API vs. GUI:** **API** is for backend communication; **GUI** is for frontend user interaction. 🌐 vs. 🖼️
3. **SDK vs. API:** **SDK** is a toolkit for building apps, while **API** is a service interface. 🛠️ vs. 🔌
4. **Prompt Engineering:** Provide clear instructions, context, input, and output format to get the best results. ✍️
5. **Google Generative AI SDK:** Install, set up the API and start generating responses using Gemini. 🐍
6. **Image Recognition:** Use Gemini to analyze images and generate descriptions. 🖼️
7. **Stateful vs. Stateless Chat:** Choose whether the model should remember past conversations. 💬
8. **Tokens and Temperature:** Manage response length and creativity. 🧮🔥
9. **OpenAI vs. Gemini:** We're using Gemini for this course since it’s free! 🎉
