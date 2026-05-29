from pathlib import Path
import json
import pdfplumber
import pandas as pd


def parse_pdf(file_name:str)->str:
    text_parts =[]
    with pdfplumber.open(file_name) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text_parts.append(page_text)

    return "\n".join(text_parts)

def parse_csv(file_name:str)->str:
    dataFrame = pd.read_csv(file_name)
    return dataFrame.to_csv(index =False)

def parse_json(file_name:str)->str:
    path = Path(file_name)

    with path.open('r',encoding = 'utf-8') as f:
        data = json.load(f)
    
    return json.dumps(data,index =2)

def parse_file(file_name:str)->str:
    extension = Path(file_name).suffix.lower()

    if extension == '.pdf':
        return parse_pdf(file_name)

    if extension == '.csv':
        return parse_csv(file_name)
    
    if extension == '.json':
        return parse_json(file_name)
    
    return ValueError("extension not found")