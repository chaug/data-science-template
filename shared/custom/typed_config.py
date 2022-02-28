import os
from dotenv import load_dotenv
from pathlib import Path

def getenv_path(*args, **kwargs):
  return Path(os.getenv(*args, **kwargs) or '.').resolve()

def getenv_int(*args, **kwargs):
  return int(os.getenv(*args, **kwargs) or 0)
