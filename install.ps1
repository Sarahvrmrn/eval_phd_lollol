python -m pip install --upgrade pip
python -m pip install --user virtualenv
python -m venv venv
Set-ExecutionPolicy Unrestricted
.\venv\Scripts\activate
pip install -r .\requirements.txt