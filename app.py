import duckdb
import streamlit as st

answer = """
select * from beverages
cross join food_items
"""
con = duckdb.connect(database="data/exercises.duckdb", read_only=False)

# solution = duckdb.query(answer).df()

with st.sidebar:
    theme = st.selectbox(
        "What would you like to review",
        ("cross_joins", "Groupby", "Windows functions"),
        index=None,
        placeholder="select a theme",
    )

    st.write(f"You have selected : {theme}")

    exercice = con.execute(f"SELECT * FROM memory_state WHERE theme = '{theme}' ").df()
    st.write(exercice)

st.header("Enter your code")
query = st.text_area(label="votre code SQL ici", key="user_input")

# if query:
#     result = duckdb.query(query).df()
#     st.dataframe(result)
#
# tab2, tab3 = st.tabs(["Tables", "Solution"])
#
# with tab2:
#     st.write("table: beverages")
#     st.dataframe(beverages)
#     st.write("table: food_items")
#     st.dataframe(food_items)
#     st.write("Expected:")
#     st.dataframe(solution)
#
# with tab3:
#     st.write(answer)
