import re
from typing import Optional, Tuple

class URLValidator:
    """Validates and extracts video IDs from YouTube URLs"""
    
    URL_PATTERNS = [
        r'(?:youtube\.com\/watch\?v=|youtu\.be\/|youtube\.com\/embed\/)([^&\n?#]+)',
        r'youtube\.com\/watch\?.*v=([^&\n?#]+)'
    ]
    
    @staticmethod
    def extract_video_id(url: str) -> Optional[str]:
        """
        Extract video ID from various YouTube URL formats
        
        Args:
            url: YouTube video URL
            
        Returns:
            Video ID if found, None otherwise
        """
        if not url or not isinstance(url, str):
            return None
            
        url = url.strip()
        
        for pattern in URLValidator.URL_PATTERNS:
            match = re.search(pattern, url)
            if match:
                return match.group(1)
        
        return None
    
    @staticmethod
    def validate_url(url: str) -> Tuple[bool, Optional[str], Optional[str]]:
        """
        Validate YouTube URL and extract video ID
        
        Args:
            url: YouTube video URL
            
        Returns:
            Tuple of (is_valid, video_id, error_message)
        """
        if not url:
            return False, None, "Please enter a YouTube video URL"
        
        video_id = URLValidator.extract_video_id(url)
        
        if not video_id:
            return False, None, "Invalid YouTube URL format. Please check the URL and try again."
        
        return True, video_id, None