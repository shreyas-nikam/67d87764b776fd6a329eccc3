import streamlit as st
from pages.input_page import input_page
from pages.calculation_page import calculation_page
from pages.visualization_page import visualization_page

st.set_page_config(page_title="Balance Sheet Estimator", layout="wide")
st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()
st.title("QuLab")
st.divider()

page = st.sidebar.selectbox("Select a page", ["Inputs", "Calculations", "Visualizations"])

if page == "Inputs":
    input_page()
elif page == "Calculations":
    calculation_page()
elif page == "Visualizations":
    if 'user_inputs' in st.session_state:
        metrics = calculate_financial_metrics(st.session_state.user_inputs)
        visualization_page(metrics[0], metrics[1], metrics[2], metrics[3])
    else:
        st.warning("Please submit your inputs first.")

st.divider()
st.write("© 2025 QuantUniversity. All Rights Reserved.")
st.caption("The purpose of this demonstration is solely for educational use and illustration. "
           "To access the full legal documentation, please visit this link. Any reproduction of this demonstration "
           "requires prior written consent from QuantUniversity.")
