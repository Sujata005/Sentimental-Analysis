# 📊 AI Sentiment Engine & Data Insights Dashboard

An end-to-end Data Science application that bridges Natural Language Processing (NLP) with real-time descriptive analytics. This platform extracts semantic sentiment from unstructured text data across various formats and dynamically aggregates it into an operational intelligence dashboard.

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NLP](https://img.shields.io/badge/NLP-VADER%20%2B%20TextBlob-blue?style=for-the-badge)

## 🚀 Live Demo
[[LINK](https://sentimental-analysis-jfvozgrnjutebuha3c3waj.streamlit.app/)]

## 💡 Dual-Focus Portfolio Value

This project is explicitly engineered to demonstrate competencies required across both **Data Analyst** and **Machine Learning Engineer** roles:

### 1. The Engineering Aspect (AI/NLP)
* **Algorithmic Context Awareness:** Utilises the VADER (Valence Aware Dictionary and sEntimer Reasoner) lexicon, which natively maps semantic shifts (e.g., negations like "not good", intensifiers, and punctuation).
* **Deterministic Heuristics:** Implements a custom keyword-weighting algorithm to address edge cases in the global news context, preventing geopolitical crises or grim articles from falsely flagging as positive due to administrative vocabulary (e.g., "objectives achieved").
* **Unstructured Data Pipeline:** Automates web-scraping and data ingestion from HTML URLs via `Newspaper3k`, text tokenisation with `NLTK`, and file parsing for `.pdf` and `.docx` blobs.

### 2. The Analytical Aspect (Data & Insights)
* **Session Aggregation Lifecycle:** Tracks transactional user interactions seamlessly using state management (`st.session_state`) to cache sequential analyses dynamically.
* **Descriptive Statistics:** Generates instantaneous aggregate KPIs, processing mathematical transformations like running means, mode distribution, and volumetric counts.
* **Exploratory Data Analysis (EDA):** Populates dynamic visualisation layers (categorical frequency bar charts and score variance tracking) to monitor semantic volatility.
* **Data Portability:** Features an on-demand data exporter that structures raw session logs into standardised, cleaned `.csv` datasets for downstream business intelligence workflows.

---

## 🛠️ System Architecture & Workflow

1. **Ingestion Layer:** Accepts unstructured inputs via active web URLs, document file uploads, or manual string entry.
2. **Processing Layer:** Cleans text, runs keyword extraction tokenisers, and targets context triggers.
3. **Sentiment Engine:** Evaluates compound polarity score ranges $[-1, 1]$.
4. **Aggregation Layer:** Updates a structured data ledger in memory via a Pandas backend.
5. **Visualisation UI:** Triggers real-time graphical renders and provides data download options.

---

## 📦 Project Structure

```
├── app.py              # Main application logic, UI design, and NLP pipelines
├── requirements.txt    # Python package dependencies (Streamlit, VADER, Pandas, etc.)
├── packages.txt        # System-level Linux dependencies for production parsing
└── nltk.txt            # Pre-downloaded NLTK tokeniser models (punkt, punkt_tab)
```
## 🛠️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Sujata005/Sentimental-Analysis.git](https://github.com/Sujata005/Sentimental-Analysis.git)
   cd Sentimental-Analysis
2. Install Dependencies:
``` pip install -r requirements.txt ```
3. Run the application:
   ``` streamlit run app.py ```

### 👤 Author
Sujata Bijalwan
