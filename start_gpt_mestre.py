
import os
from dotenv import load_dotenv
import subprocess

# Carrega variáveis do .env
load_dotenv()

# Executa o Streamlit apontando para o main.py
subprocess.run(["streamlit", "run", "main.py"])
