# AI Research Paper Summarizer

An interactive, notebook-based tool that helps users quickly understand the latest AI research papers from arXiv.

## Prerequisites

Before running the notebook, ensure the following are installed and configured:

- **Python 3.10+**
- **Jupyter Notebook or JupyterLab**
- **Ollama** installed and running locally
- A locally available Ollama model (e.g., `llama3.2`)
- **Playwright** with Chromium installed
- Required Python packages:
  - `playwright`
  - `openai`
  - `ipywidgets`
  - `IPython`
  - `markdown` (optional, for rendering)

### Setup

```bash
# Install Python dependencies
pip install playwright openai ipywidgets markdown

# Install Chromium for Playwright
playwright install chromium

# Start Ollama
ollama serve

# Pull the model (run once)
ollama pull llama3.2
````

## Features

* Scrapes the latest papers from the `cs.AI` category on arXiv
* Displays a numbered list of available research papers
* Allows users to select a paper of interest interactively
* Generates a structured, easy-to-read summary using a local Ollama LLM
* Produces approximately 500-word Markdown summaries covering:

  * Overview
  * Problem Statement
  * Proposed Approach
  * Key Contributions
  * Results and Findings
  * Limitations
  * Potential Applications
  * Takeaways
* Renders summaries directly within the Jupyter Notebook
* Optionally saves summaries as Markdown (`.md`) files for future reference

## Goal

Bridge the gap between complex academic research and quick comprehension by enabling users to explore and understand cutting-edge AI papers in minutes rather than hours.
