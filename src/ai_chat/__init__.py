dakin-aios-desktop/
├── src/
│   ├── main.py
│   ├── ai_chat/
│   │   ├── __init__.py
│   │   ├── chat_engine.py
│   │   └── ui_chat.py
│   ├── ai_browser/
│   │   ├── __init__.py
│   │   ├── browser_engine.py
│   │   └── ui_browser.py
│   ├── ai_terminal/
│   │   ├── __init__.py
│   │   ├── terminal_engine.py
│   │   └── ui_terminal.py
│   ├── api_server/
│   │   ├── __init__.py
│   │   ├── server.py
│   │   └── auth.py
│   ├── ui/
│   │   ├── App.tsx
│   │   ├── ChatPanel.tsx
│   │   ├── BrowserPanel.tsx
│   │   ├── TerminalPanel.tsx
│   │   ├── ProjectDirectorPanel.tsx
│   │   └── index.html
│   ├── tests/
│   │   ├── test_chat.py
│   │   ├── test_browser.py
│   │   ├── test_terminal.py
│   │   └── test_api.py
├── config/
│   ├── settings.json
│   └── api_keys.json (template)
├── requirements.txt
├── package.json
├── main.js (Electron entry)
├── README.md
└── .gitignore
