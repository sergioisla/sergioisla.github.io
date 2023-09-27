import streamlit as st
import os
from PIL import Image

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
    ### Data Scientist""")


## Safety Map Front
st.markdown("""
I just finished my Data Science bootcamp at Le Wagon and am eager to continue developing mainly this new path.

I'm an engineer with technical and administrative experience in search of improving the efficiency of the business activities. I achieve my responsibilities through effective prioritization before work in challenging environments, conciliatory attitude, and opportune communication. \n

During the last two weeks of the bootcamp, three mates and I developed an app showing the crimes in Mexico City, plus a map showing a forecast of the crimes in Mexico City during the next 6 months: \n
[safety-map.streamlit.app](https://safety-map.streamlit.app/) \n

""")

st.markdown("""
: ) \n
 \n
""")

st.markdown("""  .\n

    -> Later I developed a map showing the most frequent Ecobici trips from a specific bike station to a specific bike station during March, 2023.
""")

with open("app/ecobici_flow_map.html", "r") as f:
    html_content = f.read()

# Display the HTML content
st.components.v1.html(html_content, width=500,height=550)


st.markdown("""  .\n

    I also created a map showing the location of the UNESCO World Heritage Sites 2019 but color coded by their year of inscription.
    """)


with open("app/heritage_map_2019.html", "r") as h:
    html_content2 = h.read()

# Display the HTML content
st.components.v1.html(html_content2, width=700,height=550)

