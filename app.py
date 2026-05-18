import streamlit as st
import pandas as pd
from textblob import TextBlob
from newspaper import Article
import nltk
from docx import Document
import PyPDF2
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# MUST BE FIRST
st.set_page_config(page_title="Data Science Sentiment Hub", page_icon="📊", layout="wide")

# Initialize VADER
analyzer = SentimentIntensityAnalyzer()

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('punkt_tab')

# --- DATA ANALYST FEATURE: Session State Logger ---
if 'analytics_data' not in st.session_state:
    st.session_state['analytics_data'] = []

def log_analysis(source_type, title_or_snippet, label, score):
    st.session_state['analytics_data'].append({
        "Source Type": source_type,
        "Content Identification": title_or_snippet[:50] + "..." if len(title_or_snippet) > 50 else title_or_snippet,
        "Sentiment Label": label,
        "Confidence Score": score
    })

# --- AI/ML FEATURE: Precision Model ---
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
    st.header("💡 Advanced Data Insights")
    st.info("""
    **AI Engine:** VADER Lexicon + Custom Heuristics
    
    **Analytics Engine:** Real-time descriptive metrics and data distribution logging.
    """)
    st.markdown("---")
    st.write("👨‍💻 **Developer:** Sujata Bijalwan")

# --- Main Layout Split ---
st.title("📊 AI Sentiment & Data Insights Dashboard")
st.markdown("Extract text semantics using custom AI heuristics and evaluate categorical distribution patterns.")

tabs = st.tabs(["🔗 Link/URL", "📁 Upload File", "✍️ Paste Text"])
final_text = ""
source_name = ""
source_type = ""

with tabs[0]:
    url = st.text_input("Enter Article URL:")
    if url:
        try:
            article = Article(url)
            article.download()
            article.parse()
            article.nlp()
            final_text = article.summary
            source_name = article.title
            source_type = "Web URL"
            st.success(f"**Article Title:** {article.title}")
            
            if hasattr(article, 'keywords') and article.keywords:
                st.write("### 🏷️ Top Keywords")
                st.markdown(" ".join([f"`{k}`" for k in article.keywords[:10]]))
        except Exception as e:
            st.error(f"Error fetching article: {e}")

with tabs[1]:
    uploaded_file = st.file_uploader("Upload a file", type=["txt", "pdf", "docx"])
    if uploaded_file:
        source_type = "File Document"
        source_name = uploaded_file.name
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
        source_name = "Manually Pasted Text"
        source_type = "Manual Entry"

# --- Run Analysis & Log ---
if final_text:
    with st.expander("🔍 View Extracted Content"):
        st.write(final_text)
    
    if st.button("🚀 Analyze & Log Data"):
        label, emoji, score = get_precise_sentiment(final_text)
        
        # Log data point for the analytics engine
        log_analysis(source_type, source_name, label, score)
    
        st.divider()
        col1, col2 = st.columns(2)
    
        with col1:
            st.metric("Refined Sentiment", f"{label} {emoji}")
        with col2:
            st.metric("Confidence Score", f"{round(score, 2)}")
        
        normalized_score = (score + 1) / 2
        st.write(f"**Sentiment Intensity Spectrum:**")
        st.progress(normalized_score)

        if label == "Negative" and score < -0.5:
            st.error("🚨 **Critical Flag:** Alarming or highly negative semantic content detected.")
        elif label == "Positive":
            st.success("✨ **Result:** Optimistic/Positive semantic context.")
        else:
            st.warning("⚖️ **Result:** Evaluated as balanced/neutral content.")

# --- DATA ANALYST SECTION: Dashboard Summary ---
st.markdown("---")
st.header("📈 Session Aggregation & Trend Analysis")

if st.session_state['analytics_data']:
    df = pd.DataFrame(st.session_state['analytics_data'])
    
    # 1. High-Level Metrics
    m1, m2, m3 = st.columns(3)
    with m1:
        st.metric("Total Items Processed", len(df))
    with m2:
        st.metric("Average Sentiment Score", f"{round(df['Confidence Score'].mean(), 2)}")
    with m3:
        # Finding the most frequent label
        mode_label = df['Sentiment Label'].mode()[0] if not df.empty else "N/A"
        st.metric("Dominant Dataset Sentiment", mode_label)
        
    # 2. Charts Layout
    chart_col1, chart_col2 = st.columns(2)
    
    with chart_col1:
        st.subheader("📊 Sentiment Frequency Distribution")
        # Visualizing category distribution
        label_counts = df['Sentiment Label'].value_counts()
        st.bar_chart(label_counts)
        
    with chart_col2:
        st.subheader("🎯 Score Variance Across Sources")
        # Visualizing score variation
        st.line_chart(df['Confidence Score'])
        
    # 3. Data Inspection Table
    with st.expander("📂 View Raw Analytical Ledger"):
        st.dataframe(df, use_container_width=True)
        
        # Allow downloading dataset as CSV (Crucial Data Analyst tool!)
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Export Analysis Ledger as CSV",
            data=csv,
            file_name="sentiment_analytics_report.csv",
            mime="text/csv"
        )
else:
    st.info("No records logged yet. Run a few analyses above to build the real-time analytics chart engine.")