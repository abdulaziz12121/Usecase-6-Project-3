import streamlit as st
import base64
import json 
import requests 


st.set_page_config(page_title="Riyadh, and The Hunt for a Home!", page_icon="🏠", layout="wide")

# This to center the image, DO NOT REMOVE
st.markdown(
    """
    <style>
        button[title^=Exit]+div [data-testid=stImage]{
            text-align: center;
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 100%;
        }
    </style>
    """, unsafe_allow_html=True
)

left_co, right_co = st.columns(2)
file_ = open("./assets/23.gif", "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()
with left_co:
    # Title
    st.title("Riyadh, and :blue[The Hunt for a Home!]")
with right_co:
    st.markdown(
    f'<img src="data:image/gif;base64,{data_url}" alt="Riyadh, and The Hunt for a Home!">',
    unsafe_allow_html=True,
)
    
st.markdown("---")

# Grad part 
st.subheader("🎉 CONGRATULATIONS! 🎉")
st.subheader("For graduating from the top academy for Data Science!!")



st.markdown("###### Pretty nice getting all those job offers ha? Better go back and thank the academy, especially your instructors! But wait… all offers are in Riyadh? Interviewers are asking if you live in Riyadh?")



st.markdown("###### Oh, now it’s getting real..")
st.markdown("###### Yeah… Yeah we know… it's time to seriously consider moving, and finding a place to stay in Riyadh is a bit annoying (might be an understatement) and it doesn’t help that whenever you go online to find something you just get bombarded by so many options, or none! ")
st.markdown("###### And you’re probably thinking “Wouldn’t it be nice if someone just picked something for me? Or at least help me decide? I need an expert…” ")
st.markdown("###### Well look no more! We did the search for you!")
st.markdown("###### See Riyadh, just like any city, is split into multiple regions:")
st.image("./assets/distribution of region.png", caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

st.markdown("###### We thought perhaps renting apartments fit you best.")
st.markdown("###### And although they are found in all regions, prices vary.")
st.markdown("###### What affects the price is how far the place is from the center, and whether or not it's in a 'hot' new neighborhood.")

st.image("./assets/Price per region.png", caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

option = st.selectbox(
   "**Which region do you want to move to?**",
    ("Center", "West", "East", "North", "South"),
)

if option == "Center":
    st.image("./assets/Center.png", caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

elif option == "West":
    st.image("./assets/West.png", caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

elif option == "North":
    st.image("./assets/North.png", caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

elif option == "East":
    st.image("./assets/East.png", caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

elif option == "South":
    st.image("./assets/South.png", caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")


st.markdown("###### Now all you have to do is consider transportation.")
st.markdown("###### If you’re a practical person and prices don’t matter to you, you would want to be near your workplace.")
st.markdown("###### Or if you’re a person that spends wisely, then we recommend finding a place in the more affordable areas, like South.")

st.markdown("###### Everything you just saw, can be found at [Aqar](https://sa.aqar.fm/), and their offers cover all regions of Riyadh.")
st.markdown("###### Feels great doesn't it? No more worry about where and what to pick. We’re glad we could help!")
st.markdown("###### Take a look at the below list of scenarios, and hopefully one of them could be a great fit for you!")
st.markdown("###### Wishing you all the best in your future endeavors!")

st.markdown("#### Our Recommendations ")



with st.expander("If you don't have a problem to spend more money"):
    st.image("./assets/Top neighborhood.png", caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
        
with st.expander("If you need to spend wisely"):
    st.image("./assets/last 10.png", caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")



