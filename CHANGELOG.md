# Change History

## [1.0.2] - 2026-04-08
### Fixed
- Fixed Flet 0.80+ deprecation warnings (`ft.app()` to `ft.run()` and `ft.border.all` to `ft.Border.all`).
- Fixed `AttributeError` for `set_clipboard` by migrating to the new asynchronous `ft.Clipboard().set()` service API.

## [1.0.1] - 2026-04-08
### Fixed
- Fixed a crash that occurred when pressing the copy button in the packaged `.exe` (OSError: [WinError 6] The handle is invalid) due to `subprocess` being invoked without console. Replaced `clip.exe` interop with Flet's natively supported `page.set_clipboard()`.

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
