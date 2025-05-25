# Create virtual environment
python -m venv voice-anon
source voice-anon/bin/activate

# Install dependencies
pip install torch torchaudio
pip install git+https://github.com/openai/whisper.git
pip install TTS
pip install pydub
pip install gradio  # for UI
