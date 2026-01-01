from modules.video_data_extract import get_transcript, process_transcript
from modules.prompts import create_qa_prompt_template, create_qa_chain
from modules.llm_model import create_anthropic_llm
from modules.embedding_model import setup_embedding_model
from modules.langchain_data import chunk_transcript, create_faiss_index
from modules.retriever import retrieve_and_generate_answer

def answer_question(video_url, user_question, language='auto'):
    """
    Title: Answer User's Question

    Description:
    This function retrieves relevant context from the FAISS index based on the user’s query 
    and generates an answer using the preprocessed transcript.
    If the transcript hasn't been fetched yet, it fetches it first.

    Args:
        video_url (str): The URL of the YouTube video from which the transcript is to be fetched.
        user_question (str): The question posed by the user regarding the video.

    Returns:
        str: The answer to the user's question or a message indicating that the transcript 
             has not been fetched.
    """
    fetched_transcript = None
    processed_transcript = None
    # Check if the transcript needs to be fetched
    if not processed_transcript:
        if video_url:
            # Fetch and preprocess transcript
            fetched_transcript = get_transcript(video_url, language)
            processed_transcript = process_transcript(fetched_transcript)
        else:
            return "Please provide a valid YouTube URL."

    if processed_transcript and user_question:
        # Step 1: Chunk the transcript (only for Q&A)
        chunks = chunk_transcript(processed_transcript)

       
        llm = create_anthropic_llm()

        # Step 4: Create FAISS index for transcript chunks (only needed for Q&A)
        embedding_model = setup_embedding_model()
        faiss_index = create_faiss_index(chunks, embedding_model)

        # Step 5: Set up the Q&A prompt and chain
        qa_prompt = create_qa_prompt_template()
        qa_chain = create_qa_chain(llm, qa_prompt)

        # Step 6: Generate the answer using FAISS index
        answer = retrieve_and_generate_answer(user_question, faiss_index, qa_chain)
        return answer
    else:
        return "Please provide a valid question and ensure the transcript has been fetched."


if __name__ == "__main__":
    print(answer_question("https://www.youtube.com/watch?v=uiUPD-z9DTg", 
    "What is the main topic of the video?"))