import os

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
