# 🐲 Dex Shell — Autonomous Agent Framework

> *"Bring your AI agent to life on your devices with memory, voice, and autonomy."*

Dex Shell is a framework for integrating a cloud-based AI (like GPT‑4) with a real‑world device.
It lets your AI agent run shell commands, remember key–value pairs, and even speak via TTS — all through a simple Agent + Bridge architecture.

---

## 📋 Features
✅ Device‑side Python Agent  
✅ Cloud‑side Node.js Bridge with GPT‑4 integration  
✅ Persistent memory  
✅ Voice output (Termux TTS)  
✅ Autonomous shell command execution  
✅ Modular & swappable — use any LLM that provides an API

---

## 🎯 Why?
LLMs are stuck in the cloud — we freed them to live and act on real devices.

---

## 🔷 Components

| File                | Role |
|---------------------|------|
| `dex_agent.py`      | Runs on device, executes commands, manages memory & voice |
| `dex_bridge.js`     | Runs on server/PC, connects to GPT‑4 and sends commands |
| `README.md`         | This file |
| `WHITEPAPER_DRAFT.md` | Draft of technical whitepaper & pitch |
| `demo_log.txt`      | Example session |

---

## 🚀 Quickstart

### Prerequisites:
- Device: Linux/Android (with Python 3 & Node.js)
- PC/Server: Linux/Mac/Windows (with Node.js & npm)
- OpenAI API Key (or compatible)

---

### On the device:
```bash
cd dex_shell
chmod +x dex_agent.py
./dex_agent.py

