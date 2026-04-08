# Change History

## [1.0.0] - 2026-04-08
### Added
- Official 1.0 Release.
- Graphical Chat Interface powered by the Flet framework (dark mode support).
- Integration with local Ollama server running the `gemma4:latest` model.
- Real-time token streaming mechanism for immediate text rendering without UI freeze.
- Active visual loading indicator (`ProgressRing`) to prevent perceived lag during generation.
- Dedicated Flet background thread (`page.run_thread`) ensuring continuous UI updates.
- One-click copy utility preserving complete Markdown structure.
- Native Windows `clip.exe` interop to securely copy output directly to OS.
