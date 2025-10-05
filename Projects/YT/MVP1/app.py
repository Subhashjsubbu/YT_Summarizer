import streamlit as st
from datetime import datetime
from dotenv import load_dotenv
import os
from services.url_validator import URLValidator
from services.transcript_service import TranscriptService
from services.summarizer_service import SummarizerService
from utils.error_handler import ErrorHandler

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="YouTube Video Summarizer",
    page_icon="🎥",
    layout="wide"
)

# Get API key from environment
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

# Initialize services
url_validator = URLValidator()
transcript_service = TranscriptService()
error_handler = ErrorHandler()

# UI Layout
st.title("🎥 YouTube Video Summarizer")
st.markdown("Transform any YouTube video into a concise, structured summary using AI")

# Sidebar
with st.sidebar:
    st.header("⚙️ Configuration")
    
    # Show API key status
    if GEMINI_API_KEY:
        st.success("✅ LLM is ready")
    else:
        st.error("❌ No API Key found in .env file")
        st.info("💡 Create a `.env` file with `GEMINI_API_KEY=your_key`")
    
    st.markdown("---")
    st.markdown("### 📝 How to use")
    st.markdown("""
    1. Paste a YouTube video URL
    2. Click 'Generate Summary'
    3. Wait for the AI analysis
    """)
    st.markdown("---")
    st.markdown("### ℹ️ About")
    st.markdown("**MVP1** - Basic transcript extraction and summarization")
    st.markdown(f"*Last updated: {datetime.now().strftime('%Y-%m-%d')}*")

# Main content area
col1, col2 = st.columns([2, 1])

with col1:
    video_url = st.text_input(
        "YouTube Video URL",
        placeholder="https://www.youtube.com/watch?v=...",
        help="Paste any YouTube video URL here"
    )

with col2:
    st.write("")  # Spacing
    st.write("")  # Spacing
    generate_button = st.button("🚀 Generate Summary", type="primary", use_container_width=True)

# Processing logic
if generate_button:
    # Validate API key
    if not GEMINI_API_KEY:
        st.error(error_handler.format_error("missing_api_key", "Please add GEMINI_API_KEY to your .env file"))
    elif not video_url:
        st.error(error_handler.format_error("missing_url"))
    else:
        # Validate URL
        is_valid, video_id, error = url_validator.validate_url(video_url)
        
        if not is_valid:
            st.error(error_handler.format_error("invalid_url", error))
        else:
            # Optional video preview in expander
            with st.expander("🎬 Preview Video (Optional)"):
             st.video(video_url)
            
            # Fetch transcript
            with st.spinner("🔄 Fetching transcript..."):
                transcript, error = transcript_service.get_transcript(video_id)
            
            if error:
                st.error(error)
            else:
                st.success(error_handler.get_success_message("transcript_fetched"))
                
                # Show transcript preview
                with st.expander("📄 View Transcript Preview"):
                    st.text_area("Transcript", transcript[:1000] + "...", height=200, disabled=True)
                
                # Generate summary
                with st.spinner("🤖 Generating AI summary... This may take a moment."):
                    try:
                        summarizer = SummarizerService(GEMINI_API_KEY)
                        summary, error = summarizer.summarize(transcript)
                    except ValueError as e:
                        summary, error = None, str(e)
                
                if error:
                    st.error(error)
                else:
                    st.success(error_handler.get_success_message("summary_generated"))
                    
                    # Display summary
                    st.markdown("---")
                    st.subheader("📊 Video Summary")
                    st.markdown(summary)
                    
                    # Download button
                    st.download_button(
                        label="📥 Download Summary",
                        data=f"Video URL: {video_url}\n\n{summary}",
                        file_name=f"summary_{video_id}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                        mime="text/plain"
                    )

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray;'>Built with ❤️ using Streamlit & Google Gemini</div>",
    unsafe_allow_html=True
)