# Name - D K Oshan Lahiru Ranasinghe
# University - NSBM Green University
# Year - Second Year
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
Popup Message to inform cvs update
<img width="1077" height="608" alt="Screenshot 2025-08-17 231536" src="https://github.com/user-attachments/assets/bc1ee630-f20d-46c0-8565-fa08e9c32905" />
Agent respone and sentiment
<img width="714" height="203" alt="Screenshot 2025-08-17 231548" src="https://github.com/user-attachments/assets/e59660ed-ab2d-42dc-9125-1529fb7bef0f" />
Updated dataset(csv file)
<img width="1919" height="1018" alt="Screenshot 2025-08-17 231631" src="https://github.com/user-attachments/assets/32d4e166-1c36-4b72-962c-adfec3e13809" />
Updated row
<img width="367" height="21" alt="Screenshot 2025-08-17 231637" src="https://github.com/user-attachments/assets/9114b54c-d165-4357-924c-669e9a43c62f" />



# Sentiment Visualization Agent
Sentiment Visualization Agent UI
<img width="751" height="528" alt="Screenshot 2025-08-17 231220" src="https://github.com/user-attachments/assets/e6a3b798-abb5-4163-af27-def8d0a8a475" />
Visualization of plots(Figure 1)
<img width="1919" height="1019" alt="Screenshot 2025-08-17 231259" src="https://github.com/user-attachments/assets/254c170e-a38b-46ae-8ad5-0e4f6b0683df" />
Popup Message of exported pdf
<img width="329" height="181" alt="Screenshot 2025-08-17 231317" src="https://github.com/user-attachments/assets/ff77be8d-d378-4d28-a6f2-53311adb0ec5" />
Agent response Timestamp and date range
<img width="1919" height="1014" alt="Screenshot 2025-08-17 231341" src="https://github.com/user-attachments/assets/a0f0ce3f-605b-4672-839c-9c6d0e2a9694" />
Exported PDF and png files of figure 1
<img width="781" height="68" alt="Screenshot 2025-08-17 231359" src="https://github.com/user-attachments/assets/5dd36b66-9eb3-41a2-b356-fd32e59a6b6e" />
PNG File
<img width="1916" height="1017" alt="Screenshot 2025-08-17 231411" src="https://github.com/user-attachments/assets/04ba39e5-d3e8-4912-b067-8c02d03dd4a8" />
PDF File
<img width="1919" height="1021" alt="Screenshot 2025-08-17 231424" src="https://github.com/user-attachments/assets/88bef290-1c03-4037-ac2e-c20b5400f6dd" />


