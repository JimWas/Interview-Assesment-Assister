# JimWas Interview Assessment Assister

This script takes a screenshot of your Windows desktop every 2 minutes and uploads it to **Google Gemini** for analysis.  
The AI will return a response to the prompt you configure (default: `"answer this question?"`).

---

## 🚀 Features
- Automatically captures your desktop screenshot
- Sends screenshot + custom text prompt to Gemini
- Prints Gemini's response in your terminal
- Runs continuously in the background
- Error handling for API/network issues

---

## 📦 Requirements

- Python 3.9+  
- Google Gemini API key ([get one here](https://aistudio.google.com/app/apikey))  
- Install dependencies:

```powershell
pip install google-generativeai pillow pyautogui
