import streamlit as st
import numpy as np
import random as rd
from PIL import Image
from io import BytesIO

def Encrypt_image(img,key):
    shp = img.shape
    flat = []
    for i in img:
        for j in i:
            for k in j:
                flat.append(k)
    encrypt = []
    key_idx = 0
    for i in range(shp[0]):
        t = []
        for j in range(shp[1]):
            s=[]
            for k in range(shp[2]):
                s.append(flat[key[key_idx]])
                key_idx+=1
            t.append(s)
        encrypt.append(t)
    encrypt = np.array(encrypt)
    return encrypt

def Decrypt_image(img,key):
    n_key = []
    for i in range(len(key)):
        n_key.append([key[i],i])
    n_key.sort()
    for i in range(len(n_key)):
        n_key[i] = n_key[i][1]
    shp = img.shape
    flat = []
    for i in img:
        for j in i:
            for k in j:
                flat.append(k)
    
    decrypt = []
    key_idx = 0
    for i in range(shp[0]):
        t = []
        for j in range(shp[1]):
            s=[]
            for k in range(shp[2]):
                s.append(flat[n_key[key_idx]])
                key_idx+=1
            t.append(s)
        decrypt.append(t)
    decrypt = np.array(decrypt)
    return decrypt

st.title("Secure Image")
rd.seed(143)

option = st.selectbox('What you want to do?', ('Encryption', 'Decryption'),index=None,placeholder="select from Option")
buf = BytesIO()
if option=='Encryption':
    file = st.file_uploader("Input File",type=["png","jpg","jpeg","tif","bmp"])
    if file is not None:
        img = Image.open(file)
        img = np.array(img)

        st.image(img,caption="Original Image")
        
      
        key = list(range(img.size))
        key = rd.sample(key,len(key))

        encrypt = Encrypt_image(img,key)
        st.image(encrypt,caption="Encrypted Image")
    
        result = Image.fromarray(encrypt.astype('uint8'), 'RGB')

        result.save(buf, format="PNG")
        byte_im = buf.getvalue()

        btn = st.download_button(
        label="Download Encrypted image",
        data=byte_im,
        file_name="encrypt.png",
        mime="image/png")
elif option=='Decryption':
    file = st.file_uploader("Input File",type=["png","jpg","jpeg","tif"])
    if file is not None:
        img = Image.open(file)
        img = np.array(img)

        st.image(img,caption="Encrypted Image")
        
        key = list(range(img.size))
        key = rd.sample(key,len(key))

        decrypt = Decrypt_image(img,key)
        st.image(decrypt,caption="Decrypted Image")
        result = Image.fromarray(decrypt.astype('uint8'), 'RGB')

        result.save(buf, format="PNG")
        byte_im = buf.getvalue()

        btn = st.download_button(
        label="Download Decrypted image",
        data=byte_im,
        file_name="Decrypt.png",
        mime="image/png")
