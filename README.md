
# Gemini LLM Streamlit Application

A simple AI question-and-answer application built with Python, Streamlit, and the Google Gemini API.

Users can enter a question through the Streamlit interface, submit it to the Gemini model, and view the generated response.

## Features

* Simple Streamlit web interface
* Integration with the Google Gemini API
* Secure API-key loading using environment variables
* Loading indicator while Gemini generates a response
* Input validation
* API error handling
* Responsive question-and-answer interface

## Technologies Used

* Python
* Streamlit
* Google GenAI SDK
* Google Gemini
* Python Dotenv

## Project Structure

```text
gemini-llm-app/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env
```

> The `.env` file contains your private API key and must not be committed to GitHub.

## Prerequisites

Before running the application, install:

* Python 3.10 or later
* pip
* A Google Gemini API key

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
cd YOUR-REPOSITORY
```

Replace `YOUR-USERNAME` and `YOUR-REPOSITORY` with your GitHub username and repository name.

### 2. Create a virtual environment

On Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

On macOS or Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install the dependencies

```bash
pip install -r requirements.txt
```

The `requirements.txt` file should contain:

```txt
streamlit
python-dotenv
google-genai
```

## API-Key Configuration

Create a file named `.env` in the project root:

```env
GEMINI_API_KEY=your_actual_api_key_here
```

Replace `your_actual_api_key_here` with your Gemini API key.

Never commit the `.env` file or expose your API key in application output, source control, screenshots, or documentation.

## Run the Application

Start the Streamlit application with:

```bash
streamlit run app.py
```

Streamlit will normally open the application in your browser at:

```text
http://localhost:8501
```

## How It Works

1. The application loads the Gemini API key from the `.env` file.
2. A Google GenAI client is created using the API key.
3. The user enters a question in the Streamlit interface.
4. The application sends the question to the Gemini model.
5. Gemini generates a response.
6. The response is displayed in the application.

## Example

Enter a question such as:

```text
What are the advantages of using microservices?
```

Select **Submit** to generate and display the Gemini response.

## Security

The Gemini API key must remain private.

Make sure `.gitignore` contains:

```gitignore
.env
.env.*
```

Before pushing the project to GitHub, verify that `.env` is not being tracked:

```bash
git status
```

If `.env` was previously committed, remove it from Git tracking:

```bash
git rm --cached .env
```

Then commit the change:

```bash
git commit -m "Remove environment file from source control"
```

You should also revoke and regenerate an API key that was previously committed or displayed publicly.

## Troubleshooting

### API key not found

Confirm that:

* The file is named `.env`
* The `.env` file is in the same project directory as `app.py`
* The variable is named `GEMINI_API_KEY`
* The virtual environment is active
* `python-dotenv` is installed

### Model not found

Model availability can change or depend on the API account and region. Update the model name in `app.py` to one that is available to your Gemini API project.

```python
response = client.models.generate_content(
    model="gemini-2.5-pro",
    contents=question,
)
```

### Quota exceeded

A quota error generally means that the project has exceeded its request, token, or billing limit. Review the Gemini API quota and billing configuration associated with the API key.

### Streamlit command not found

Install Streamlit:

```bash
pip install streamlit
```

Alternatively, run it through Python:

```bash
python -m streamlit run app.py
```

## Future Enhancements

Possible improvements include:

* Conversation history
* Streaming responses
* Model selection
* Adjustable temperature and token settings
* User authentication
* File upload and document analysis
* Chat-style interface
* Database storage for previous conversations
* Deployment to Streamlit Community Cloud

## License

This project is intended for learning and demonstration purposes.
