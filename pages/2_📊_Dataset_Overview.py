import streamlit as st

st.set_page_config(page_title="Data Overview", page_icon="📊", layout="wide")


st.markdown("# Dataset Overview")
st.markdown("These are data for the real estate transactions that took place in the Kingdom of Saudi Arabia, it was scraped from [Aqar](https://sa.aqar.fm)")

columns = "user_id,id,title,price,content,imgs,refresh,beds,livings,wc,area,street_width,age,last_update,ketchen,ac,furnished,location,path,district,width,length,advertiser_type,create_time,review,profileImg,UserName,iam_verified,onMarket,IsRent"

descriptions = {
    "user_id": "The user id",
    "id": "The post id",
    "title": "Title of the rental apartments",
    "price": "Price of the rental",
    "content": "Description of the rental",
    "imgs": "Images related to the rental",
    "refresh": "Last refresh timestamp",
    "beds": "Number of bedrooms ",
    "livings": "Number of living rooms",
    "wc": " Number of bathrooms",
    "area": "Area in square meters",
    "street_width": "Width of the street",
    "age": "Age of the property",
    "last_update": "Last update timestamp",
    "ketchen": "Presence of a kitchen",
    "ac": "Presence of air conditioning",
    "furnished": "Furnished status",
    "location": "Location of the property",
    "path": "Path to the property",
    "district": "District of the property",
    "width": "Width of the property",
    "length": "Length of the property",
    "advertiser_type": "Type of advertiser",
    "create_time": "Creation time of the listing",
    "review": "User reviews",
    "profileImg": "Profile image of the advertiser",
    "UserName": "Name of the user",
    "iam_verified": "Verification status of the user",
    "onMarket": "Whether the property is on the market",
    "IsRent": "Whether the property is for rent"
}

column_list = columns.split(',')

st.markdown("## Introducion")
st.markdown("### Data")
st.markdown("The dataset contains the following columns:")
for i, column in enumerate(column_list, start=1):
    description = descriptions.get(column, ".")
    st.markdown(f"`{i}. {column}`: {description}")



st.markdown("### Data Source")
st.markdown("The data is collected from the following sources:")
st.markdown("1. [Scrapped from Aqar](https://sa.aqar.fm)")
