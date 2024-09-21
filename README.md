# Voice-to-Voice Translation

This project provides a voice-to-voice translation service using AssemblyAI for transcription and ElevenLabs for text-to-speech conversion. The user can record their voice in English and receive immediate voice translations in Turkish, Spanish, and Japanese.

## Features

- **Voice Transcription**: Converts spoken English into text using AssemblyAI.
- **Text Translation**: Translates the transcribed text into Turkish, Spanish, and Japanese using the `translate` library.
- **Text-to-Speech**: Converts the translated text into speech using ElevenLabs.

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/voice-to-voice-translation.git
    cd voice-to-voice-translation
    ```

2. **Create a virtual environment**:
    ```sh
    conda env create -f environment.yml
    conda activate sts_env
    ```

3. **Set up environment variables**:
    Create a `.env` file in the root directory and add your API keys:
    ```dotenv
    ELEVENLABS_API_KEY=your_elevenlabs_api_key
    ASSEMBLYAI_API_KEY=your_assemblyai_api_key
    ```

## Usage

1. **Run the application**:
    ```sh
    python src/ui.py
    ```

2. **Interact with the UI**:
    - Record your voice in English.
    - Click the "Submit" button.
    - Receive voice translations in Turkish, Spanish, and Japanese.

## Project Structure

- `src/main.py`: Contains the main functions for voice transcription, text translation, and text-to-speech conversion.
- `src/ui.py`: Contains the Gradio UI components.
- `environment.yml`: Lists the dependencies required for the project.
- `.env`: Stores the API keys for ElevenLabs and AssemblyAI.

## Dependencies

- `gradio==4.44.0`
- `assemblyai==0.12.0`
- `elevenlabs==1.9.0`
- `translate==3.6.1`
- `dotenv==0.21.0`

Refer to `environment.yml` for the full list of dependencies.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.