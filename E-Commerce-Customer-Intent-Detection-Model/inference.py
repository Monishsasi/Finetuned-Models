
############################
## Run this code in colab to access the model
############################


from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load once (global)
model_name = "monish-sd-7/E-Commerce-Customer-Intent-Detection-Model-Finetuned"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)
model.eval()

## Function to predict the intent
def get_intent(text: str) -> str:
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    
    with torch.no_grad():
        outputs = model(**inputs)
    
    predicted_class_id = torch.argmax(outputs.logits, dim=1).item()
    return model.config.id2label[predicted_class_id]


## Predict the intent by function call and intent input
intent = get_intent("who is prime minister of india")
print(f"predicted intent : {intent}")