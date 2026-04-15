# 🚀 E-Commerce Customer Intent Detection (Fine-Tuned DistilBERT)

A lightweight NLP system that classifies customer queries into intents, reducing unnecessary LLM usage and lowering operational cost.

This project focuses on building a **cost-efficient AI pipeline** by introducing an **Intent Classification layer** before sending user queries to Large Language Models (LLMs).

Instead of forwarding every query to an LLM (which increases cost), this system:
- Classifies user intent  
- Filters simple queries  
- Routes only complex or Out-Of-Scope queries to the LLM  

---

## 💡 Problem Statement

Most AI-powered chat systems send **every user query** to LLMs.

❌ High token usage  
❌ Increased cost  
❌ Unnecessary processing  

---

## ✅ Solution

Fine-tuned a **DistilBERT model** for **Customer Intent Detection** to act as an intelligent filter.

---

## 🧠 Key Features

- 🎯 Intent Classification for customer queries  
- 💬 Handles real-world chat patterns (WhatsApp-style input)  
- 🛑 Out-Of-Scope (OOS) Detection  
- ⚡ Lightweight and fast inference  
- 💻 Easy-to-use inference script  

---

## 📊 Dataset

The model was trained on a **combination of datasets**:

- Hugging Face datasets  
- UCI Machine Learning Repository datasets  
- Curated GitHub datasets  
- Synthetic data generated using ChatGPT  

👉 Dataset Link:  
https://huggingface.co/datasets/monish-sd-7/E-Commerce-Customer-Intent-Detection-Dataset  

---

## 🤖 Model

Fine-tuned **DistilBERT** for multi-class intent classification.

👉 Model Link:  
https://huggingface.co/monish-sd-7/E-Commerce-Customer-Intent-Detection-Model-Finetuned  

---

## 🧩 Supported Intents (Examples)

- Order Tracking  
- Cancellation  
- Returns  
- Product Inquiry  
- Payment Issues  
- Out-Of-Scope (OOS)  

---

## 💬 Real-World Input Handling

The model is trained to handle:

- Misspellings  
- Short forms  
- Informal language  
- Noisy user inputs  

### Examples:

- "whr is my ordrr" → Order Tracking  
- "cncl my order" → Cancellation  
- "hey do u sell laptops?" → OOS  

---

## 🛠️ Installation

### 🚀 Setup & Run Guide

### Step 1: Clone the Repository
```
git clone https://github.com/Monishsasi/Finetuned-Models.git
```

### Step 2: Navigate to Project Directory
```
cd E-Commerce-Customer-Intent-Detection-Model
```

### Step 3: Create Virtual Environment
```
python -m venv .venv
```

### Step 4: Activate Virtual Environment (Windows)
```
.venv\Scripts\activate
# For macOS/Linux use:
# source .venv/bin/activate
```

### Step 5: Install Dependencies
```
pip install -r requirements.txt
```

### Step 6: Run Inference Script

```
python inference.py
```