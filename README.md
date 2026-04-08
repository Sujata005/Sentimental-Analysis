# 📊 Sentimental Analysis Dashboard

An intelligent web application that analyses the emotional tone and sentiment of various text sources. Unlike basic sentiment tools, this dashboard uses a **Refined Hybrid Model** to ensure high precision even in complex news contexts.

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![NLP](https://img.shields.io/badge/NLP-VADER%20%2B%20TextBlob-blue?style=for-the-badge)

## 🚀 Live Demo
[[LINK](https://sentimental-analysis-jfvozgrnjutebuha3c3waj.streamlit.app/)]

## ✨ Key Features
- **Multi-Source Input:** - **URLs:** Automatically scrape and summarize news articles.
  - **File Uploads:** Supports `.pdf`, `.docx`, and `.txt` documents.
  - **Manual Entry:** Direct text area for custom analysis.
- **Refined Precision Logic:** Uses VADER sentiment analysis combined with custom keyword-weighting to accurately interpret grim or sensitive news topics.
- **Visual Analytics:** Includes a sentiment intensity spectrum (progress bar) and confidence scoring.
- **Keyword Extraction:** Automatically identifies top keywords from analysed articles.

## 🧠 How It Works
Standard sentiment libraries often misinterpret negative news (like war or threats) as positive because of words like "achieved" or "objectives." 

This project solves that by:
1. **VADER Integration:** Using a model tuned for social media and news nuances.
2. **Context Heuristics:** A custom Python function that scans for high-impact "trigger words" to nudge the compound score, ensuring realistic results for sensitive global events.

## 🛠️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Sujata005/Sentimental-Analysis.git](https://github.com/Sujata005/Sentimental-Analysis.git)
   cd Sentimental-Analysis
2. Install Dependencies:
``` pip install -r requirements.txt ```
3. Run the application:
   ``` streamlit run app.py ```
## 📂 Project Structure
``` app.py ```: Main Streamlit application and NLP logic.

```requirements.txt```: Python dependencies.

```packages.txt```: System-level dependencies for Linux environments.

```nltk.txt```: Specific NLTK data models (punkt, punkt_tab).

### 👤 Author
Sujata Bijalwan
