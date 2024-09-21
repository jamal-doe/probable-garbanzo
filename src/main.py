# Description: This file contains the main functions to convert voice to voice using AssemblyAI and ElevenLabs APIs.
import os
import uuid
from pathlib import Path
from typing import List, Any
from dotenv import load_dotenv

import assemblyai as aai
from translate import Translator
from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs

load_dotenv()


# Function to convert voice to voice
def voice_to_voice(audio_file):

    # transcribe audio
    transcription_response = transcribe_audio(audio_file)

    # Check the status of the transcription
    if transcription_response.status == aai.TranscriptStatus.error:
        raise gr.Error(transcription_response.error)
    else:
        transcript = transcription_response.text

    # translate text
    list_translations = translate_text(transcript)
    generated_audio_paths = []

    # generate speech from text
    for translation in list_translations:
        translated_audio_file_name = text_to_speech(translation)
        path = Path(translated_audio_file_name)
        generated_audio_paths.append(path)

    return generated_audio_paths[0], generated_audio_paths[1], generated_audio_paths[2], \
        list_translations[0], list_translations[1], list_translations[2]


# Function to transcribe audio using AssemblyAI
def transcribe_audio(audio_file):
    # Set the API key
    aai.settings.api_key = os.getenv("ASSEMBLYAI_API_KEY")

    # Create a transcriber object
    transcriber = aai.Transcriber()

    # Transcribe the audio file
    transcript = transcriber.transcribe(audio_file)

    return transcript


# Function to translate text
def translate_text(text: str) -> list[Any]:
    languages = ["tr", "es", "ja"]
    list_translations = []

    for lan in languages:
        translator = Translator(from_lang="en", to_lang=lan)
        translation = translator.translate(text)
        list_translations.append(translation)

    return list_translations


# Function to convert text to speech using ElevenLabs
def text_to_speech(text):

    # Create a client object
    client = ElevenLabs(
        api_key=os.getenv("ELEVENLABS_API_KEY"),
    )

    # Calling the text_to_speech conversion API with detailed parameters
    response = client.text_to_speech.convert(
        voice_id="nsQAxyXwUKBvqtEK9MfK",  # clone your voice on elevenlabs dashboard and copy the id
        optimize_streaming_latency="0",
        output_format="mp3_22050_32",
        text=text,
        model_id="eleven_multilingual_v2",  # use the turbo model for low latency, for other languages use the `eleven_multilingual_v2`
        voice_settings=VoiceSettings(
            stability=0.5,
            similarity_boost=0.8,
            style=0.5,
            use_speaker_boost=True,
        ),
    )

    # Generating a unique file name for the output MP3 file
    save_file_path = f"outputs/{uuid.uuid4()}.mp3"

    # Writing the audio to a file
    with open(save_file_path, "wb") as f:
        for chunk in response:
            if chunk:
                f.write(chunk)

    print(f"{save_file_path}: A new audio file was saved successfully!")

    # Return the path of the saved audio file
    return save_file_path
