# Voice-Anonymization-Application
This is a internship assignment
Concept Overview
Voice anonymization involves:

Speech-to-text conversion (transcription)

Text-to-speech synthesis with a different voice

Optional voice transformation without full TTS

Technical Approach
Option 1: Full TTS Pipeline (More Reliable)
Use Whisper (open-source from OpenAI) for speech recognition

Use Coqui TTS or VITS for voice synthesis

Implement a voice selection mechanism

Option 2: Voice Conversion (More Challenging)
Use So-VITS-SVC or RVC for voice conversion

Requires more computational resources

Needs voice samples for training
