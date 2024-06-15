# LinkedIn Profile Summarizer

## Overview

The LinkedIn Profile Summarizer is a Python-based tool that scrapes detailed information from a LinkedIn profile and generates a comprehensive summary. This includes the person's work experience, technologies they have used, and interesting facts about them. It leverages the `langchain_openai` library to create human-like summaries using GPT models.

## Features

- **LinkedIn Profile Scraping**: Extracts detailed information from a LinkedIn profile.
- **Automated Summary Generation**: Creates summaries including work experience and technology stack.
- **Interesting Facts Extraction**: Identifies and presents interesting facts about the profile owner.

## Getting Started

### Prerequisites

- Python 3.7 or later
- LinkedIn account with access to view the desired profile
- OpenAI API key

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/linkedin-profile-summarizer.git
    cd linkedin-profile-summarizer
    ```

2. **Create a virtual environment** (optional but recommended):
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

3. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables**:
    Create a `.env` file in the root directory and add your OpenAI API key and any other required environment variables:
    ```plaintext
    OPENAI_API_KEY=your_openai_api_key_here
    ```

### Usage

1. **Edit the script**:
    - Open `main.py` and specify the LinkedIn profile URL you want to scrape.

2. **Run the script**:
    ```bash
    python main.py
    ```

3. **View the output**:
    The script will print the summary and details extracted from the LinkedIn profile.

## APIs Used

###  ProxyURL

- **Function**: `scrape_linkedin_profile`
- **Purpose**: Extracts information from a given LinkedIn profile.
- **Parameters**:
    - `linkedin_profile_url` (str): The URL of the LinkedIn profile to scrape.
    - `mock` (bool, optional): If set to `True`, returns mock data for testing purposes.

### OpenAI API

- **Library**: `langchain_openai`
- **Purpose**: Generates summaries and extracts information using GPT models.
- **Setup**:
    - Requires an OpenAI API key, which should be added to the `.env` file.



