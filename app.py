import streamlit as st

# Title of the application
st.title("My Streamlit Application")

# Header
st.header("Welcome to my application!")

# Subheader
st.subheader("This is a subheader")

# Text
st.text("Hello, Streamlit!")

# Markdown
st.markdown("## This is a markdown heading")
st.markdown("**This** is some markdown text.")

# Display an image
from PIL import Image
image = Image.open("image.jpg")
st.image(image, caption="Streamlit Logo", use_column_width=True)

# Interactive widgets
name = st.text_input("Enter your name", "John Doe")
st.write("Hello,", name)

age = st.number_input("Enter your age", min_value=0, max_value=120, value=30)
st.write("Your age is", age)

option = st.selectbox("Choose an option", ["Option 1", "Option 2", "Option 3"])
st.write("You selected", option)

# Button
if st.button("Click me"):
    st.write("Button clicked!")

# Checkbox
if st.checkbox("Check me"):
    st.write("Checkbox checked!")

# Radio buttons
option = st.radio("Choose an option", ["Option 1", "Option 2", "Option 3"])
st.write("You selected", option)

# Slider
value = st.slider("Select a value", min_value=0, max_value=100, value=50, step=5)
st.write("Selected value:", value)

# Progress bar
import time
progress_bar = st.progress(0)
for i in range(101):
    time.sleep(0.05)
    progress_bar.progress(i)

# Sidebar
st.sidebar.header("Sidebar")
st.sidebar.text("This is a sidebar")

# Dataframes
import pandas as pd
data = pd.DataFrame({
    "Name": ["John", "Jane", "Bob"],
    "Age": [30, 25, 40]
})
st.write(data)
