import streamlit as st
import google.generativeai as genai
from PIL import Image

# get API key from Streamlit secrets
GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]

# Set up Streamlit page configuration
st.set_page_config(page_title="Dr. Pixel", page_icon=":robot:")

# Set up page title and subtitle
st.title("Dr. Pixel 🚨🩺")
st.subheader("Your AI-Powered Medical Image Analysis Assistant")

# User chooses which input to use
input_mode = st.radio("Select input mode", ["Upload Image", "Take a Picture"], horizontal=True)

uploaded_image = None
camera_image = None

if input_mode == "Upload Image":
    uploaded_image = st.file_uploader(
        "Upload a medical image for analysis",
        type=["png", "jpg", "jpeg"],
        key="uploader"
    )
    medical_image = uploaded_image

else:
    camera_image = st.camera_input("Take a picture", key="camera")
    medical_image = camera_image

# Preview
if medical_image is not None:
    st.image(medical_image, caption=f"Selected Medical Image ({input_mode})", use_container_width=True)

submit_button = st.button("Analyze Image")

if submit_button:
    if medical_image is None:
        st.warning("⚠️ Please upload a medical image or take a picture first!")
    else:
        with st.spinner("🔍 Analyzing your medical image..."):
            try:
                genai.configure(api_key=GEMINI_API_KEY)
                image = Image.open(medical_image).convert("RGB")

                model = genai.GenerativeModel("gemini-flash-latest")

                prompt = """Analyze this medical image in detail:

1. Anatomical Structures: Identify visible organs, tissues, or body parts
2. Observations: Note any abnormalities, lesions, or unusual features
3. Potential Findings: Suggest possible conditions (non-definitive)
4. Recommendations: Provide next steps or additional tests if appropriate

Important: Be cautious and avoid definitive diagnosis. Use uncertainty language.
"""
                response = model.generate_content([prompt, image])

                st.success("✅ Analysis Complete!")
                st.markdown("### 📊 Analysis Results")
                st.markdown(response.text)

                st.divider()
                st.warning(
                    "⚠️ **Medical Disclaimer**: This is an AI-generated analysis for educational purposes only. "
                    "Always consult a qualified healthcare professional for diagnosis and treatment."
                )
            except Exception as e:
                st.error(f"❌ An error occurred: {str(e)}")