import streamlit as slt
import pickle
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
ps=PorterStemmer()


# tfd=pickle.load("Vectorizer.pkl","rb")
with open('Vectorizer.pkl', 'rb') as file:
    tfd = pickle.load(file)


# model=pickle.load("model.pkl","rb")
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)





def text_transform(text):
    text_lower=text.lower() #changing all chaarcter into lower
#     print(f'text_in_lower={text_lower}')
    
    text_break_word=nltk.word_tokenize(text_lower)#breaking all the sentence into word and store in list 
#     print(f'text_break_word={text_break_word}')
    
    #TEXT WITHOUT SPECIAL  CHARACTER
    text_without_spec_char=[]
    for i in text_break_word:
        if  i.isalnum():
            text_without_spec_char.append(i) #REMOVING THE SPECIAL CHARACTER
#     print(f'text_without_spec_char={text_without_spec_char}') 
    
    
    #REMOVING  THE stopword and punctuation
    text_without_stopword_punc=[]
    for i in text_without_spec_char:
        if i not in stopwords.words("english") and i not in string.punctuation:
            text_without_stopword_punc.append(i)
#     print(f'text_without_stopword_punc={text_without_stopword_punc}')
        
        
    #removig stemming 
    text_without_stemming=[]
    for i in text_without_stopword_punc:
        text_without_stemming.append(ps.stem(i))
        
#     print(f'text_without_stemming={text_without_stemming}') 
            
    return " ".join(text_without_stemming)

    


slt.title("Email/Sms Spam Detection System")
input_sms =slt.text_area("Enter Your message")
# input_sms="Hi hello ,How are you?"

if slt.button("Predict"):
    # 1.preprocess
    transformed_sms=text_transform(input_sms)
    print(transformed_sms)

    # 2.Vectorize
    vector_input=tfd.transform([transformed_sms])
    # # 3.predict
    result=model.predict(vector_input[0])
    # # 4.Display
    if result==1:
        slt.header("Spam")

    else:
        slt.header("Not spam")





