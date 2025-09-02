JimWas Gemini Screenshot AssistantJimWas Gemini Screenshot Assistant is a Python-based tool that leverages the Google Gemini AI (gemini-1.5-flash model) to assist with answering questions during online interviews or exams. 

The application captures screenshots of your screen at user-defined intervals, sends them to the Gemini AI for analysis, and displays real-time responses in a user-friendly GUI. 

By running this tool on a secondary computer via remote desktop, you can connect to your primary exam-taking machine, allowing Gemini AI to analyze and answer questions displayed on your screen. Ethical Note: This tool is intended for educational and demonstration purposes only. Using it to gain an unfair advantage in exams or interviews may violate academic integrity or professional ethics policies. Always ensure compliance with relevant guidelines.

FeaturesAutomated Screenshot Capture: Captures your screen at customizable intervals (minimum 10 seconds).

Google Gemini AI Integration: Sends screenshots to the Gemini API to analyze and answer questions displayed on your screen.

Remote Desktop Compatibility: Run on a secondary computer using remote desktop software (e.g., TeamViewer, AnyDesk) to monitor and assist with exams on your primary machine.

User-Friendly GUI: Built with tkinter, featuring start/stop controls, interval settings, and a scrollable output window for AI responses.

Secure API Key Input: Prompts for your Gemini API key at runtime via a secure dialog box, avoiding hardcoding or environment variables.

Cross-Platform: Supports Windows and macOS, with instructions for creating a standalone .exe for Windows.

Use CaseThis tool is ideal for simulating AI assistance during practice exams or interviews. By connecting to your exam-taking computer via remote desktop from a secondary machine, the assistant captures and analyzes questions in real-time, providing answers to aid preparation or learning. 

Examples include:Technical Interviews: Analyze coding problems or whiteboard questions displayed on your screen.

Online Exams: Get AI-generated responses to questions in real-time during practice sessions.

Learning Aid: Use during mock exams to understand how Gemini AI interprets and answers complex questions.

Installation
Follow these steps to set up the JimWas Gemini Screenshot Assistant:Clone the Repository:bash

git clone https://github.com/<your-username>/jimwas-gemini-assistant.git
cd jimwas-gemini-assistant

Set Up a Virtual Environment:bash

python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

Install Dependencies:bash

pip install google-generativeai pyautogui pillow

Obtain a Gemini API Key:Sign up at Google Cloud Console.
Enable the Generative AI API and create an API key.

Run the Script:bash

python jimwas-assist.py

UsageSet Up Remote Desktop:Install remote desktop software (e.g., TeamViewer, AnyDesk) on both your primary (exam) and secondary (assistant) computers.
Connect from the secondary computer to the primary computer’s screen.

Launch the Assistant:Run jimwas-assist.py on the secondary computer.
Enter your Gemini API key when prompted in the secure dialog box.

Configure and Start:Set the screenshot interval (e.g., 120 seconds) in the GUI.
Click Start to begin capturing screenshots of the remote desktop session.
Gemini AI will analyze each screenshot and display responses in the GUI.

Stop and Exit:Click Stop to pause screenshot capture.
Close the GUI to exit the application.

Creating a Windows ExecutableTo distribute the tool as a standalone .exe for Windows:bash

pip install pyinstaller
pyinstaller --onefile --noconsole jimwas-assist.py

The executable will be in the dist/ folder, ready to run on any Windows machine without Python installed.RequirementsPython: 3.8 or higher
Operating System: Windows 10/11 (64-bit) or macOS 10.15+
Google Gemini API Key: Required for AI functionality
Remote Desktop Software: For cross-computer access (e.g., TeamViewer, AnyDesk)

TroubleshootingAPI Errors:Ensure your API key is valid and the Generative AI API is enabled in Google Cloud Console.
Update the google-generativeai library:bash

pip install --upgrade google-generativeai

Screenshot Permissions (macOS):Grant screen recording permissions in System Settings > Privacy & Security > Screen Recording.

Network Issues:If behind a proxy, configure environment variables:bash

# Windows
set HTTP_PROXY=http://your-proxy:port
set HTTPS_PROXY=https://your-proxy:port
# macOS/Linux
export HTTP_PROXY=http://your-proxy:port
export HTTPS_PROXY=https://your-proxy:port

LicenseMIT License (LICENSE) – Feel free to use, modify, and distribute, but adhere to ethical usage guidelines.DisclaimerThis tool is for educational purposes only. Misuse in official exams or interviews may violate academic or professional policies. Use responsibly and in compliance with all applicable rules.ContributingContributions are welcome! Please submit a pull request or open an issue for bug reports, feature requests, or improvements.

