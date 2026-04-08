# CallGemma 4 - User Manual

Welcome to **CallGemma 4**, a modern, lightweight, and blazing-fast desktop chat interface for your local Gemma AI model!

## Prerequisites
1. You must have **Ollama** installed on your system.
2. The `gemma4:latest` model must be pulled and available locally (`ollama run gemma4:latest`).

## Installation & Setup
The project comes with an isolated Python virtual environment (`.callgemma4`) to ensure maximum stability.
If you need to reinstall dependencies manually:
```powershell
python -m venv .callgemma4
.\.callgemma4\Scripts\pip.exe install flet ollama
```

## How to Launch
To open the user interface, run the following command in your terminal from the project root folder:
```powershell
.\.callgemma4\Scripts\python.exe main.py
```

## Features & Usage
- **Chat Interface**: Type your prompt into the bottom text box and press `Enter` (or click the Send arrow).
- **Real-time Streaming**: Gemma's responses will seamlessly stream into your window immediately, character by character.
- **Copy Formatting**: Every AI response features a "Copy" button at the bottom right. Clicking it will securely copy the text **along with all its original Markdown formatting** to your Windows clipboard. You can paste it into Notion, Notepad++, Obsidian, or Word!

## Troubleshooting
- If you encounter a connection error, please verify that your local Ollama backbone service is actively running.
