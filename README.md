# 🩺 Dr. Pixel

**AI-Powered Medical Image Analysis Assistant**

Dr. Pixel is a Streamlit web application that allows users to upload or capture medical images and receive a structured, non-diagnostic analysis powered by Google’s Gemini vision models. The app is designed strictly for **educational and exploratory purposes**, with strong emphasis on safety, uncertainty awareness, and medical disclaimers.

---

## ✨ Features

* 📁 **Upload medical images** (PNG, JPG, JPEG)
* 📷 **Capture images using device camera**
* 🧠 **AI-powered visual analysis** using Gemini Vision
* 📊 **Structured output** with observations, interpretations, and limitations
* 📉 **Automatic image resizing** for performance and stability
* 🔐 **Secure API key handling** using Streamlit Secrets
* ⚠️ **Built-in medical disclaimer** to prevent misuse

---

## 🖼️ How It Works

1. Choose an input mode:

   * Upload an image
   * Take a picture using your camera
2. The image is converted to RGB
3. The resized image is sent to Gemini for analysis
4. Results are displayed in a clear, structured format:

   * Image overview
   * Visual observations
   * Possible (non-diagnostic) interpretations
   * Uncertainty & limitations
   * Recommended next steps

---

## 🚀 Live Demo

Deploy easily on **Streamlit Community Cloud** (instructions below).

---

## 🛠️ Tech Stack

* **Frontend:** Streamlit
* **AI Model:** Google Gemini (Vision)
* **Image Processing:** Pillow (PIL)
* **Deployment:** Streamlit Community Cloud

---

## 📦 Installation (Local)

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/dr-pixel.git
cd dr-pixel
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Set up secrets (local)

Create a file at:

```
.streamlit/secrets.toml
```

```toml
GEMINI_API_KEY = "your_api_key_here"
```

⚠️ Do **NOT** commit this file to GitHub.

---

## ▶️ Run the App

```bash
streamlit run app.py
```

---

## ☁️ Deployment (Streamlit Community Cloud)

1. Push your code to GitHub (without secrets)
2. Go to **Streamlit Community Cloud**
3. Click **New App**
4. Select:

   * Repository
   * Branch
   * Main file path (`app.py`)
5. Open **Advanced settings → Secrets**
6. Paste:

   ```toml
   GEMINI_API_KEY = "your_api_key_here"
   ```
7. Deploy 🎉

---

## 📄 requirements.txt

```txt
streamlit>=1.32.0
google-generativeai>=0.5.0
Pillow>=10.0.0
```

---

## ⚠️ Medical Disclaimer

> This application provides **AI-generated analysis for educational purposes only**.
> It does **not** provide medical diagnoses, treatment recommendations, or professional medical advice.
> Always consult a qualified healthcare professional for medical concerns.

---

