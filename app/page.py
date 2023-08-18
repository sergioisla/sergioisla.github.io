import streamlit as st
import os
from PIL import Image

#API_HOST = os.getenv("API_HOST")

# Setting the wide config for the page
st.set_page_config(layout="wide")
#adding marging specs for the main page with css inyection
margins_css = """
    <style>
        .main > div {
            padding-left: 2rem;
            padding-right: 2rem;
            padding-top: 0.5rem;
        }
    </style>
"""

st.markdown(margins_css, unsafe_allow_html=True)

#Title
st.markdown("""
    ## Sergio Isla
    ### Portfolio""")

col1, col2 = st.columns([1,1])

with col1:
    ## Safety Map Front
    st.markdown("""
    I just finished my Data Science bootcamp at Le Wagon and am eager to continue developing mainly this new path.

I'm an engineer with technical and administrative experience in search of improving the efficiency of the business activities. I achieve my responsibilities through effective prioritization before work in challenging environments, conciliatory attitude, and opportune communication..""")

with col2:
    st.markdown("""
    : ) \n
    : ) \n
    """)
    #To be transparent from the beginning, you can find the data for our project publicly available [here](https://datos.cdmx.gob.mx/dataset/victimas-en-carpetas-de-investigacion-fgj#:~:text=Descargar-,V%C3%ADctimas%20en%20Carpetas%20de%20Investigaci%C3%B3n%20(completa),-CSV)
    

st.markdown("""un mapa
""")

with open("ecobici_flow_map.html", "r") as f:
        html_content = f.read()
    
# Display the HTML content
st.components.v1.html(html_content, height=600)
