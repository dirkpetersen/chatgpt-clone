#! /bin/bash

if [[ ! -d "server" ]]; then
  echo "please run this script from the root of the git repos"
  exit
fi

if [[ ! -d "venv" ]]; then
  python3 -m venv venv
fi
source ./venv/bin/activate

if [[ -z "${OPENAI_API_KEY}" ]]; then
  echo "OPENAI_API_KEY not set"
  exit 1
  #export OPENAI_API_KEY=sk-
fi

# Flask settings 
#export FLASK_APP=ChatGPTUI
#export FLASK_DEBUG=true
#export FLASK_RUN_HOST="0.0.0.0"
#export FLASK_RUN_PORT=8081
#export FLASK_RUN_HOST="0.0.0.0"

if [[ ! -f "venv/bin/flask" ]]; then
  python -m pip install --upgrade -r requirements.txt
fi

python run.py
