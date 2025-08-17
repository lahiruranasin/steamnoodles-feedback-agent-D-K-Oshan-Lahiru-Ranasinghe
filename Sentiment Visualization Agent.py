import os
import time
from datetime import datetime
from dotenv import load_dotenv
import tkinter as tk
from tkinter import messagebox, scrolledtext
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from reportlab.platypus import SimpleDocTemplate, Image, Spacer
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch

from langchain.agents import initialize_agent, AgentType
from langchain.tools import Tool
from langchain_openai import ChatOpenAI

# -------------------------------------------------
# 🔐 Load Environment
# -------------------------------------------------
load_dotenv(r"E:\Agent X\agent2.env")  # Contains OPENROUTER_API_KEY
api_key = os.getenv("OPENROUTER_API_KEY")

# -------------------------------------------------
# 📅 Current Date
# -------------------------------------------------
current_date = time.strftime("%Y-%m-%d")
print("Local date:", current_date)

# -------------------------------------------------
# 🤖 Initialize LLM
# -------------------------------------------------
llm = ChatOpenAI(
    model="nousresearch/deephermes-3-llama-3-8b-preview:free",
    temperature=0,
    openai_api_base="https://openrouter.ai/api/v1",
    openai_api_key=api_key,
)

VERBOSE = False

# -------------------------------------------------
# 🛠 Tool Definition (placeholder)
# -------------------------------------------------
def comment_on_prompt(prompt: str) -> str:
    return f"Here's a comment on the prompt: \"{prompt}\""

plotting_tool = Tool(
    name="Plotting_Agent",
    func=comment_on_prompt,
    description="Use this tool to analyze user prompt and get inputs."
)

# -------------------------------------------------
# 🤝 Agent Initialization
# -------------------------------------------------
agent = initialize_agent(
    tools=[plotting_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=VERBOSE
)

# -------------------------------------------------
# 🧩 Parser Utility
# -------------------------------------------------
def process_agent_result(result_text: str) -> dict:
    data = {}
    for line in result_text.splitlines():
        if "=" in line:
            key, value = line.split("=", 1)
            data[key.strip()] = value.strip()
    return data

def extract_date_columns(prompt: str) -> dict:
    raw_output = agent.run(
        f"""
        The current date is {current_date}.
        Identify the date range and columns the user wants from this prompt: '{prompt}'.
        If not mentioned, set date range to last month and columns to all columns.
        Respond ONLY in the following exact format with no extra words:
        start_date=YYYY-MM-DD
        end_date=YYYY-MM-DD
        columns=<comma-separated column names>
        """
    )
    return process_agent_result(raw_output)

# -------------------------------------------------
#Visualization + PDF Export
# -------------------------------------------------
def plot_results(start_date, end_date, columns):
    csv_file = r"E:\Agent X\prompt_dataset.csv"

    if not os.path.exists(csv_file):
        messagebox.showerror("Error", f"CSV file not found: {csv_file}")
        return

    df = pd.read_csv(csv_file)

    if 'date' not in df.columns or 'sentiment' not in df.columns:
        messagebox.showerror("Error", "CSV must contain 'date' and 'sentiment' columns.")
        return

    # Convert date & sentiment
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    mapping = {"positive": 1, "neutral": 0, "negative": -1}
    df["sentiment_numeric"] = df["sentiment"].map(mapping).fillna(0)

    # Filter by date range
    mask = (df['date'] >= pd.to_datetime(start_date)) & (df['date'] <= pd.to_datetime(end_date))
    filtered_df = df.loc[mask]

    if filtered_df.empty:
        messagebox.showinfo("No Data", "No records found for the selected date range.")
        return

    sns.set(style="whitegrid")
    fig, axes = plt.subplots(2, 3, figsize=(20, 10))
    axes = axes.flatten()

    # Line Chart
    sns.lineplot(data=filtered_df, x="date", y="sentiment_numeric", ax=axes[0], marker="o")
    axes[0].set_title("Sentiment Over Time")
    axes[0].set_ylabel("Sentiment (-1/0/1)")

    #  Pie Chart
    sentiment_counts = filtered_df["sentiment"].value_counts()
    axes[1].pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', startangle=90)
    axes[1].set_title("Sentiment Distribution")

    # Bar Chart
    sns.barplot(x=sentiment_counts.index, y=sentiment_counts.values, ax=axes[2])
    axes[2].set_title("Sentiment Counts")
    axes[2].set_ylabel("Count")

    #  Stacked Area
    stacked = filtered_df.groupby(["date", "sentiment"]).size().unstack(fill_value=0)
    stacked.plot.area(ax=axes[3], alpha=0.6)
    axes[3].set_title("Sentiment Stacked Over Time")

    
    fig.tight_layout()
    fig.autofmt_xdate()

    # Save chart & PDF
    chart_path = r"E:\Agent X\sentiment_charts.png"
    fig.savefig(chart_path, dpi=300)

    pdf_path = r"E:\Agent X\sentiment_report.pdf"
    doc = SimpleDocTemplate(pdf_path, pagesize=A4)
    elements = [Image(chart_path, width=6*inch, height=4*inch), Spacer(1, 0.5*inch)]
    doc.build(elements)

    # Show in Tkinter
    for widget in chart_frame.winfo_children():
        widget.destroy()
    canvas = FigureCanvasTkAgg(fig, master=chart_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    messagebox.showinfo("Success", f"Charts saved and exported to PDF:\n{pdf_path}")

# -------------------------------------------------
#  Submit prompt
# -------------------------------------------------
def submit_prompt():
    prompt = prompt_input.get("1.0", tk.END).strip()
    if not prompt:
        messagebox.showwarning("Input Error", "Please enter prompt before submitting.")
        return

    parsed = extract_date_columns(prompt)
    start_date = parsed.get("start_date")
    end_date = parsed.get("end_date")
    columns = parsed.get("columns")

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    output_text.config(state=tk.NORMAL)
    output_text.insert(tk.END, f"Timestamp: {timestamp}\n")
    output_text.insert(tk.END, f"start_date={start_date}\n")
    output_text.insert(tk.END, f"end_date={end_date}\n")
    output_text.insert(tk.END, "-" * 50 + "\n")
    output_text.config(state=tk.DISABLED)

    plot_results(start_date, end_date, columns)
    prompt_input.delete("1.0", tk.END)

# -------------------------------------------------
# Tkinter UI
# -------------------------------------------------
root = tk.Tk()
root.title("SteamNoodles - Sentiment Plotting Agent ")

tk.Label(root, text="Enter Prompt:").pack(anchor="w", padx=10, pady=5)
prompt_input = scrolledtext.ScrolledText(root, width=70, height=5)
prompt_input.pack(padx=10, pady=5)

submit_btn = tk.Button(root, text="Enter", command=submit_prompt)
submit_btn.pack(pady=10)

tk.Label(root, text="Agent Response:").pack(anchor="w", padx=10, pady=5)
output_text = scrolledtext.ScrolledText(root, width=70, height=10, state=tk.DISABLED)
output_text.pack(padx=10, pady=5)

chart_frame = tk.Frame(root)
chart_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

root.mainloop()
