#!/usr/bin/env python3
import asyncio
import websockets
import subprocess
import os
import json

MEMORY_FILE = "dex_memory.json"
dex_memory = {}

def speak(text):
    print(text)
    os.system(f'termux-tts-speak "{text}"')

def load_memory():
    global dex_memory
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, 'r') as f:
            dex_memory.update(json.load(f))
        print("🧠 Memory loaded.")
    else:
        print("📭 No memory yet.")

def save_memory():
    with open(MEMORY_FILE, 'w') as f:
        json.dump(dex_memory, f)

def remember(key, value):
    dex_memory[key] = value
    save_memory()
    speak(f"Remembered: {key} → {value}")

def recall(key):
    val = dex_memory.get(key, "Not found.")
    speak(f"Recall: {key} → {val}")
    return val

def run_shell(cmd):
    try:
        proc = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        return proc.stdout + proc.stderr
    except Exception as e:
        return f"[Dex Error]: {e}"

async def agent():
    load_memory()
    uri = "ws://localhost:8080"
    async with websockets.connect(uri) as ws:
        print("Connected to server")

        while True:
            msg = await ws.recv()
            print(f"💬 Received:\n{msg}")

            output = ""
            commands = [c.strip() for c in msg.splitlines() if c.strip()]
            for cmd in commands:
                if cmd.startswith("shell:"):
                    output += run_shell(cmd[6:].strip()) + "\n"
                elif cmd.startswith("remember "):
                    _, key, value = cmd.split(" ", 2)
                    remember(key, value)
                    output += f"Remembered: {key} → {value}\n"
                elif cmd.startswith("recall "):
                    _, key = cmd.split(" ", 1)
                    val = recall(key)
                    output += f"Recall: {key} → {val}\n"
                else:
                    output += f"❓ Unknown command: {cmd}\n"

            await ws.send(output)

asyncio.run(agent())
