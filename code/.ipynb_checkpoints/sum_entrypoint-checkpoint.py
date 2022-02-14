from transformers import BartTokenizer, BartForConditionalGeneration, BartConfig
from transformers import pipeline
import json

def model_fn(model_dir):
    
    tokenizer = BartTokenizer.from_pretrained(model_dir)
    model = BartForConditionalGeneration.from_pretrained(model_dir)
    nlp=pipeline("summarization", model=model, tokenizer=tokenizer)
    
    return nlp


def transform_fn(nlp, request_body, input_content_type, output_content_type="application/json"):
    
    if input_content_type == "text/csv":
        result = nlp(request_body, truncation=True)[0]
    
    else:
        raise Exception("content type not supported")
    
    return json.dumps(result)
