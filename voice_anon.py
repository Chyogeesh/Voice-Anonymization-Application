import whisper
from TTS.api import TTS
from pydub import AudioSegment
import gradio as gr
import tempfile
import os

# Initialize models
whisper_model = whisper.load_model("base")
tts = TTS(model_name="tts_models/multilingual/multi-dataset/your_tts", progress_bar=False)

def anonymize_voice(audio_file, target_voice="male"):
    # Convert input to WAV if needed
    audio = AudioSegment.from_file(audio_file)
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp_wav:
        audio.export(tmp_wav.name, format="wav")
    
    # Transcribe audio
    result = whisper_model.transcribe(tmp_wav.name)
    text = result["text"]
    os.unlink(tmp_wav.name)
    
    # Voice parameters based on selection
    voice_params = {
        "male": {"speaker": "lj", "language": "en"},
        "female": {"speaker": "jenny", "language": "en"},
        "robot": {"speaker": "awb", "language": "en"}
    }
    
    # Generate new voice
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as output_file:
        tts.tts_to_file(
            text=text,
            speaker=voice_params[target_voice]["speaker"],
            language=voice_params[target_voice]["language"],
            file_path=output_file.name
        )
        
        # Convert back to input format
        output_audio = AudioSegment.from_wav(output_file.name)
        output_path = "output.mp3"
        output_audio.export(output_path, format="mp3")
        os.unlink(output_file.name)
    
    return output_path, text

# Create Gradio interface
iface = gr.Interface(
    fn=anonymize_voice,
    inputs=[
        gr.Audio(source="microphone", type="filepath"),
        gr.Dropdown(["male", "female", "robot"], label="Target Voice")
    ],
    outputs=[
        gr.Audio(label="Anonymized Voice"),
        gr.Textbox(label="Recognized Text")
    ],
    title="Voice Anonymizer",
    description="Record your voice and transform it to protect your identity"
)

iface.launch()
