import getpass
import os
from dotenv import load_dotenv

load_dotenv()

if "OPENAI_API_KEY" not in os.environ:
    os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter your OPENAI API key: ")

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="kimi-k2-turbo-preview",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    base_url="https://api.moonshot.cn/v1"
    # other params...
)
messages = [
    (
        "system",
        "You are a helpful assistant that translates English to French. Translate the user sentence.",
    ),
    ("human", "I love programming."),
]
ai_msg = llm.invoke(messages)
print(ai_msg.content)
