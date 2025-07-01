# Real Estate Asset Assistant

A conversational AI assistant for real estate asset management, powered by Google Gemini and LangChain. The assistant analyzes a dataset of real estate assets and generates responses with relevant data, insights, and summaries.

---

## Features
- Conversational interface for real estate asset management
- Automatic SQL query generation and execution on a local database
- Data analysis and executive summaries

---

## Architecture
- **Frontend:** Streamlit app (`ui`) for chat-based interaction
- **Backend:** FastAPI app (`main.py`) exposes a `/chat` endpoint
- **Agent:** LangChain agent (`app/agent`) with tools for SQL database interaction based on Google Gemini model
- **Database:** SQLite database (`app/db`) generated from a Parquet file (`app/db/cortex.parquet`)
- **Shared:** Common constants and DTOs in `shared/`

---

## Prerequisites
- Python 3.9+
- Google Gemini API Key ([get one here](https://aistudio.google.com/app/apikey))

---

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ArzhkvJl/real-estate-agent <my-folder>
   cd <my-folder>
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## Run Applications

1. **Run the FastAPI backend:**
   ```bash
   python main.py
   ```
2. **In a separate terminal, run the Streamlit UI:**
   ```bash
   cd frontend
   streamlit run ui.py
   ```
3. **Open a browser and navigate to the link from the terminal.**

---

## API Documentation

- The API documentation is available at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) when the backend is running.
- Main endpoint:
  - `POST /chat` — Accepts a list of message strings and a Gemini API key, returns the assistant's response.

---

## Project Structure

```
real-estate-agent/
├── app/
│   ├── agent/         # Agent logic and tools
│   ├── db/            # Database and data files
│   ├── llm/           # LLM integration (Gemini)
├── shared/            # Shared constants and DTOs
├── frontend/          # Streamlit UI
├── main.py            # FastAPI backend
├── requirements.txt   # Python dependencies
```

---
## Model and frameworks choices

_Python_ is considered the best programming language for AI development due to its ease of use, large ecosystem of libraries and frameworks, and strong community support.

_Google Gemini models_ are specifically designed as reasoning models. This means they can think internally about problems and generate intermediate steps before providing a final answer. This capability is critical for real estate asset management, where decisions often require multi-step analysis.
Gemini models have a high ability to extract specific information from unstructured text, which is invaluable for processing leases, contracts, market reports, and other real estate documents.
The Gemini family of models is the availability of a free tier for the Gemini API. Even the free tier provides access to powerful models with reasonable token limits that are sufficient for significant development.

_LangChain_ allows you to efficiently build applications on top of large language models. It is ideal for connecting LLM to databases to extract information and making answers more accurate. There are some developed tool to work with SQL querues.

_LangGraph_ is required for more complex and non-linear processes. Graph representation of logic allows the application to share the data between tolls and show the user only the final answer.

---

## Main challenges
1. **Data Gaps & Schema Mismatch**

A single table (cortex) contained rental and maintenance logs, but did not contain asset-level fields such as address, market_value, or purchase_price.
User queries (e.g., "Compare the price of assets on 123 Main St and 456 Oak Ave") could not be satisfied from the existing schema.

_Solution_:

Graceful system prompt 

2. **Agent architecture and tool development**

It was necessary to develop an application flow that would analyze the database, not raw numerical data from the user.

_Solution_:

To do this, the agent's work scheme should represent:

Analysis of the database schema → Creating an SQL query → Checking the correctness of the query → Execution → Summarizing

Therefore, the agent compares the user's request with the database schema, extracts the necessary information and generates a report.