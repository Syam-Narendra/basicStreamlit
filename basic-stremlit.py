import streamlit as st

st.title("Streamlit Title")
st.write("Stream write")
st.success("success")
st.info("Streamlit info")

sliderValue = st.slider(label="slidebar",min_value=0,max_value=25,step=10)
st.write(sliderValue)

selectedRadio = st.radio("Pickone",options=["syam","asbc","asc"])
st.write(selectedRadio)


isClicked = st.button("Click me!!")

if isClicked:
    clear = st.write("clicked!!!")

isClear = st.button("Clear!!")
if isClear:
    clear = st.write("")