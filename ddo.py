import streamlit as st

col1, col2 = st.columns([2,3])
tab1,tab2 = st.tabs(['Tab A','Tab b'])
with col1 :
    st.title("here is column1 title")
    with tab1 :
        st.write('hello')
    with tab2:
        st.write('h1')

with col2 :
    st.title("here is column2 tltle")
    st.checkbox("this is checkbox1 in col2")
col1.subheader("i am column1 subheader")
col2.checkbox("this is checkbox2 in col2")
