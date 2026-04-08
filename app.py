import streamlit as st
from textblob import TextBlob
from newspaper import Article
import nltk
from docx import Document
import PyPDF2

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('punkt_tab')
st.set_page_config(page_title="Sentiment Analyzer", page_icon="📊")

def get_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity # New line
    
    if polarity > 0:
        label = "Positive"
        emoji = "😊"
    elif polarity < 0:
        label = "Negative"
        emoji = "🌑"
    else:
        label = "Neutral"
        emoji = "😐"
        
    return label, emoji, polarity, subjectivity

def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def extract_text_from_docx(file):
    doc = Document(file)
    return "\n".join([para.text for para in doc.paragraphs])

# --- UI Setup ---
st.title("📊 Sentiment Analysis Dashboard")
st.markdown("Analyze the sentiment of news articles, documents, or raw text.")

tabs = st.tabs(["Link/URL", "Upload File", "Paste Text"])

final_text = ""

# Tab 1: URL Input
with tabs[0]:
    url = st.text_input("Enter Article URL:")
    if url:
        try:
            article = Article(url)
            article.download()
            article.parse()
            article.nlp()
            final_text = article.summary
            st.info(f"**Article Title:** {article.title}")
        except Exception as e:
            st.error(f"Error fetching article: {e}")

# Tab 2: File Upload
with tabs[1]:
    uploaded_file = st.file_uploader("Upload a file", type=["txt", "pdf", "docx"])
    if uploaded_file:
        if uploaded_file.type == "text/plain":
            final_text = str(uploaded_file.read(), "utf-8")
        elif uploaded_file.type == "application/pdf":
            final_text = extract_text_from_pdf(uploaded_file)
        elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            final_text = extract_text_from_docx(uploaded_file)

# Tab 3: Manual Text
with tabs[2]:
    user_text = st.text_area("Paste your text here:")
    if user_text:
        final_text = user_text

# --- Analysis Logic ---
if final_text:
    with st.expander("View Extracted Content"):
        st.write(final_text)
    
    if st.button("Analyze Sentiment"):
        label, emoji, score, subj = get_sentiment(final_text)
    
        st.divider()
    # Creating 3 columns for a professional dashboard look
        col1, col2, col3 = st.columns(3)
    
        with col1:
            st.metric("Label", f"{label} {emoji}")
        with col2:
            st.metric("Polarity Score", f"{round(score, 2)}")
        with col3:
            st.metric("Subjectivity", f"{round(subj, 2)}") # New Metric

    # Logic-based advice for the user
        if subj > 0.6:
            st.info("💡 **Note:** This text appears to be highly opinionated or emotional.")
        else:
            st.info("💡 **Note:** This text appears to be mostly factual/objective.")