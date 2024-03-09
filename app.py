import streamlit as st
import pandas as pd
import duckdb

st.write("Hello World")
data = {"a": [1, 2, 3], "b": [4, 5, 6]}
df = pd.DataFrame(data)

tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
    st.header("a Cat")
    sql_query = st.text_area(label="Entrez votre input")
    st.write(sql_query)
    st.dataframe(duckdb.query(sql_query).df())

with tab2:
    st.header("a Dog")

with tab3:
    st.header("an Owl")
