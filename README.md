
<p align="center">
  <img src="assets/logo/logo.png" width="220" alt="Dropbox Transfer Bot Logo">
</p>

<h1 align="center">Dropbox HTML Video Generator Bot</h1>

<p align="center"><strong>Developer: Anubhav</strong></p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Telegram%20Bot-API-0088cc?logo=telegram&logoColor=white" />
  <img src="https://img.shields.io/badge/License-MIT-green.svg" />
  <img src="https://img.shields.io/badge/HTML5-Video%20Player-orange?logo=html5&logoColor=white" />
  <img src="https://img.shields.io/badge/Platform-Telegram-blue?logo=telegram" />
  <img src="https://img.shields.io/badge/Status-Active-success" />
</p>

<p align="center">
Easily convert any Dropbox video link into a fully-functional custom HTML video player with a modern UI and auto-generated HTML file — delivered directly through Telegram.
</p>

---

## 📌 Features

### 🔗 Dropbox Link Handler
- Accepts any **Dropbox shareable link**
- Automatically converts it into a **direct playable video URL**
- Fixes `dl=0` issues by converting them into `dl=1`

### 🎨 HTML Template Injection
- Uses a premium-styled video player (from `dl3.html`)
- Inserts your Dropbox direct URL into the video source
- Custom title & video UI loading inside the template

### 🤖 Telegram Bot Features
- `/start` command with conversation flow  
- Deletes previous messages for a clean UI  
- Stores temporary HTML, sends the file, and auto-deletes  
- Asks for filename and outputs `filename.html`  
- Supports direct sending of a Dropbox link without commands

### 🎥 Premium-Looking Video Player Template
The template includes:
- Custom controls  
- Speed options  
- Volume slider  
- Quality menu  
- Fullscreen with rotation lock  
- Auto-hide controls  
- Mobile optimizations  
- Download blocking & long-press prevention  
- Spinner while buffering  

All these UI/UX features load automatically into the generated HTML.

---

## 📂 Project Structure

```
├── fyp.py               # Telegram bot code
├── dl3.html             # Premium video player template
└── assets/logo/logo.png # Logo for README
```

---

## 🚀 Installation & Setup

### 1️⃣ Install Required Libraries
```bash
pip install python-telegram-bot==20.0
```

### 2️⃣ Add Your Bot Token
In `fyp.py` replace:

```python
BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"
```

### 3️⃣ Run the Bot
```bash
python fyp.py
```

---

## 🧠 How It Works Internally

### ✔ 1. Accept Dropbox Link  
User sends:

```
https://www.dropbox.com/s/abc123/video.mp4?dl=0
```

### ✔ 2. Convert to Direct Video  
Transforms to:

```
dl.dropboxusercontent.com/...&dl=1
```

### ✔ 3. Inject Into HTML Template  
Replaces the default hardcoded URL inside `dl3.html`.

### ✔ 4. Generate Output File  
Example output:

```
myvideo.html
```

### ✔ 5. Send File to User  
Bot sends the HTML file and deletes the temporary file.

---

## 🛡 Security

- No files stored on server  
- HTML generated temporarily  
- Auto-delete after sending  
- User chat cleaned for privacy

---

## 👨‍💻 Developer

**Anubhav**

---

## 📜 License

This project is licensed under the **MIT License**.
