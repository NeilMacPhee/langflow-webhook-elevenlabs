from fastapi import FastAPI, Request
import httpx
import uvicorn
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

# Get LangFlow API URLs from environment variables
LANGFLOW_URL = os.getenv("LANGFLOW_URL")
LANGFLOW_URL_EMAIL = os.getenv("LANGFLOW_URL_EMAIL")
LANGFLOW_URL_DOC = os.getenv("LANGFLOW_URL_DOC")

@app.get("/")
async def root():
    return {"message": "Webhook tool is running."}


@app.post("/runLangFlow")
async def run_langflow(request: Request):
    try:
        user_data = await request.json()
        user_input = user_data.get("input", "Hello!")# Default fallback

        async with httpx.AsyncClient() as client:
            response = await client.post(
                LANGFLOW_URL,
                json={"input_value": user_input},
                headers={"Content-Type": "application/json"},
                timeout=15  # Adjust as needed
            )

        response.raise_for_status()
        langflow_result = response.json()

        print("LangFlow Result:", langflow_result)

        # Adapt depending on LangFlow's actual output format
        output_text = langflow_result["outputs"][0]["outputs"][0]["results"][
            "message"]["text"]
        #output_text = langflow_result["outputs"]["response"]["message"]

        return {"result": output_text}

    except Exception as e:
        return {"result": f"Error: {str(e)}"}

@app.post("/runLangFlowEmail")
async def run_langflow_email(request: Request):
    try:
        user_data = await request.json()
        user_input = user_data.get("input", "Hello!")  # Default fallback

        async with httpx.AsyncClient() as client:
            response = await client.post(
                LANGFLOW_URL_EMAIL,
                json={"input_value": user_input},
                headers={"Content-Type": "application/json"},
                timeout=15  # Adjust as needed
            )

        response.raise_for_status()
        langflow_result = response.json()
        print("Response:", response.json())
        print("LangFlow Result:", langflow_result)

        # Adapt depending on LangFlow's actual output format
        output_text = langflow_result["outputs"][0]["outputs"][0]["results"][
            "message"]["text"]
        #output_text = langflow_result["outputs"]["response"]["message"]

        return {"result": output_text}

    except Exception as e:
        return {"result": f"Error: {str(e)}"}

@app.post("/runLangFlowDoc")
async def run_langflow_doc(request: Request):
    try:
        user_data = await request.json()
        user_input = user_data.get("input", "Hello!")  # Default fallback

        async with httpx.AsyncClient() as client:
            response = await client.post(
                LANGFLOW_URL_DOC,
                json={"input_value": user_input},
                headers={"Content-Type": "application/json"},
                timeout=15  # Adjust as needed
            )

        response.raise_for_status()
        langflow_result = response.json()

        print("LangFlow Result:", langflow_result)

        # Adapt depending on LangFlow's actual output format
        output_text = langflow_result["outputs"][0]["outputs"][0]["results"][
            "message"]["text"]
        #output_text = langflow_result["outputs"]["response"]["message"]

        return {"result": output_text}

    except Exception as e:
        return {"result": f"Error: {str(e)}"}

@app.post("/runTest")
async def run_test(request: Request):
    try:
        user_data = await request.json()
        user_input = user_data.get("input", "Hello!")  # Default fallback

        print("User Data:", user_data)
        print("User Input:", user_input)

        #

        return {"result": user_data}

    except Exception as e:
        return {"result": f"Error: {str(e)}"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}