#  AI Video Assistant

An AI-powered video and meeting intelligence assistant that can **transcribe, summarize, extract insights, and answer questions from video or audio content using Retrieval-Augmented Generation (RAG)**.

The application accepts a **YouTube URL or local media file**, processes the audio, generates a transcript, extracts structured meeting insights, and allows users to chat with the content through a modern Streamlit interface.

##  Live Demo

 [Launch AI Video Assistant](https://aivideoassistant-avd.streamlit.app/)

##  Features

-  **YouTube & Local File Processing** — Analyse YouTube videos or local audio/video files.
-  **Automatic Audio Processing** — Downloads, converts, and chunks audio for transcription.
-  **Local Speech-to-Text** — Uses OpenAI Whisper for transcription.
-  **English & Hinglish Workflow** — Select the language mode from the application sidebar.
-  **AI Title Generation** — Generates a contextual title from the transcript.
-  **AI Summarization** — Produces a concise summary of the processed content.
-  **Action Item Extraction** — Identifies actionable tasks from conversations.
-  **Key Decision Extraction** — Extracts important decisions discussed in the content.
-  **Open Question Extraction** — Detects unresolved or important questions.
-  **RAG-Based Chat** — Ask questions directly about the processed transcript.
-  **Chat History** — Maintains the current question-answer conversation in the Streamlit session.
-  **Modern Streamlit UI** — Dark, responsive interface with live pipeline status.

##  How It Works

```text
YouTube URL / Local Media File
              │
              ▼
       Audio Processing
              │
              ▼
       Audio Chunking
              │
              ▼
     Whisper Transcription
              │
              ▼
     AI Title Generation
              │
              ▼
        Summarization
              │
              ▼
  Action Items / Decisions /
       Open Questions
              │
              ▼
       Text Embeddings
              │
              ▼
      Chroma Vector Store
              │
              ▼
       RAG-Based Chat
```

##  Tech Stack

| Technology | Purpose |
| --- | --- |
| Python | Core application development |
| Streamlit | Interactive web interface |
| OpenAI Whisper | Local speech-to-text transcription |
| yt-dlp | YouTube audio acquisition |
| pydub | Audio conversion and chunking |
| FFmpeg | Audio/video processing |
| LangChain | LLM and RAG orchestration |
| Mistral AI | Generative AI and question answering |
| Hugging Face / Sentence Transformers | Text embeddings |
| ChromaDB | Local vector database |
| PyTorch | Whisper backend |
| python-dotenv | Environment variable management |

##  Project Structure

```text
AI_VIDEO_ASSISTANT/
│
├── app.py
├── main.py
├── test.py
├── requirements.txt
├── .gitignore
│
├── core/
│   ├── transcriber.py
│   ├── summarizer.py
│   ├── extractor.py
│   ├── rag_engine.py
│   └── vector_store.py
│
└── utils/
    └── audio_processor.py
```



##  Installation

### 1. Clone the repository

```bash
git clone <https://github.com/meharr22/AI_VIDEO_ASSISTANT>
cd AI-Video-Assistant
```

### 2. Create a virtual environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### macOS / Linux

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Install FFmpeg

FFmpeg must be installed separately and available in your system `PATH`.

Verify the installation using:

```bash
ffmpeg -version
ffprobe -version
```

### 5. Configure environment variables

Create a `.env` file in the project root.

```env
MISTRAL_API_KEY=your_mistral_api_key
```


##  Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

Open the local Streamlit URL shown in the terminal, enter a YouTube URL or local file path, choose the language mode, and click **Analyse**.

##  CLI Mode

The project also includes a command-line pipeline:

```bash
python main.py
```

The CLI processes the input, prints the generated title, summary, action items, key decisions, and open questions, and then starts an interactive RAG chat session.

##  RAG Pipeline

The Retrieval-Augmented Generation pipeline follows these steps:

1. The generated transcript is prepared for retrieval.
2. Transcript text is split into manageable chunks.
3. Hugging Face embeddings convert text chunks into vectors.
4. ChromaDB stores and indexes the vectors locally.
5. Relevant transcript chunks are retrieved for each user question.
6. The LLM generates an answer grounded in the retrieved transcript context.

This allows users to **chat with the content of a meeting or video instead of asking a model to answer without transcript context**.

##  Use Cases

- Meeting intelligence
- Lecture and educational video analysis
- YouTube content summarization
- Interview analysis
- Webinar processing
- Podcast transcription and summarization
- Action-item tracking
- Question answering over long-form video content

##  Author

**Mehar Arora**


