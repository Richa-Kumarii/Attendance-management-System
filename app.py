import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

# Load project settings from .env
load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")
HF_MODEL_ID = os.getenv("HF_MODEL_ID")

if not HF_TOKEN:
    raise RuntimeError("HF_TOKEN .env file mein nahi mila.")

if not HF_MODEL_ID:
    raise RuntimeError("HF_MODEL_ID .env file mein nahi mila.")

client = InferenceClient(
    model=HF_MODEL_ID,
    provider="novita",
    token=HF_TOKEN,
)

def ask_attendance_ai(command: str) -> str:
    """Ask the model to interpret an attendance-related command."""
    response = client.chat_completion(
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an assistant for a student attendance system. "
                    "Understand attendance-related commands. Do not invent "
                    "student records or claim that attendance was changed. "
                    "Reply briefly in plain text."
                ),
            },
            {"role": "user", "content": command},
        ],
        max_tokens=150,
    )

    return response.choices[0].message.content or ""


if __name__ == "__main__":
    print("Attendance AI test")
    command = input("Enter your attendance question: ")

    try:
        answer = ask_attendance_ai(command)
        print("\nAI response:", answer)
    except Exception as error:
      print("\nRequest failed.")
      print("Error type:", type(error).__name__)
      print("Details:", str(error))