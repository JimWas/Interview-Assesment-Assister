# JimWas Interview Assessment Assister

**JimWas Interview Assessment Assister** is a Python-based tool designed to assist with answering questions during online interviews or exams by leveraging the **Google Gemini AI** (`gemini-1.5-flash` model). The application captures screenshots of your screen at user-defined intervals (default: every 2 minutes), sends them to the Gemini API for analysis, and displays AI-generated responses in a user-friendly GUI.

To ensure compliance with exam proctoring software, the tool is designed to run on a **secondary computer** (e.g., a laptop or desktop) using remote desktop software such as [VNC](https://www.realvnc.com), [NoMachine](https://www.nomachine.com), or [Windows RDP](https://learn.microsoft.com/en-us/windows-server/remote/remote-desktop-services/welcome-to-rds) to connect to your primary exam-taking computer. This setup prevents the testing software from detecting the assistant, as it runs independently on a separate machine.

> ⚠️ **Ethical Note**: This tool is intended for **educational and demonstration purposes only**. Using it to gain an unfair advantage in exams or interviews may violate academic integrity or professional ethics policies. Always ensure compliance with relevant guidelines and use this tool responsibly, such as for practice exams or mock interviews.

---

## **Demo Version**

The demo version is provided as a standalone `.exe` file for Windows, making it incredibly easy to use:

- **Download** the `jimwas-assist.exe` file from the [Releases](https://github.com/<your-username>/jimwas-gemini-assistant/releases) page.
- **Double-click** to run—no need to install Python or dependencies.
- Enter your Google Gemini API key when prompted, and the tool is ready to assist!

The `.exe` is portable and works on any Windows 10/11 (64-bit) machine, bundling all necessary dependencies for a seamless experience.

---

## **Features**

- **Automated Screenshot Capture**: Captures your screen at customizable intervals (default: 120 seconds, minimum 10 seconds).
- **Google Gemini AI Integration**: Sends screenshots with a configurable prompt (default: `"answer this question?"`) to the Gemini API for real-time analysis and responses.
- **Remote Desktop Compatibility**: Run on a secondary computer using remote desktop software (e.g., [VNC](https://www.realvnc.com), [NoMachine](https://www.nomachine.com), [Windows RDP](https://learn.microsoft.com/en-us/windows-server/remote/remote-desktop-services/welcome-to-rds)) to monitor your primary exam-taking computer’s screen without detection by proctoring software.
- **User-Friendly GUI**: Built with `tkinter`, featuring start/stop controls, interval settings, and a scrollable output window for AI responses.
- **Secure API Key Input**: Prompts for your Gemini API key at runtime via a secure dialog box, avoiding hardcoding or environment variables.
- **Cross-Platform Support**: Source code runs on Windows and macOS, with the demo `.exe` tailored for Windows.
- **Error Handling**: Robust handling for API and network issues, with detailed error messages displayed in the GUI and console for debugging.

---

## **Use Case**

This tool is perfect for simulating AI assistance during **practice exams or mock interviews**. By running the assistant on a secondary computer connected via remote desktop to your exam-taking machine, you can receive real-time AI-generated answers to questions displayed on your screen. Examples include:

- **Technical Interviews**: Analyze coding problems, algorithms, or whiteboard questions in real-time.
- **Online Exams**: Get AI responses to practice questions during mock exams to enhance learning.
- **Educational Aid**: Understand how Gemini AI interprets and answers complex questions during preparation sessions.

> **Important**: To avoid detection by proctoring software (e.g., ProctorU, ExamSoft), always run this tool on a **separate computer**, not the exam-taking machine. Use remote desktop software to mirror the exam screen to the secondary computer.

---

## **Requirements**

### **Demo Version (.exe)**

- Windows 10/11 (64-bit)
- Google Gemini API key ([get one here](https://aistudio.google.com/app/apikey))
- Remote desktop software (e.g., [VNC](https://www.realvnc.com), [NoMachine](https://www.nomachine.com), [Windows RDP](https://learn.microsoft.com/en-us/windows-server/remote/remote-desktop-services/welcome-to-rds))
- No Python or dependencies required—the `.exe` is self-contained

### **Source Code**

- Python 3.9 or higher
- Windows 10/11 or macOS 10.15+
- Google Gemini API key
- Remote desktop software (as above)
- Python dependencies:
  ```bash
  pip install google-generativeai pyautogui pillow
