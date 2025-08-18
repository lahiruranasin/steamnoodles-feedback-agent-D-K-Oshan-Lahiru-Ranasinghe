# Name - D K Oshan Lahiru Ranasinghe
# University - NSBM Green University
# Year - Second Year
# Project Title -  Automated Restaurant Feedback Agent – SteamNoodles
# Event - Agent X by Leo Club of University of Moratuwa (2025)

# 🍜 SteamNoodles Feedback Agent  

An AI-powered **multi-agent system** for automating restaurant customer feedback analysis and visualization, built for the **SteamNoodles** restaurant chain.  

This project implements **two agents** using LLMs (Groq + OpenRouter), LangChain, and Python visualization libraries:  

1. **Feedback Response Agent**   
   - Accepts customer feedback via a Tkinter GUI.  
   - Detects sentiment (Positive, Negative, Neutral).  
   - Generates professional automated replies.  
   - Saves data into a CSV file.  

2. **Sentiment Visualization Agent**   
   - Accepts user prompts with **date ranges**.  
   - Uses LLMs to parse the prompt.  
   - Reads stored feedback data.  
   - Generates charts (line, pie, bar, stacked area).  
   - Exports results as PNG and PDF reports.  

---

##  Tools & Technologies  

- **Frameworks**: LangChain, LlamaIndex (optional)  
- **LLMs**: Groq (`llama3-70b-8192`), OpenRouter (`deephermes-3-llama-3-8b-preview`)  
- **Python Libraries**:  
  - NLP/AI: `langchain`, `langchain_groq`, `langchain_openai`  
  - Data: `pandas`, `csv`, `dotenv`  
  - Visualization: `matplotlib`, `seaborn`  
  - GUI: `tkinter`  
  - Reporting: `reportlab`


## ⚙️ Setup Instructions  
```bash
1️⃣ Clone Repository  

git clone https://github.com/[your-username]/steamnoodles-feedback-agent-[your-name].git
cd steamnoodles-feedback-agent-[your-name]
2️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
If requirements.txt doesn’t exist, create one with:

txt
Copy
Edit
langchain
langchain-community
langchain-openai
langchain-groq
python-dotenv
pandas
matplotlib
seaborn
reportlab
tk
3️⃣ Setup Environment Variables
Create a file agent2.env with your API keys:

ini
Copy
Edit
OPENROUTER_API_KEY=sk-your-openrouter-key
GROQ_API_KEY=gsk-your-groq-key
4️⃣ Verify Installation
python
Copy
Edit
import os
from dotenv import load_dotenv

load_dotenv("agent2.env")
print(os.getenv("OPENROUTER_API_KEY"))
print(os.getenv("GROQ_API_KEY"))

How to Test Each Agent
1. Feedback Response Agent
python feedback_response_agent.py
Steps:
Enter a review in the Tkinter input box.
Click Submit Feedback.
The system will:
  Detect sentiment
  Generate an AI response
  Save results into feedback_dataset.csv

Example Output (GUI + CSV):
Timestamp: 2025-08-17 12:30:45
Sentiment: Positive
Agent Response: Thank you for your kind words! We’re glad you enjoyed your experience.
2. Sentiment Visualization Agent
python sentiment_visualization_agent.py
Steps:
Enter a prompt with a date range. Example:
 Show sentiment analysis from August 1 to August 15
Click Enter.
The system will:
 Parse the date range
 Filter prompt_dataset.csv
 Generate charts (line, pie, bar, stacked area)
 Display them in Tkinter
 Export sentiment_charts.png and sentiment_report.pdf

Example Output:
 Charts displayed in GUI
 sentiment_charts.png saved
 sentiment_report.pdf exported

Changing File Locations
Update all hardcoded file paths (CSV, ENV, PDF, PNG) in the scripts from E:\Agent X\... to match the correct folder locations on your own computer.
```
# UI and Output plots
# Feedback Response Agent
Feedback Response Agent UI

<img width="753" height="599" alt="Screenshot 2025-08-17 231507" src="https://github.com/user-attachments/assets/54fd713a-b089-48dc-b000-72839c257418" />

Popup Message to inform csv update

<img width="1077" height="608" alt="Screenshot 2025-08-17 231536" src="https://github.com/user-attachments/assets/bc1ee630-f20d-46c0-8565-fa08e9c32905" />

Agent respone and sentiment

<img width="747" height="602" alt="Screenshot 2025-08-18 142532" src="https://github.com/user-attachments/assets/54ece4f4-2100-40ab-ad6c-ec83952cf621" />

Updated row(csv file)

<img width="487" height="307" alt="Screenshot 2025-08-18 143134" src="https://github.com/user-attachments/assets/585f5e36-4062-4921-92cd-81db947d1bbe" />




# Sentiment Visualization Agent
Sentiment Visualization Agent UI

<img width="751" height="528" alt="Screenshot 2025-08-17 231220" src="https://github.com/user-attachments/assets/e6a3b798-abb5-4163-af27-def8d0a8a475" />

Visualization of plots(Figure 1)

<img width="1919" height="1015" alt="Screenshot 2025-08-18 145432" src="https://github.com/user-attachments/assets/0353fb9a-0877-4ceb-8ea6-03490fa94979" />


Popup Message of exported pdf

<img width="329" height="181" alt="Screenshot 2025-08-17 231317" src="https://github.com/user-attachments/assets/ff77be8d-d378-4d28-a6f2-53311adb0ec5" />

Agent response Timestamp and date range

<img width="1919" height="1019" alt="Screenshot 2025-08-18 145454" src="https://github.com/user-attachments/assets/fd538ec1-4d9b-4044-8a49-df5f7fb7088e" />


Exported PDF and png files of figure 1

<img width="781" height="68" alt="Screenshot 2025-08-17 231359" src="https://github.com/user-attachments/assets/5dd36b66-9eb3-41a2-b356-fd32e59a6b6e" />

PNG File

<img width="1919" height="1018" alt="Screenshot 2025-08-18 145517" src="https://github.com/user-attachments/assets/575d9704-da0a-41d6-96e3-f915126fb95e" />

PDF File

<img width="1919" height="1010" alt="Screenshot 2025-08-18 145534" src="https://github.com/user-attachments/assets/85fac13e-75dd-464d-b7ac-4c4b194fd66d" />



