import os
import re

def load_headlines():
    existing_headlines = set()
    try:
        with open('headlines.txt', 'r', encoding='utf-8') as file:
            for line in file:
                existing_headlines.add(line.strip()) 
    except FileNotFoundError:
        pass

    return existing_headlines

def save_headlines(headlines):
    with open('headlines.txt', 'a', encoding='utf-8') as file:  
        headlines = set(headlines)  # Ensure uniqueness in case we call this repeatedly
        for title in headlines:
            file.write(title + '\n') 


def clean_headline(text):
    text = text.strip()
    text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces with a single space
    text = re.sub(r'http\S+', '', text) # Remove URLs
    text = re.sub(r'\S+@\S+', '', text) # email address
    text = re.sub(r'\d{10}', '', text) # phone number

    return text