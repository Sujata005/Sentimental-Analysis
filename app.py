import streamlit as st
from textblob import TextBlob
from newspaper import Article
import nltk
from docx import Document
import PyPDF2
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# MUST BE FIRST
st.set_page_config(page_title="Sentiment Analyzer", page_icon="📊")

# Initialize VADER
analyzer = SentimentIntensityAnalyzer()

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('punkt_tab')

def get_precise_sentiment(text):
    vs = analyzer.polarity_scores(text)
    compound = vs['compound']
    
    trigger_words = ['war', 'attack', 'death', 'threat', 'casualty', 'psychopath']
    count = sum(1 for word in trigger_words if word in text.lower())
    
    if count >= 2:
        compound -= 0.2
        
    if compound >= 0.05:
        return "Positive", "😊", compound
    elif compound <= -0.05:
        return "Negative", "🌑", compound
    else:
        return "Neutral", "😐", compound

def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def extract_text_from_docx(file):
    doc = Document(file)
    return "\n".join([para.text for para in doc.paragraphs])

# --- Sidebar ---
with st.sidebar:
    st.header("💡 About the Project")
    st.info("""
    **Tech Stack:**
    - Python (Streamlit)
    - VADER (Sentiment Logic)
    - Newspaper3k (Scraping)
    
    **Precision Logic:**
    Hybrid approach using VADER lexicon with custom weighted heuristics for news context.
    """)
    st.markdown("---")
    st.write("👨‍💻 **Developer:** Sujata Bijalwan")

# --- UI Setup ---
st.title("📊 Sentiment Analysis Dashboard")
st.markdown("Analyze the sentiment of news articles, documents, or raw text.")

tabs = st.tabs(["🔗 Link/URL", "📁 Upload File", "✍️ Paste Text"])
final_text = ""

with tabs[0]:
    url = st.text_input("Enter Article URL:")
    if url:
        try:
            article = Article(url)
            article.download()
            article.parse()
            article.nlp()
            final_text = article.summary
            st.success(f"**Article Title:** {article.title}")
            
            # KEYWORDS MOVE HERE (So they only show for URLs)
            if hasattr(article, 'keywords') and article.keywords:
                st.write("### 🏷️ Top Keywords")
                st.markdown(" ".join([f"`{k}`" for k in article.keywords[:10]]))
        except Exception as e:
            st.error(f"Error fetching article: {e}")

with tabs[1]:
    uploaded_file = st.file_uploader("Upload a file", type=["txt", "pdf", "docx"])
    if uploaded_file:
        if uploaded_file.type == "text/plain":
            final_text = str(uploaded_file.read(), "utf-8")
        elif uploaded_file.type == "application/pdf":
            final_text = extract_text_from_pdf(uploaded_file)
        elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            final_text = extract_text_from_docx(uploaded_file)

with tabs[2]:
    user_text = st.text_area("Paste your text here:")
    if user_text:
        final_text = user_text

# --- Analysis Logic ---
if final_text:
    with st.expander("🔍 View Extracted Content"):
        st.write(final_text)
    
    if st.button("🚀 Analyze Sentiment"):
        label, emoji, score = get_precise_sentiment(final_text)
    
        st.divider()
        col1, col2 = st.columns(2)
    
        with col1:
            st.metric("Refined Sentiment", f"{label} {emoji}")
        with col2:
            st.metric("Confidence Score", f"{round(score, 2)}")
        
        # Visual Progress Bar
        normalized_score = (score + 1) / 2
        st.write(f"**Sentiment Intensity Spectrum (Negative to Positive):**")
        st.progress(normalized_score)

        if label == "Negative" and score < -0.5:
            st.error("🚨 **Critical:** This content contains highly negative or alarming sentiment.")
        elif label == "Positive":
            st.success("✨ **Result:** The tone is generally positive.")
        else:
            st.warning("⚖️ **Result:** The tone is neutral or balanced.")