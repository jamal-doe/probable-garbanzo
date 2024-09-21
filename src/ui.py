import gradio as gr
from main import voice_to_voice

with gr.Blocks(theme=gr.themes.Soft(primary_hue='red')) as demo:
    gr.Markdown("## Record yourself in English and immediately receive voice translations.")
    with gr.Row():
        with gr.Column():
            audio_input = gr.Audio(sources=["microphone"],
                                   type="filepath",
                                   show_download_button=True,
                                   waveform_options=gr.WaveformOptions(
                                       waveform_color="#01C6FF",
                                       waveform_progress_color="#0066B4",
                                       skip_length=2,
                                       show_controls=False,
                                   ), )
            with gr.Row():
                submit = gr.Button("Submit", variant="primary")
                btn = gr.ClearButton(audio_input, "Clear")

    with gr.Row():
        with gr.Group() as turkish:
            tr_output = gr.Audio(label="Turkish", interactive=False)
            tr_text = gr.Markdown()

        with gr.Group():
            es_output = gr.Audio(label="Spanish", interactive=False)
            es_text = gr.Markdown()

        with gr.Group():
            jp_output = gr.Audio(label="Japanese", interactive=False)
            jp_text = gr.Markdown()

    output_components = [tr_output, es_output, jp_output, tr_text, es_text, jp_text]
    submit.click(fn=voice_to_voice, inputs=audio_input, outputs=output_components, show_progress=True)

if __name__ == "__main__":
    demo.launch()
