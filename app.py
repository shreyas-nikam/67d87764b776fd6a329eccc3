import streamlit as st
import pages.input_page as input_page
import pages.visualizations as visualizations
import pages.markdown_page as markdown_page

st.set_page_config(page_title="QuCreate Streamlit Lab", layout="wide")
st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()
st.title("QuLab")
st.divider()

# Sidebar navigation
selected = st.sidebar.radio("Navigation", ["Input & Calculations", "Visualizations", "Documentation"])

if selected == "Input & Calculations":
    input_page.app()
elif selected == "Visualizations":
    visualizations.app()
elif selected == "Documentation":
    markdown_page.app()

st.divider()
st.write("© 2025 QuantUniversity. All Rights Reserved.")
st.caption("The purpose of this demonstration is solely for educational use and illustration. "
           "To access the full legal documentation, please visit this link. Any reproduction of this demonstration "
           "requires prior written consent from QuantUniversity.")
