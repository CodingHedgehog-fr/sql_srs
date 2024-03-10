import streamlit as st
import duckdb
import pandas as pd
import io

csv = """
beverage, price
orange juice,2.5
Expresso,2
Tea,3
"""

beverages = pd.read_csv(io.StringIO(csv))

csv2 = """
food_item, food_price
cookie juice,2.5
Chocolatine,2
Muffin,3
"""

food_items = pd.read_csv(io.StringIO(csv2))

answer = """
select * from beverages
cross join food_items
"""

solution = duckdb.query(answer).df()

st.header("Enter your code")
query = st.text_area(label="votre code SQL ici", key="user_input")

if query:
    result = duckdb.query(query).df()
    st.dataframe(result)

tab2, tab3 = st.tabs(["Tables", "Solution"])

with tab2:
    st.write("table: beverages")
    st.dataframe(beverages)
    st.write("table: food_items")
    st.dataframe(food_items)
    st.write("Expected:")
    st.dataframe(solution)

with tab3:
    st.write(answer)
