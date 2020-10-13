# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 09:17:21 2020

@author: prachi
"""
import streamlit as st
import pickle
import numpy as np
pks= pickle.load(open('rfmodel.pkl','rb'))


def predict_disease(*args):
    input=np.array([args]).astype(np.float64)
    prediction=pks.predict(input)
    
    return int(prediction)

def main():
    st.title("Credit Card Defaulter Prediction App")
    html_temp="""
    <div style="background-color:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;">Are you a defaulter? </h2>
    </div>
    """ 
    
    page_bg_img = '''
    <style>
    body {
    background-image: url("https://images.unsplash.com/photo-1589758438368-0ad531db3366?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=889&q=80");
    background-size: cover;
    }
    </style>
    '''
    st.markdown(html_temp, unsafe_allow_html=True)
    st.markdown(page_bg_img, unsafe_allow_html=True)
    a = st.text_input("BALANCE LIMIT","Type Here")
    b = st.text_input("SEX","Type Here")
    c = st.text_input("AGE","Type Here")
    d = st.text_input("BILL AMT1","Type Here")
   
    
    e = st.text_input("BILL AMT 2","Type Here")
    f = st.text_input("BILL AMT 3","Type Here")
    g = st.text_input("BILL AMT 4","Type Here")
    h = st.text_input("BILL AMT 5","Type Here")
    i = st.text_input("BILL AMT 6","Type Here")
    j = st.text_input("PAY AMT 1 ","Type Here")
    k = st.text_input("PAY AMT 2","Type Here")
    l = st.text_input("PAY AMT 3","Type Here")
    m = st.text_input("PAY AMT 4","Type Here")
    n = st.text_input("PAY AMT 5","Type Here")
    o = st.text_input("PAY AMT 6","Type Here")
    
          
    
    safe_html="""  
      <div style="background-color:#F4D03F;padding:10px >
       <h2 style="color:white;text-align:center;">Congratulations! You have successfully managed to maintain minimum balance </h2>
       </div>
    """
    
    
    danger_html="""  
      <div style="background-color:#F08080;padding:10px >
       <h2 style="color:black ;text-align:center;">Alert! You are below minimum balance.</h2>
       </div>
    """
    
    if st.button("Predict"):
        output=predict_disease(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o)
        st.success('The probability is {}'.format(output*100))
        
        
        if output == 1:
            st.markdown(danger_html,unsafe_allow_html=True)
        else:
            st.markdown(safe_html,unsafe_allow_html=True)
     
            
if __name__=='__main__':
   main()