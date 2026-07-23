import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

st.title("🏗️ DM–BIM–BEM Graph Dashboard")

# Load the generated graph HTML
with open("data/outputs/building_graph.html", "r", encoding="utf-8") as f:
    html = f.read()

# Display it inside Streamlit
components.html(html, height=800, scrolling=True)