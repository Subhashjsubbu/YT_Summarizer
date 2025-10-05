from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import (
    TranscriptsDisabled, 
    NoTranscriptFound, 
    VideoUnavailable
)
from typing import Tuple, Optional

class TranscriptService:
    """Handles YouTube transcript extraction"""
    
    @staticmethod
    def get_transcript(video_id: str) -> Tuple[Optional[str], Optional[str]]:
        """
        Fetch transcript from YouTube video
        
        Args:
            video_id: YouTube video ID
            
        Returns:
            Tuple of (transcript_text, error_message)
        """
        try:
            # Create instance and get list of available transcripts
            api = YouTubeTranscriptApi()
            transcript_list = api.list(video_id)
            
            # Try multiple strategies to get a transcript
            transcript = None
            
            # Strategy 1: Try English first
            try:
                transcript = transcript_list.find_transcript(['en'])
            except:
                pass
            
            # Strategy 2: Try manually created transcripts in any language
            if transcript is None:
                try:
                    for t in transcript_list:
                        if not t.is_generated:
                            transcript = t
                            break
                except:
                    pass
            
            # Strategy 3: Try generated transcripts in any language
            if transcript is None:
                try:
                    for t in transcript_list:
                        if t.is_generated:
                            transcript = t
                            break
                except:
                    pass
            
            # Strategy 4: Just take the first available transcript
            if transcript is None:
                try:
                    transcript = list(transcript_list)[0]
                except:
                    raise NoTranscriptFound(video_id, [], None)
            
            # Fetch the actual transcript data
            transcript_data = transcript.fetch()
            
            # Extract text from FetchedTranscriptSnippet objects
            transcript_text = " ".join([item.text for item in transcript_data])
            
            return transcript_text, None
            
        except TranscriptsDisabled:
            return None, (
                "❌ Transcripts are disabled for this video.\n\n"
                "💡 **Tip**: Try another video with captions enabled."
            )
            
        except NoTranscriptFound:
            return None, (
                "❌ No transcript found for this video.\n\n"
                "💡 **Tip**: The video might not have captions/subtitles available. "
                "Try a video with auto-generated or manual captions."
            )
            
        except VideoUnavailable:
            return None, (
                "❌ Video is unavailable.\n\n"
                "💡 **Tip**: Check if:\n"
                "- The URL is correct\n"
                "- The video is public (not private or unlisted)\n"
                "- The video hasn't been removed"
            )
            
        except Exception as e:
            return None, f"❌ An unexpected error occurred while fetching the transcript: {str(e)}"
    
    @staticmethod
    def get_transcript_with_timestamps(video_id: str) -> Tuple[Optional[list], Optional[str]]:
        """
        Fetch transcript with timestamp information (for future MVP2)
        
        Args:
            video_id: YouTube video ID
            
        Returns:
            Tuple of (transcript_list, error_message)
        """
        try:
            api = YouTubeTranscriptApi()
            transcript_list = api.list(video_id)
            
            # Get first available transcript
            transcript = list(transcript_list)[0]
            transcript_data = transcript.fetch()
            return transcript_data, None
        except Exception as e:
            return None, f"Error fetching transcript: {str(e)}"