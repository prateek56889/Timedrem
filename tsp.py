import streamlit as st
import pandas as pd
def filterr(data):
    lis=[]
    for i in data["Time"]:
        ior=i[:-6]
        j=ior.split("T")
        j1=j[0]
        j2=j[1]
        if int(j2[:-6])>12:
            nt=str(int(j2[:-6])-12)+j2[2:]+" PM"
            lis.append(str(j1)+" T "+nt)
        if int(j2[:-6])<12:
            lis.append(str(j1)+" T "+str(j2)+" AM")
        if int(j2[:-6])==12:
            lis.append(str(j1)+" T "+str(j2)+" PM")
        
    data["Time"]=lis
    return data
st.title("Time_Converter")
st.write("upload your file")
file=st.file_uploader(label="Upload the file",type=["csv"])
if file:
    dat=pd.read_csv(file,delimiter=",")
    st.write(filterr(dat))
    
else:
    st.write("File kaun upload karega !!")





