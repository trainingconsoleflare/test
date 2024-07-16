import streamlit as st 
import pandas as pd  
import matplotlib.pyplot as plt 
import plotly.express as px 

st.title('Data Analysis')

file = st.file_uploader('Drop any file',type='xlsx')
if(file!=None):
    df = pd.read_excel(file)
    st.dataframe(df)
    st.markdown(f'Columns in the dataset: {list(df.columns)}')

    st.header('Basic Summary of the Dataset')
    st.dataframe(df.describe())

    st.header('Groupby Operations')
    group_col = st.multiselect('Choose column you want to group',options=list(df.columns))
    operation_col = st.selectbox('Column For Operation',options=list(df.columns))
    operation = st.selectbox('Operation',options=['sum','max','min','mean','media','max','min'])
    result = df.groupby(group_col).agg(
        result= (operation_col,operation)
    ).reset_index()
    
    st.dataframe(result)
    st.header('Visualization')
    graphs = st.selectbox('Graphs',options=[None,'line','bar','pie'])
    if(graphs=='line'):
        x_axis = st.selectbox('Choose X:',options=[None]+list(result.columns))
        y_axis = st.selectbox('Choose Y:',options=[None]+list(result.columns))
        colr = st.selectbox('Choose:',options=[None]+list(result.columns))
        if(x_axis or y_axis or colr):
            fig = px.line(result,x=x_axis,y=y_axis,color=colr)
            st.plotly_chart(fig)
    elif(graphs=='bar'):
        x_axis = st.selectbox('Choose X:',options=[None]+list(result.columns))
        y_axis = st.selectbox('Choose Y:',options=[None]+list(result.columns))
        colr = st.selectbox('Choose:',options=[None]+list(result.columns))
        if(x_axis or y_axis or colr):
            fig = px.bar(result,x=x_axis,y=y_axis,color=colr)
            st.plotly_chart(fig)
    

