# PIAIC SUNDAY CLASS 07 Q2 Bact 61, Karachi Morning :clipboard:

**Instructor**: [Wajahat Hussain](#) 👨‍🏫  

## Table of Contents

1. [Overview](#overview-rocket) 🚀 
2. [Latency](#latency-hourglass_flowing_sand) ⏳ 
3. [Fine-tuning Overview](#fine-tuning-overview-hammer_and_wrench) 🛠 
4. [Detailed Fine-tuning Process](#detailed-fine-tuning-process-mag) 
5. [Understanding Epochs](#understanding-epochs-calendar) 🗓  
6. [Fine-tuning Through OpenAI](#fine-tuning-through-openai-globe_with_meridians) 🌐 
7. [Conclusion](#conclusion-checkered_flag) 🚩 

## Overview :rocket:

These notes recap our discussion on:
- **Fine-tuning Gemini with Google AI (Vertex AI)**
- **Understanding Latency**
- **Importance of Input and Output Patterns**
- **Epochs and the full fine-tuning process for Generative AI models**
- **Fine-tuning with OpenAI**

## Latency :hourglass_flowing_sand:

- **Definition**: Latency is how long it takes from sending a request to receiving a response from the model.  
- **Why Low Latency Is Important**:  
  - Improves user experience in interactive applications.  
  - Essential for real-time or near-real-time systems.

## Fine-tuning Overview :hammer_and_wrench:

### What Is Fine-tuning?
Fine-tuning is the process of taking a pre-trained large language model (foundation model) and further training it on a smaller, task-specific dataset. This helps the model **specialize** in tasks such as:
- :clipboard: Question Answering  
- :page_facing_up: Summarization  
- :mag_right: Classification  
- :hospital: Domain-specific tasks (e.g., legal, medical)

### Approaches to Fine-tuning
1. **Full Fine-tuning**  
   - Updates *all* parameters of the model.  
   - Expensive in terms of compute.  
   - Less common for very large models.

2. **Parameter-Efficient Fine-tuning (PEFT)**  
   - Freezes most parameters and updates only a small set.  
   - Much faster and more resource-friendly.  
   - **LoRA** (Low-Rank Adaptation) is a popular PEFT method.

### When to Use Fine-tuning
- **Domain Expertise**: E.g., specialized legal or medical tasks.  
- **Format Customization**: Produce outputs with a specific structure or style.  
- **Task Optimization**: For narrow tasks (like advanced summarization).  
- **Behavior Control**: Control model’s style (concise vs. detailed, etc.).

> **Note**: Because fine-tuning changes internal weights, it’s not ideal for real-time data (e.g., weather). In such cases, consider **RAG (Retrieval-Augmented Generation)** or **function calling** to fetch fresh info.

## Detailed Fine-tuning Process :mag:

Below is an example workflow using **Google Vertex AI** (Gemini models).

### 1. Data Preparation
1. **Annotation/Labeling**  
   - Collect input–output pairs for your task.  
2. **Cleaning & Deduplication**  
   - Remove duplicates.  
   - Standardize capitalization, whitespace, punctuation.  
3. **Formatting**  
   - For Gemini, each training example is a single line in a `.jsonl` file.  
   ```json
   {
     "contents": [
       {
         "role": "user",
         "parts": [
           { "text": "Here goes the question and context" }
         ]
       },
       {
         "role": "model",
         "parts": [
           { "text": "Here goes the model response" }
         ]
       }
     ]
   }
   ```

### 2. Model Selection
- **Gemini 1.5 Pro**: High accuracy, better reasoning.  
- **Gemini 1.5 Flash**: Lower latency, more cost-effective.  
> **Tip**: Start with Flash to quickly test data. If you need higher accuracy, move to Pro.

### 3. Establish a Baseline
- Evaluate the **pre-trained model** (foundation) on some data.  
- Use metrics like **Exact Match (EM)** and **F1 Score** to see how well it does before fine-tuning.

### 4. Launch the Fine-tuning Job
Using the Vertex AI SDK in Python:
```python
from vertexai.preview.tuning import sft

tuned_model_display_name = "fine-tuning-gemini-flash-qa-v01"

sft_tuning_job = sft.train(
    source_model="gemini-1.5-flash-002",
    train_dataset=f"{BUCKET_URI}/squad_train.jsonl",
    validation_dataset=f"{BUCKET_URI}/squad_validation.jsonl",
    tuned_model_display_name=tuned_model_display_name,
)
```
- **source_model**: Which base Gemini model to fine-tune.  
- **train_dataset**: Path to your training data (JSONL).  
- **validation_dataset** (optional): Helps monitor overfitting.  
- **tuned_model_display_name**: Name for the fine-tuned model.

### 5. Monitoring
- **Training Loss**: Should decrease.  
- **Validation Loss**: Should also decrease and stay close to training loss to avoid overfitting.

### 6. Evaluate the Fine-tuned Model
- Test on your **validation** or **test set**.  
- Compare **EM, F1,** or other task-specific metrics to the baseline.

### 7. Using the Fine-tuned Model
```python
tuned_model_endpoint_name = sft_tuning_job.tuned_model_endpoint_name
tuned_genai_model = GenerativeModel(tuned_model_endpoint_name)

prompt = "Your question or text prompt here..."
response = tuned_genai_model.generate_content(contents=prompt)

print(response)
```

## Understanding Epochs :calendar:

- **Epoch**: One full pass through the training dataset.  
- **Too Few vs. Too Many**:  
  - Too few → model might not learn enough (underfitting).  
  - Too many → risk of overfitting.  
- **Practice**: Large language models often need only **1–3 epochs** because they are already well-trained.

## Fine-tuning Through OpenAI :globe_with_meridians:

The overall process with OpenAI is similar: prepare data → train → evaluate → deploy.

### 1. Data Preparation
- Format as `.jsonl` with lines like:
  ```json
  {"prompt": "<instructions>", "completion": "<desired response>"}
  ```
- Check OpenAI’s token limits and guidelines.

### 2. Using the OpenAI API
- **Install/Update**:
  ```bash
  pip install --upgrade openai
  ```
- **Upload Training File**:
  ```bash
  openai tools fine_tunes.prepare_data -f train_data.jsonl
  openai api files.upload -f train_data_prepared.jsonl
  ```
- **Create a Fine-tune**:
  ```bash
  openai api fine_tunes.create -t <FILE_ID> -m <BASE_MODEL>
  ```
- **Monitor**:
  ```bash
  openai api fine_tunes.follow -i <FINE_TUNE_JOB_ID>
  ```
- **Use the Fine-tuned Model**:
  ```python
  import openai

  openai.api_key = "YOUR_API_KEY"
  response = openai.Completion.create(
      model="<YOUR_FINE_TUNED_MODEL>",
      prompt="Your prompt..."
  )
  print(response.choices[0].text)
  ```

## Conclusion :checkered_flag:

**Fine-tuning** is a powerful way to adapt big models like Gemini or GPT to your specific tasks. Here’s the general process once more:

1. :sparkles: **Prompt Engineering & Few-Shot Learning**: Always try these first.  
2. :books: **Consider RAG** if data changes frequently.  
3. :hammer: **Fine-tune** for tasks requiring custom responses or deeper domain knowledge.  
4. :chart_with_upwards_trend: **Evaluate** using relevant metrics (e.g., EM, F1) to confirm improvements.  
5. :trophy: **Deploy** your fine-tuned model for better, more personalized performance.


> **Happy Fine-tuning!** If you find any part confusing, experiment with small datasets and watch your metrics closely. Remember, data quality is everything, and your choice of approach—PEFT, LoRA, or full fine-tuning—depends on your computational resources and task requirements.


