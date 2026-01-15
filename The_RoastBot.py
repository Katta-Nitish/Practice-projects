import streamlit as st
from rembg import remove
import json
from PIL import Image
from io import BytesIO
import requests
@st.cache_data
def bot_logo():
  req=requests.get("https://www.sanssapien.com/_next/image?url=https%3A%2F%2Fs3.ap-south-1.amazonaws.com%2Fai-app-discovery%2FImg%2F11d0ca46-1cab-4d3d-be3c-030b69bc2099%2Fabb54305-cde0-4896-a458-8e79993dc71b&w=3840&q=80")
  ig=Image.open(BytesIO(req.content))
  return remove(ig)
col1, col2 = st.columns([2,10]) 
img=bot_logo()
with col1:
    st.image(img, width=200) # Smaller width to fit nicely

with col2:
    st.title("The Roast Bot")
txt=st.text_input("Enter a statement","")

click=st.button("Let's see..")
API_KEY=st.secrets["GEMINI_API_KEY"]
# Make sure it says 'v1beta' and includes ':generateContent' at the end
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={API_KEY}"
headers={
  "content-type":"application/json"
}
payload={
  "contents":[{
    "parts":[{"text":f"You are a sarcastic bot. Reply to this with ONLY a witty roast for example User: I love coding in Python. AI: Wow, you learned print('hello world'), somebody give this genius a medal.User: What is the capital of France? AI: Its Paris. Did you skip elementary school or is your Google broken? User: I missed my bus. AI: Maybe if you ran as fast as your mouth, you would have caught it.user:I missed class today. Ai:My bed held me hostage, and the negotiations for my release fell through. User: {txt} AI:"}]
  }]
}
if click:
  try:
    response=requests.post(url,headers=headers,json=payload)
    if response.status_code==200:
      data=response.json()
      answer=data['candidates'][0]['content']['parts'][0]['text']
      st.success(f"{answer}")
    else:
       st.error(f"{response.status_code}")
  except Exception as e:
    st.error(f"Connection Error: {e}")