import duckdb
import streamlit as st
import ast

answer = """
select * from beverages
cross join food_items
"""
con = duckdb.connect(database="data/exercises.duckdb", read_only=False)

# solution = duckdb.query(answer).df()

with st.sidebar:
    theme = st.selectbox(
        "What would you like to review",
        ("cross_joins", "Groupby", "window_functions"),
        index=None,
        placeholder="select a theme",
    )

    st.write(f"You have selected : {theme}")

    exercice = con.execute(f"SELECT * FROM memory_state WHERE theme = '{theme}' ").df()
    st.write(exercice)

st.header("Enter your code")
query = st.text_area(label="votre code SQL ici", key="user_input")

if query:
    result = con.execute(query).df()
    st.dataframe(result)

tab2, tab3 = st.tabs(["Tables", "Solution"])

with tab2:
    st.write(exercice.loc[0, "tables"])
    print(exercice.loc[0, "tables"])
    exercice_tables = ast.literal_eval(exercice.loc[0, "tables"])
    for table in exercice_tables:
        st.write(f"table: {table}")
        df_table = con.execute(f"SELECT * FROM {table}").df()
        st.dataframe(df_table)
#     st.write("table: beverages")
#     st.dataframe(beverages)
#     st.write("table: food_items")
#     st.dataframe(food_items)
#     st.write("Expected:")
#     st.dataframe(solution)
#

with tab3:
    exercise_name = exercice.loc[0, "exercise_name"]
    with open(f"answers/{exercise_name}.sql", "r") as f:
        answer = f.read()
    st.text(answer)
