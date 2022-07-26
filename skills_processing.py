import nltk
from nltk.tokenize import TreebankWordTokenizer
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
nltk.download('stopwords')
from nltk.corpus import stopwords
import string
import re
import pandas as pd
import numpy as np 
from sentence_transformers import SentenceTransformer
from sentence_transformers.evaluation import EmbeddingSimilarityEvaluator
import pickle
import faiss
import torch
model=torch.load('model')
with open('skills_encoder-Copy1','rb') as f:
            encoded_file_skills_final=pickle.load(f)
class skills :
    
    def standardize_skills(self,text) :
        lower_text = text.lower()
        nopunc_text = re.sub(r'[^\w\s]',',', lower_text)
        text_nonum = re.sub(r'\d+', '', nopunc_text)
        #text_no_doublespace = re.sub('\s+', ' ', text_nonum).strip()
        return text_nonum
    def get_model(self):
        model=torch.load('model')
        return model
    def embedding_skills(self,text) :
        global encoded_file_skills_final
        text=self.standardize_skills(text)
        model=self.get_model()
        skills_encoded=model.encode(text,show_progress_bar=True,
                                    output_value='sentence_embedding',
                                    normalize_embeddings=True,convert_to_tensor=True)
            
        encoded_file_skills1= torch.cat([encoded_file_skills_final,
                    skills_encoded.reshape(1,-1),
                    encoded_file_skills_final[:0]])
        encoded_file_skills_final=encoded_file_skills1
        return encoded_file_skills_final
    
#s=skills()
#s.embedding_skills()
#with open('skills_encoder-Copy1','wb') as f:
           #pickle.dump(encoded_file_skills_final,f)