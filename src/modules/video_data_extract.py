import re
from youtube_transcript_api import YouTubeTranscriptApi

def get_video_id(url):    
    pattern = r'https:\/\/www\.youtube\.com\/watch\?v=([a-zA-Z0-9_-]{11})'
    match = re.search(pattern, url)
    return match.group(1) if match else None

def get_transcript(url, language='auto'):
    """
    Fetch transcript from YouTube video.
    
    Args:
        url: YouTube video URL
        language: Language code (e.g., 'en', 'es') or 'auto' to auto-detect
    
    Returns:
        Fetched transcript or None if not available
    """
    video_id = get_video_id(url)
    
    ytt_api = YouTubeTranscriptApi()
    transcripts = ytt_api.list(video_id)
    
    transcript = None
    fallback_transcript = None
    
    for t in transcripts:
        # Auto-detect: prefer manual transcripts, then auto-generated
        if language == 'auto':
            if not t.is_generated:
                transcript = t.fetch()
                break
            elif fallback_transcript is None:
                fallback_transcript = t.fetch()
        # Specific language requested
        elif t.language_code == language:
            if not t.is_generated:
                transcript = t.fetch()
                break
            elif fallback_transcript is None:
                fallback_transcript = t.fetch()
    
    return transcript or fallback_transcript  
def process_transcript(transcript):
    # Initialize an empty string to hold the formatted transcript
    txt = ""
    
    # Loop through each entry in the transcript
    for i in transcript:
        try:
            # Append the text and its start time to the output string
            txt += f"Text: {i.text} Start: {i.start}\n"
        except KeyError:
            # If there is an issue accessing 'text' or 'start', skip this entry
            pass
            
    # Return the processed transcript as a single string
    return txt      


if __name__ == "__main__":
    print(process_transcript(get_transcript("https://www.youtube.com/watch?v=uiUPD-z9DTg")))    