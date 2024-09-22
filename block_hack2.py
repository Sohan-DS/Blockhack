import os
import streamlit as st
import random
import time

# Simulated companies with portfolio links
companies = [
    {"name": "Company 1", "portfolio": "https://portfolio1.com"},
    {"name": "Company 2", "portfolio": "https://portfolio2.com"},
    {"name": "Company 3", "portfolio": "https://portfolio3.com"},
    {"name": "Company 4", "portfolio": "https://portfolio4.com"},
    {"name": "Company 5", "portfolio": "https://portfolio5.com"},
    {"name": "Company 6", "portfolio": "https://portfolio6.com"},
    {"name": "Company 7", "portfolio": "https://portfolio7.com"},
    {"name": "Company 8", "portfolio": "https://portfolio8.com"},
    {"name": "Company 9", "portfolio": "https://portfolio9.com"},
    {"name": "Company 10", "portfolio": "https://portfolio10.com"},
]

# Function to simulate auction creation
def create_auction(model_path, budget):
    return random.sample(companies, 3)  # Randomly select 3 bidders

# Streamlit UI
st.title("Construction Auction DApp Prototype")
st.write("Upload your 3D model, JPEG image, or PDF and set your budget for construction.")

# File uploader for models, images, and PDFs
model_file = st.file_uploader("Upload 3D Model, JPEG Image, or PDF", type=['stl', 'obj', 'fbx', 'jpeg', 'jpg', 'pdf'])

# Input for budget
budget = st.number_input("Enter Budget for Construction", min_value=0)

if st.button("Create Auction"):
    if model_file is not None and budget > 0:
        # Ensure the directory exists
        upload_dir = "uploaded_models"
        os.makedirs(upload_dir, exist_ok=True)

        model_path = os.path.join(upload_dir, model_file.name)  # Create the full path
        with open(model_path, "wb") as f:
            f.write(model_file.getbuffer())

        # Show the uploaded image if it's an image file
        if model_file.type in ['image/jpeg', 'image/png']:
            st.image(model_file, caption="Uploaded Image", use_column_width=True)

        # Simulate auction creation
        bids = create_auction(model_path, budget)
        st.success("Auction created successfully!")

        # Display company bids
        st.write("Selected Bidders:")
        for bid in bids:
            st.write(f"- {bid['name']} (Portfolio: [Link]({bid['portfolio']}))")

        # Countdown timer
        countdown_time = 60  # 1 minute countdown
        st.write("Auction ends in:")
        countdown_placeholder = st.empty()
        for remaining in range(countdown_time, 0, -1):
            countdown_placeholder.write(f"{remaining} seconds")
            time.sleep(1)

        # User selects a company
        chosen_company = st.selectbox("Choose a company to select for your project:", [bid['name'] for bid in bids])

        if st.button("Submit Choice"):
            selected_company = next((c for c in bids if c['name'] == chosen_company), None)
            if selected_company:
                st.success(f"You selected {selected_company['name']}! Portfolio: [Link]({selected_company['portfolio']})")
            else:
                st.error("Company not found.")
    else:
        st.error("Please upload a valid file and enter a budget.")