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
