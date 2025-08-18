GROQ_API_KEY = "YOUR_GROQ_API_KEY"

import os
from dotenv import load_dotenv
import tkinter as tk
from tkinter import messagebox, scrolledtext
from langchain.agents import initialize_agent, AgentType
from langchain.tools import Tool
from langchain_groq import ChatGroq
from datetime import datetime
import csv
import threading
import string

# Load environment variables
os.environ["GROQ_API_KEY"] = GROQ_API_KEY
load_dotenv()

# Initialize LLM
llm = ChatGroq(model="llama3-70b-8192", temperature=0)

VERBOSE = False

# Custom function to analyze feedback
def comment_on_feedback(feedback: str) -> str:
    return f"Here's a comment on the feedback: \"{feedback}\""

# Wrap it in a LangChain Tool
feedback_tool = Tool(
    name="FeedbackCommenter",
    func=comment_on_feedback,
    description="Use this tool to analyze and comment on customer feedback about restaurant."
)

# Initialize Agent
agent = initialize_agent(
    tools=[feedback_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=VERBOSE
)

# LLM-powered sentiment detection with fallback
def detect_sentiment(feedback: str):
    """Detect sentiment using Groq LLM with fallback to keyword logic."""
    try:
        sentiment_prompt = f"""
        Classify the following restaurant customer feedback into one of:
        Positive, Negative, or Neutral.
        Only respond with one word.

        Feedback: "{feedback}"
        Sentiment:
        """
        sentiment_result = llm.invoke(sentiment_prompt).content.strip()
        sentiment_result = sentiment_result.split()[0].capitalize()

        if sentiment_result in ["positive", "negative", "neutral"]:
            return sentiment_result
    except Exception as e:
        print(f"[Warning] LLM sentiment failed, falling back to keywords. Error: {e}")

    # Fallback keyword method
    positive_keywords = ["delicious", "tasty", "amazing", "fantastic", "excellent", "good",
                         "great", "friendly", "wonderful", "perfect", "love", "loved", "fresh",
                         "best", "nice", "pleasant", "enjoyed", "happy", "satisfied"]
    negative_keywords = ["bad", "awful", "terrible", "horrible", "worst", "cold", "stale", 
                         "slow", "rude", "disgusting", "overpriced", "not fresh", "dirty",
                         "unfriendly", "unsatisfied", "poor", "bland", "tasteless", "smelly"]

    feedback_lower = feedback.lower().translate(str.maketrans('', '', string.punctuation))
    has_positive = any(word in feedback_lower for word in positive_keywords)
    has_negative = any(word in feedback_lower for word in negative_keywords)

    if has_positive and not has_negative:
        return "positive"
    elif has_negative and not has_positive:
        return "negative"
    else:
        return "neutral"

# CSV file path
csv_file = r"E:\Agent X\feedback_dataset.csv"

# GUI submit function with threading
def submit_feedback_thread():
    feedback = feedback_input.get("1.0", tk.END).strip()
    if not feedback:
        messagebox.showwarning("Input Error", "Please enter feedback before submitting.")
        return

    def process_feedback():
        sentiment = detect_sentiment(feedback)
        agent_comment = agent.run(f"Please comment professionally on this customer feedback: '{feedback}'")
        date_today = datetime.now().strftime("%#m/%#d/%Y")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Save to CSV
        with open(csv_file, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            if file.tell() == 0:
                writer.writerow(["Date", "Feedback", "Sentiment"])
            writer.writerow([date_today, feedback, sentiment])

        # Show results in GUI
        output_text.config(state=tk.NORMAL)
        output_text.insert(tk.END, f"Timestamp: {timestamp}\n")
        output_text.insert(tk.END, f"Sentiment: {sentiment}\n")
        output_text.insert(tk.END, f"Agent Response: {agent_comment}\n")
        output_text.insert(tk.END, "-"*50 + "\n")
        output_text.config(state=tk.DISABLED)

        feedback_input.delete("1.0", tk.END)
        messagebox.showinfo("Success", "Feedback submitted and saved to CSV!")

    threading.Thread(target=process_feedback).start()

# Tkinter window
root = tk.Tk()
root.title("SteamNoodles - Customer Feedback Response Agent")

# Feedback input
tk.Label(root, text="Enter Customer Feedback:").pack(anchor="w", padx=10, pady=5)
feedback_input = scrolledtext.ScrolledText(root, width=70, height=5)
feedback_input.pack(padx=10, pady=5)

# Submit button
submit_btn = tk.Button(root, text="Submit Feedback", command=submit_feedback_thread)
submit_btn.pack(pady=10)

# Output area
tk.Label(root, text="Agent Response:").pack(anchor="w", padx=10, pady=5)
output_text = scrolledtext.ScrolledText(root, width=70, height=15, state=tk.DISABLED)
output_text.pack(padx=10, pady=5)

root.mainloop()


