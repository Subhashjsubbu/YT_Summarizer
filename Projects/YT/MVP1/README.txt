# YouTube Video Summarizer - MVP1

Transform any YouTube video into a concise, structured summary using AI-powered content analysis.

## 🏗️ Project Structure

```
youtube-summarizer-mvp1/
│
├── app.py                      # Main Streamlit application
├── requirements.txt            # Python dependencies
├── README.md                   # Documentation
│
├── config/
│   └── prompts.py             # System prompts and configurations
│
├── services/
│   ├── __init__.py
│   ├── url_validator.py       # YouTube URL validation
│   ├── transcript_service.py  # Transcript extraction logic
│   └── summarizer_service.py  # AI summarization service
│
└── utils/
    ├── __init__.py
    └── error_handler.py       # Centralized error handling
```

## 🚀 Features

- **URL Validation**: Supports multiple YouTube URL formats
- **Transcript Extraction**: Fetches video transcripts automatically
- **AI Summarization**: Expert content analyst powered by Google Gemini
- **Error Handling**: Clear, user-friendly error messages in UI
- **Export**: Download summaries as text files
- **Clean Architecture**: Modular, maintainable codebase

## 📦 Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd youtube-summarizer-mvp1
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Get your Google Gemini API key from [Google AI Studio](https://makersuite.google.com/app/apikey)

## 🎯 Usage

1. Run the Streamlit app:
```bash
streamlit run app.py
```

2. Enter your Gemini API key in the sidebar

3. Paste a YouTube video URL

4. Click "Generate Summary"

5. Download or copy the generated summary

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **Transcript**: youtube-transcript-api
- **LLM**: Google Gemini Flash
- **Hosting**: Streamlit Cloud (Free Tier)

## 💰 Cost Breakdown

- Transcript extraction: FREE
- LLM (Gemini Flash): ~$0.0004 per video
- Hosting: FREE (Streamlit Cloud)

**Total cost: ~$0 for MVP testing**

## 🔧 Configuration

Edit `config/prompts.py` to customize:
- System prompt for the AI analyst
- Maximum transcript length
- Gemini model version

## 🚦 Error Handling

The app handles various errors gracefully:
- Invalid YouTube URLs
- Disabled transcripts
- Missing captions
- Video unavailable
- API key issues
- Rate limiting
- Quota exceeded

All errors are displayed clearly in the UI with helpful tips.

## 📈 Future Roadmap

- **MVP2**: Timestamp-based explanations, visual generation
- **MVP3**: RAG Q&A, user accounts, history
- **MVP4**: Batch processing, API, analytics

## 🤝 Contributing

This is an MVP project. Feel free to fork and adapt for your needs!

## 📄 License

MIT License - feel free to use for your projects.

---

Built with ❤️ using Streamlit & Google Gemini