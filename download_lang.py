import os
import spacy
import subprocess

# List of spaCy model names
models = [
    'en_core_web_sm',
    'es_core_news_sm',
    'fr_core_news_sm',
    'de_core_news_sm',
    'zh_core_web_sm',
    'xx_ent_wiki_sm',
    'es_core_news_md',
    'pt_core_news_sm',
    'ja_core_news_sm'
]

# Iterate through the models and download them
for model_name in models:
    try:
        # Use subprocess to run the Homebrew Python and the spaCy download command
        subprocess.run(['/opt/homebrew/bin/python3', '-m', 'spacy', 'download', model_name])
        print(f"Downloaded language model: {model_name}")
    except Exception as e:
        print(f"Error downloading {model_name}: {str(e)}")

print("All models downloaded successfully.")
    
