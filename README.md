AI-Based Attendance Management System

Overview

The AI-Based Attendance Management System is a Python-based application designed to simplify student attendance management using artificial intelligence. The goal is to make student records easier to manage, attendance easier to track, and attendance-related queries easier to handle.


Planned Features

- Student Record Management: Manage student details and records.
- Attendance Marking: Record and update daily attendance.
- Attendance Percentage: Calculate attendance percentages for individual students.
- Attendance Reports: Generate attendance summaries and reports.
- AI Integration: Handle attendance-related queries using an AI model.

Technologies Used

- Python
- Hugging Face Hub
- Hugging Face Inference API
- python-dotenv
- JSON

Setup

1. Clone or download this repository.

2. Install the required packages:
   
   pip install huggingface_hub python-dotenv

3. Create a ".env" file in the project directory:
   
   HF_TOKEN=your_hugging_face_token
HF_MODEL_ID=meta-llama/Llama-3.1-8B-Instruct

4. Run the application:
   
   python app.py

Future Improvements

- Database integration for storing records.
- Automated attendance summaries.
- Improved AI-powered queries.
- A user-friendly graphical interface.
