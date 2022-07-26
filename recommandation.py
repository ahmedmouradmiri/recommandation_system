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
import pickle
import faiss
import torch
import sentence_transformers
import numpy as np
from Data import list_skills
import json
#model = SentenceTransformer('bert-base-nli-mean-tokens')
model=torch.load('model.pkl')
infile = open('skills_encoder-Copy1','rb')
encoded_file_skills = pickle.load(infile)
infile.close()
class cleaning :
    
    def standardize(self, text):
        lower_text = text.lower()
        nopunc_text = re.sub(r'[^\w\s]',' ', lower_text)
        text_nonum = re.sub(r'\d+', '', nopunc_text) #Remove Numbers
        # substitute multiple whitespace with single whitespace
        # Also, removes leading and trailing whitespaces
        text_no_doublespace = re.sub('\s+', ' ', text_nonum).strip()
        return text_no_doublespace
    
    def tokenize(self, text):
        text=self.standardize(text)
        tokenizer = TreebankWordTokenizer()
        tokens=tokenizer.tokenize(text)
        
        return tokens
    
    def stopword(self, text):
        text=self.tokenize(text)
        stop = set(stopwords.words('english'))
        stop=",".join(stop)
        sentence_after_stopword_removal = [token for token in text if token not in stop]
        sentence_after_stopword_removal_end = " ".join(sentence_after_stopword_removal)
        return sentence_after_stopword_removal_end
    
    def lemma(self, text):
        text=self.stopword(text)
        lemmatizer = WordNetLemmatizer()
        lemmatized_output = ''.join([lemmatizer.lemmatize(token) for token in text])
        #lemmatized_output_tokens=lemmatized_output.split(' ')
        
        return lemmatized_output
    
    def job_cleaner(self,text):
        text=self.lemma(text)
        return text
    
    
    
    def recommandation(self,text) : 
        text=self.job_cleaner(text)
        d=encoded_file_skills.size()[1]
        index=faiss.IndexFlatIP(d)
        index.add(np.array(encoded_file_skills))
        xq=model.encode(text,normalize_embeddings=True)
        k=5
        D,I=index.search(xq.reshape(1,-1),k)
        result={f'{i}':list_skills[i] for i in I[0]}
        json_object = json.dumps(dict(zip(result.keys(),result.values())))
        return json_object
    

    