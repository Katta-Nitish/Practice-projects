import streamlit as st
from PIL import Image
from io import BytesIO
import requests
response=requests.get("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQKAamECE8Hro_r6Cu1ShDICQ2aEqamvRSfgA&s")
st.title("IBM Calculator")
img=Image.open(BytesIO(response.content))
st.image(img,width=200)
weight=st.number_input("Enter your weight here(in kg):",min_value=0.0,format="%.2f")
unit=st.radio("Select your height unit",["Meters","Feet","Centimeters"])
height=st.number_input("Enter your height",min_value=0.0,format="%.2f")
if st.button("Submit"):
  try:
    if unit=="Centimeters":
      height=height/100
    elif unit=="Feet":
      height=height/3.28
    heightm=height*height
    ibm=weight/heightm
  except:
    st.error("Invalid information")
  else:
    st.success(f"Your BMI is {ibm:.2f}")
    if ibm<16:
      st.error("You are extremely underweight")
    elif 16<ibm<=18.5:
      st.warning("You are underweight")
    elif 18.5<ibm<=25:
      st.success("You are perfectly healthy")
    elif 25<ibm<=30:
      st.warning("You are over weight")
    else :
      st.error("You are extremely overweight")