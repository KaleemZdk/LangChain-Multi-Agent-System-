# LangChain Multi-Agent System

A research-oriented multi-agent AI application built with LangChain, Streamlit, and Google Gemini. The system combines web search, content extraction, report writing, and critique evaluation into a single workflow for automated research generation.

## Overview

This project demonstrates how multiple specialized agents can collaborate to perform a lightweight research pipeline:

- A search agent finds relevant sources online
- A reader agent retrieves and extracts readable content from a chosen source
- A writer agent synthesizes a structured research report
- A critic agent reviews the output and gives feedback

The application is designed as a simple, extensible demo for experimenting with multi-agent research workflows in Python.

## Features

- Multi-agent orchestration with LangChain
- Web search via Tavily
- Scraping and content extraction with requests, BeautifulSoup, readability-lxml, and trafilatura
- AI-powered writing and critique using Google Gemini
- Streamlit interface for easy interaction
- Lightweight, modular Python project structure

## Architecture

The system follows a four-step research flow:

1. Search Agent
   - Queries the web for relevant information related to a user topic.
2. Reader Agent
   - Selects the most relevant URL and extracts clean article text.
3. Writer Chain
   - Combines search results and scraped content into a structured report.
4. Critic Chain
   - Reviews the generated report and returns strengths, improvement areas, and a verdict.

A simplified view of the pipeline is:

```text
User Topic
   ↓
Search Agent → Web Search
   ↓
Reader Agent → Content Extraction
   ↓
Writer Chain → Research Report
   ↓
Critic Chain → Feedback
```

## Tech Stack

- Python 3.11
- LangChain
- LangChain Core
- LangChain Community
- Google Gemini (via langchain-google-genai)
- Tavily Search API
- Streamlit
- BeautifulSoup4
- readability-lxml
- trafilatura
- python-dotenv
- requests

## Project Structure

```text
LangChain-Multi-Agent-System-/
├── app.py                 # Streamlit UI
├── main.py                # Simple entry point for running the pipeline
├── requirements.txt       # Python dependencies
├── .env.example           # Optional environment template
├── LICENSE                # MIT License
├── README.md              # Project documentation
├── src/
│   ├── agents/
│   │   └── agents.py      # Agent and chain definitions
│   ├── pipelines/
│   │   └── pipeline.py    # Research workflow pipeline
│   └── tools/
│       └── tools.py       # Search and scraping utilities
└── .gitignore
```

## Installation

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd LangChain-Multi-Agent-System-
```

### 2. Create a virtual environment

Using conda:

```bash
conda create -n langagent python=3.11 -y
conda activate langagent
```

Or using Python venv:

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_google_gemini_api_key
TAVILY_API_KEY=your_tavily_api_key
```

> You need valid API keys for both Google Gemini and Tavily to run the research workflow successfully.

## Usage

### Run the Streamlit app

```bash
streamlit run app.py
```

Then open the local URL shown in the terminal and enter a topic to start the pipeline.

### Run the research pipeline directly

```bash
python main.py
```

This executes the pipeline for a default sample topic defined in the script.

## Example Workflow

1. Enter a research topic such as:
   - "Impact of AI on education"
   - "Renewable energy investment trends"
   - "Global semiconductor supply chain challenges"
2. The search agent fetches relevant sources.
3. The reader agent extracts readable content.
4. The writer agent compiles a structured report.
5. The critic agent provides a review and improvement suggestions.

## Limitations

- Research quality depends strongly on the quality of the chosen search results and API responses.
- The workflow is best suited for demo and prototyping use cases rather than production-scale research automation.
- Some websites may block automated scraping or require stricter compliance controls.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome. If you would like to improve the system, consider:

- Adding more agent roles and workflows
- Improving scraping reliability
- Supporting additional LLM providers
- Improving the UI and report formatting
- Adding evaluation metrics for response quality

## Acknowledgements

This project uses open-source libraries and APIs for web search, extraction, and LLM orchestration, including LangChain, Streamlit, Tavily, and Google Gemini.
