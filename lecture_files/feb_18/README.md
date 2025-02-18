# Todo App 2/18/2025

1. Create Virtual Environment

'''powershell
python -m venv venv
.\venv\bin\activate

# macOS
source venv\bin\activate

pip install fastapi uvicorn

# after creating main.py file, generate an instance of FastAPI()
uvicorn main:app
