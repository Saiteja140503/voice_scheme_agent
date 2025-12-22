# 🎙️ Telugu Voice-Based Government Scheme Agent

A **voice-first, agentic AI system** that helps users identify **eligible government and public welfare schemes** using **Telugu**, a native Indian language.

The system goes beyond a chatbot by reasoning across multiple voice turns, maintaining memory, invoking tools, and handling speech recognition failures.

---

## 📌 Problem Statement

Many citizens want to apply for government schemes but do not know:
- which schemes they are eligible for
- what information is required
- how to access scheme details in their native language

This project addresses the problem using a **voice-only Telugu interface**, making it accessible to non-English speakers.

---

## 🗣️ Example User Request

> **“నాకు ప్రభుత్వ పథకాల వివరాలు కావాలి”**

The agent asks follow-up questions in Telugu, collects user details, evaluates eligibility, and responds **with spoken Telugu output**.

---

## ✨ Key Features

- 🎧 **Voice-first interaction** (speech input & speech output)
- 🗣️ **End-to-end Telugu pipeline** (STT → Agent → TTS)
- 🧠 **Agentic workflow** using a state machine
- 🗂️ **Conversation memory** across turns
- 🧰 **Multiple tools** for decision making
- 🚨 **Failure handling** for unclear or missing speech

---

## 🧠 Agent Workflow

The agent follows a structured, multi-step flow instead of a single prompt.
<img width="1024" height="1536" alt="ChatGPT Image Dec 22, 2025, 09_03_14 PM" src="https://github.com/user-attachments/assets/c52dc76d-ce98-4f2c-a8d6-3bac27f6fd39" />

At each step, the agent:
- asks a question in Telugu
- stores the response in memory
- decides the next action
- invokes tools only when enough information is available

---

## 🖼️ System Architecture

![System Architecture](images/architecture_flow.png)
<img width="1024" height="1536" alt="ChatGPT Image Dec 22, 2025, 08_52_49 PM" src="https://github.com/user-attachments/assets/14c9a8c4-e1c5-4dbf-b618-93656573ef25" />


**Flow Overview:**
1. User provides Telugu voice input  
2. Speech is converted to text using Whisper  
3. Text is normalized into Telugu script  
4. Agent reasons using memory and a state machine  
5. Tools are invoked for eligibility and scheme lookup  
6. Final response is spoken in Telugu  

---

## 🔁 Agent State Machine

![State Machine](images/state_machine.png)

**States Used:**
- START  
- ASK_AGE  
- ASK_INCOME  
- ASK_OCCUPATION  
- EVALUATE  
- DONE  
<img width="1024" height="1536" alt="ChatGPT Image Dec 22, 2025, 09_03_14 PM" src="https://github.com/user-attachments/assets/63ad9e16-e9d7-4fad-9026-c5abada45c3a" />

This ensures logical progression and prevents premature conclusions.

---

## 🧰 Tools Used

### 1️⃣ Eligibility Engine
Determines which schemes apply based on:
- age
- annual income
- occupation

### 2️⃣ Scheme Information Tool (Mock API)
Fetches descriptions and benefits of eligible schemes.

> Tool usage is explicit and dynamic — responses are not hard-coded.

---




### 📁 Project Structure

voice_scheme_agent/
├── main.py                # Entry point
├── stt.py                 # Speech-to-text (Whisper + filters)
├── tts.py                 # Telugu text-to-speech
├── agent.py               # Agent logic & state machine
├── agent_state.py         # Conversation memory
├── eligibility_tool.py    # Eligibility engine (Tool 1)
├── scheme_tool.py         # Scheme info retrieval (Tool 2)
├── text_normalizer.py     # Telugu normalization
├── audio/                 # Telugu WAV voice inputs
├── images/                # Architecture & state diagrams
│   ├── architecture_flow.png
│   └── state_machine.png
├── requirements.txt
└── README.md
---
# ⚙️ Setup Instructions

This document explains how to set up and run the **Telugu Voice-Based Government Scheme Agent** locally.

---

## 🔧 System Requirements

- **Operating System**: Windows / Linux / macOS  
- **Python**: 3.9 or 3.10 (recommended)  
- **Microphone**: Required for live voice input  
- **FFmpeg**: Required for audio processing  

---

## 🐍 Python Environment Setup

### 1️⃣ Create a Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
### Install Dependencies

Make sure you are inside the project directory, then run:

pip install -r requirements.txt
🎧 FFmpeg Installation

FFmpeg is required for audio decoding and preprocessing.

Windows

Download FFmpeg from: https://ffmpeg.org/download.html

Extract the folder

Add the bin/ directory to System PATH

Verify installation:

ffmpeg -version

Linux
sudo apt install ffmpeg

macOS
brew install ffmpeg

▶️ Running the Project
1️⃣ Prepare Audio Input

Place Telugu .wav audio files inside the audio/ directory

Audio should be 16kHz, mono for best results

2️⃣ Run the Agent
python main.py




