from typing import Optional

class ErrorHandler:
    """Centralized error handling and user-friendly messages"""
    
    @staticmethod
    def format_error(error_type: str, details: Optional[str] = None) -> str:
        """
        Format error messages for UI display
        
        Args:
            error_type: Type of error
            details: Additional error details
            
        Returns:
            Formatted error message
        """
        error_messages = {
            "missing_api_key": "⚠️ Please enter your Gemini API key in the sidebar",
            "missing_url": "⚠️ Please enter a YouTube video URL",
            "invalid_url": "❌ Invalid YouTube URL. Please check the URL and try again.",
        }
        
        base_message = error_messages.get(error_type, "❌ An error occurred")
        
        if details:
            return f"{base_message}\n\n{details}"
        
        return base_message
    
    @staticmethod
    def get_success_message(message_type: str) -> str:
        """
        Get success messages
        
        Args:
            message_type: Type of success message
            
        Returns:
            Success message
        """
        success_messages = {
            "transcript_fetched": "✅ Transcript fetched successfully!",
            "summary_generated": "✅ Summary generated successfully!",
        }
        
        return success_messages.get(message_type, "✅ Success!")