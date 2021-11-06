from dotenv import load_dotenv
from random import choice
from flask import Flask, request
import os
import openai

load_dotenv()
open.api_key = os.getenv("OPENAI_API_KEY")
completion = openai.Completion()

start_sequence = "n\basnikZ:"
restart_sequence = "n\mPerson:"
