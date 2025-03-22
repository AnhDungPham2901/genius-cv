
import streamlit as st

pg = st.navigation([st.Page("home.py", title="Home"), st.Page("edit_cv.py", title="Edit CV"), st.Page("view_cv.py", title="View CV")])
pg.run()
