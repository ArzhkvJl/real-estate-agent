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

