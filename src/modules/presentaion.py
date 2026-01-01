import gradio as gr
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from qa_agent import answer_question
from sumerize_video import summarize_video

def run_app():
    with gr.Blocks(title="YouTube Summarizer") as interface:
        gr.Markdown("# 🎬 YouTube Video Summarizer & Q&A")
        gr.Markdown("Enter a YouTube URL to summarize the video or ask questions about its content.")
        
        # Shared YouTube URL input at the top
        video_url = gr.Textbox(
            label="YouTube Video URL", 
            placeholder="https://www.youtube.com/watch?v=..."
        )
        
        with gr.Tabs():
            # Summary Tab
            with gr.TabItem("📝 Summary"):
                gr.Markdown("### Generate a summary of the video")
                summarize_btn = gr.Button("Summarize Video", variant="primary")
                summary_output = gr.Textbox(
                    label="Video Summary", 
                    lines=10
                )
                summarize_btn.click(
                    summarize_video, 
                    inputs=video_url, 
                    outputs=summary_output
                )
            
            # Q&A Tab
            with gr.TabItem("❓ Q&A"):
                gr.Markdown("### Ask questions about the video content")
                question_input = gr.Textbox(
                    label="Your Question", 
                    placeholder="What is the main topic of the video?"
                )
                question_btn = gr.Button("Get Answer", variant="primary")
                answer_output = gr.Textbox(
                    label="Answer", 
                    lines=10
                )
                question_btn.click(
                    answer_question, 
                    inputs=[video_url, question_input], 
                    outputs=answer_output
                )
    
    # Launch the app
    interface.launch(server_name="0.0.0.0", server_port=7860)