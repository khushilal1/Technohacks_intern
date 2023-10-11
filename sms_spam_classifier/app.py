# import streamlit as slt
import pickle


# tfd=pickle.load("Vectorizer.pkl","rb")
with open('Vectorizer.pkl', 'rb') as file:
    tfd = pickle.load(file)


# model=pickle.load("model.pkl","rb")
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)


# text_transform=pickle.load("text_transform_functon.pkl","rb")
with open('text_transform_functon.pkl', 'rb') as file:
    text_transform = pickle.load(file)


# slt.title("Emain/Sms Spam Detection System")
# input_sms =slt.text_input("Enter Your message")
input_sms="Hi hello ,How are you?"


# 1.preprocess
transformed_sms=text_transform(input_sms)
print(transformed_sms)
# 2.Vectorize
# vector_input=tfd.transform([transformed_sms])
# # 3.predict
# result=model.predict(vector_input)
# # 4.Display
# if result==1:
#     print("Spam")

# else:
#     print("Not spam")





