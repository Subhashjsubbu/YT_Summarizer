import google.generativeai as genai
from typing import Tuple, Optional
from config.prompts import EXPERT_ANALYST_PROMPT, MAX_TRANSCRIPT_LENGTH, GEMINI_MODEL

class SummarizerService:
    """Handles AI-powered summarization using Google Gemini"""
    
    def __init__(self, api_key: str):
        """
        Initialize summarizer with API key
        
        Args:
            api_key: Google Gemini API key
        """
        self.api_key = api_key
        self._configure_api()
    
    def _configure_api(self):
        """Configure Gemini API"""
        try:
            genai.configure(api_key=self.api_key)
            self.model = genai.GenerativeModel(GEMINI_MODEL)
        except Exception as e:
            raise ValueError(f"Failed to configure Gemini API: {str(e)}")
    
    def summarize(self, transcript: str) -> Tuple[Optional[str], Optional[str]]:
        """
        Generate summary from transcript
        
        Args:
            transcript: Video transcript text
            
        Returns:
            Tuple of (summary, error_message)
        """
        try:
            # Truncate transcript if too long
            truncated_transcript = transcript[:MAX_TRANSCRIPT_LENGTH]
            
            # Build prompt
            prompt = f"""{EXPERT_ANALYST_PROMPT}

Transcript:
{truncated_transcript}

Please provide a detailed summary following the structure mentioned above."""
            
            # Generate summary
            response = self.model.generate_content(prompt)
            
            if not response or not response.text:
                return None, "❌ Failed to generate summary. The API returned an empty response."
            
            return response.text, None
            
        except Exception as e:
            error_message = self._handle_api_error(e)
            return None, error_message
    
    @staticmethod
    def _handle_api_error(error: Exception) -> str:
        """
        Handle and format API errors
        
        Args:
            error: Exception from API call
            
        Returns:
            Formatted error message
        """
        error_str = str(error).lower()
        
        if "api key" in error_str or "authentication" in error_str:
            return (
                "❌ Authentication error with Gemini API.\n\n"
                "💡 **Tip**: Check if your API key is:\n"
                "- Entered correctly\n"
                "- Valid and active\n"
                "- Has the necessary permissions"
            )
        
        if "quota" in error_str or "limit" in error_str:
            return (
                "❌ API quota exceeded.\n\n"
                "💡 **Tip**: You've reached your API usage limit. "
                "Wait a few minutes or check your quota in Google AI Studio."
            )
        
        if "rate limit" in error_str:
            return (
                "❌ Rate limit exceeded.\n\n"
                "💡 **Tip**: Too many requests in a short time. Please wait a moment and try again."
            )
        
        return f"❌ Error generating summary with Gemini: {str(error)}"