import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(layout="wide")

st.title("🏗️ DM–BIM–BEM Graph Dashboard")

html_path = Path("data/outputs/building_graph.html")

if html_path.exists():
    with open(html_path, "r", encoding="utf-8") as f:
        html = f.read()

    components.html(html, height=800, scrolling=True)

else:
    st.error("Graph visualization file not found.")
    st.info("Run `python -m src.visualization.graph_view` locally first.")