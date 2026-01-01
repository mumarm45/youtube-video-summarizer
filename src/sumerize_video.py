from modules.video_data_extract import get_transcript, process_transcript
from modules.prompts import create_summary_prompt, create_summary_chain
from modules.llm_model import create_anthropic_llm

def summarize_video(video_url, language='auto'):
    """
    Title: Summarize Video

    Description:
    This function generates a summary of the video using the preprocessed transcript.
    If the transcript hasn't been fetched yet, it fetches it first.

    Args:
        video_url (str): The URL of the YouTube video from which the transcript is to be fetched.

    Returns:
        str: The generated summary of the video or a message indicating that no transcript is available.
    """
    global fetched_transcript, processed_transcript
    
    
    if video_url:
        # Fetch and preprocess transcript
        fetched_transcript = get_transcript(video_url, language)
        processed_transcript = process_transcript(fetched_transcript)
    else:
        return "Please provide a valid YouTube URL."

    if processed_transcript:
        llm = create_anthropic_llm()

        summary_prompt = create_summary_prompt()
        summary_chain = create_summary_chain(llm, summary_prompt)

        # Step 4: Generate the video summary
        summary = summary_chain.run({"transcript": processed_transcript})
        return summary
    else:
        return "No transcript available. Please fetch the transcript first."

if __name__ == "__main__":
    print(summarize_video("https://www.youtube.com/watch?v=uiUPD-z9DTg"))           