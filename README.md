# Universal Translator

<div align="center">
  <img src="static/SVG/bot.svg" alt="Universal Translator Logo" width="120" height="120">
  <h1>Universal Translator</h1>
  <p>A powerful web-based translation service with auto-language detection and text-to-speech capabilities</p>
  
  ![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
  ![FastAPI](https://img.shields.io/badge/FastAPI-0.115.12+-green.svg)
  ![License](https://img.shields.io/badge/License-MIT-yellow.svg)
  ![Vercel](https://img.shields.io/badge/Vercel-Deployed-brightgreen.svg)
</div>

## 📋 Table of Contents

- [Features](#-features)
- [Demo](#-demo)
- [Tech Stack](#-tech-stack)
- [Installation](#-installation)
- [Usage](#-usage)
- [Deployment](#-deployment)
- [API Endpoints](#-api-endpoints)
- [Project Structure](#-project-structure)
- [Contributing](#-contributing)
- [License](#-license)

## ✨ Features

- **Multilingual Support**: Translate between 13+ languages including English, Spanish, French, German, Chinese, and more
- **Auto Language Detection**: Automatically detects the source language with confidence scoring
- **Text-to-Speech**: Listen to both source and translated text with high-quality speech synthesis
- **Responsive Design**: Works seamlessly across desktop, tablet, and mobile devices
- **Elegant UI**: Modern glass-morphism design with beautiful animations and effects
- **Character Count**: Real-time character counting for input text
- **Swap Languages**: Easily switch between source and target languages
- **Copy to Clipboard**: One-click copying of translated text
- **Keyboard Shortcuts**: Use Ctrl+Enter to translate quickly

## 🚀 Demo

The Universal Translator is deployed and accessible at [https://myra-translator.vercel.app](https://myra-translator.vercel.app)

[![Universal Translator Screenshot](https://raw.githubusercontent.com/ShivanshGhelani/Myra-Translator/main/static/screenshot.png)](https://myra-translator.vercel.app)

## 💻 Tech Stack

- **Frontend**:
  - HTML5, CSS3, JavaScript
  - Tailwind CSS for styling
  - Font Awesome for icons

- **Backend**:
  - Python 3.9+
  - FastAPI framework
  - Uvicorn ASGI server

- **Translation Engine**:
  - mtranslate library
  - langdetect for language detection

- **Text-to-Speech**:
  - External TTS API service

## 🔧 Installation

### Prerequisites

- Python 3.9 or higher
- pip (Python package manager)

### Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/ShivanshGhelani/Myra-Translator.git
   cd Myra-Translator
   ```

2. **Create and activate a virtual environment**:
   ```bash
   # On Windows
   python -m venv myra_translate
   myra_translate\Scripts\activate.bat
   
   # On macOS/Linux
   python -m venv myra_translate
   source myra_translate/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```bash
   uvicorn api.main:create_app --reload
   ```

5. **Access the application**:
   Open your browser and navigate to [http://localhost:8000](http://localhost:8000)

## 📖 Usage

1. **Select source and target languages** from the dropdown menus
2. **Enter text** in the source text area
3. **Click the translate button** or press Ctrl+Enter to translate
4. **View translation** in the target text area
5. **Use text-to-speech** buttons to listen to both source and translated text
6. **Copy translated text** to clipboard with the copy button

## 🚀 Deployment

### Deploying to Vercel

This project is set up for seamless deployment on Vercel.

1. **Fork or push the repository to GitHub**:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/yourusername/Myra-Translator.git
   git push -u origin main
   ```

2. **Connect your repository to Vercel**:
   - Go to [Vercel](https://vercel.com) and log in
   - Click "New Project"
   - Import your GitHub repository
   - Vercel will automatically detect the FastAPI framework

3. **Configure Vercel deployment**:
   - The `vercel.json` file in this project already contains the necessary configuration
   - Set the Environment Variables if needed
   - Click "Deploy"

4. **Access your deployed application**:
   - Once deployment is complete, Vercel will provide a URL
   - You can set up a custom domain in the Vercel dashboard

## 🌐 API Endpoints

### Translation API

**Endpoint**: `/translate`  
**Method**: POST  
**Description**: Translates text from one language to another

**Request Body**:
```json
{
  "text": "Hello, how are you?",
  "dest_lang": "es",
  "source_lang": null,
  "auto_detect": true,
  "preserve_formatting": true
}
```

**Response**:
```json
{
  "translated_text": "Hola, ¿cómo estás?",
  "detected_source_language": "en",
  "detection_confidence": 0.95
}
```

## 📁 Project Structure

```
Myra-Translator/
├── api/
│   ├── main.py             # FastAPI application setup
│   └── routes.py           # API router configuration
├── routes/
│   └── translation_routes.py # Translation API endpoint
├── static/
│   ├── SVG/
│   │   ├── bot.svg         # Logo and icons
│   │   └── user.svg        
│   └── favicon.ico
├── templates/
│   └── translate.html      # Main web interface
├── myra_translate/         # Virtual environment
├── README.md
└── requirements.txt
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

<div align="center">
  <p>Created with ❤️ by <a href="https://github.com/ShivanshGhelani">Shivansh Ghelani</a></p>
</div>
