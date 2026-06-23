# AI Research Paper Summarizer

An interactive tool that helps users quickly understand the latest AI research papers from arXiv by generating structured summaries using a locally running Ollama model.

## Features

- Scrapes the latest papers from the `cs.AI` category on arXiv
- Displays a numbered list of available research papers
- Allows users to select a paper of interest interactively
- Generates structured, easy-to-read summaries using a local Ollama LLM
- Produces approximately 500-word Markdown summaries covering:
  - Overview
  - Problem Statement
  - Proposed Approach
  - Key Contributions
  - Results and Findings
  - Limitations
  - Potential Applications
  - Takeaways
- Saves summaries as Markdown (`.md`) files for future reference
- Supports both:
  - Command-line interface (CLI)
  - Jupyter Notebook workflow

---

## Project Structure

```text
ai-research-paper-summarizer/
├── pyproject.toml
├── README.md
├── src/
│   └── ai_research_summarizer/
│       ├── cli.py
│       ├── config.py
│       ├── models.py
│       ├── prompts.py
│       ├── scraper.py
│       ├── summarizer.py
│       └── utils.py
├── notebooks/
│   └── ai_research_summarizer.ipynb
├── summaries/
└── tests/
````

---

## Prerequisites

Before running the application, ensure the following are installed:

* Python 3.11+
* uv
* Ollama
* Chromium browser for Playwright

---

## Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd ai-research-paper-summarizer
```

### 2. Install dependencies

```bash
uv sync
```

### 3. Install Playwright browsers

```bash
uv run playwright install chromium
```

### 4. Start Ollama

```bash
ollama serve
```

### 5. Pull the required model

```bash
ollama pull llama3.2
```

---

## Running the Application

### Option 1: Run as a CLI Application

Start the summarizer:

```bash
uv run paper-summarizer
```

Example:

```text
Recent AI Papers

1. Paper A
2. Paper B
3. Paper C

Choose paper number: 2
```

The application will:

1. Fetch recent AI papers from arXiv
2. Display the available papers
3. Prompt you to select a paper
4. Retrieve the paper's metadata
5. Generate a structured summary using Ollama
6. Save the summary in the `summaries/` directory

---

### Option 2: Run the Jupyter Notebook

Launch Jupyter:

```bash
uv run jupyter lab
```

or

```bash
uv run jupyter notebook
```

Open:

```text
notebooks/ai_research_summarizer.ipynb
```

The notebook provides an interactive workflow for:

* Exploring recent papers
* Selecting papers using widgets
* Generating summaries
* Rendering Markdown summaries directly inside the notebook
* Saving summaries as `.md` files

---

## Output

Generated summaries are saved under:

```text
summaries/
├── Efficient_Planning_With_LLMs.md
├── Multi_Agent_Memory_Systems.md
└── ...
```

---

## Technologies Used

* Python
* uv
* Playwright
* arXiv
* Ollama
* OpenAI Python SDK
* JupyterLab
* ipywidgets

---

## Goal

Bridge the gap between complex academic research and quick comprehension by enabling users to explore and understand cutting-edge AI papers in minutes rather than hours.
