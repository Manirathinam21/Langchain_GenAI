from langchain_google_genai import ChatGoogleGenerativeAI
from fastapi import FastAPI
import uvicorn
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from langserve import add_routes

# Creating prompt templates
prompt= ChatPromptTemplate.from_messages([
            ("system", "Translate the following into {language}:"),
            ("user", "{text}")])

# Creating LLM
llm= ChatGoogleGenerativeAI(model= 'gemini-pro', convert_system_message_to_human=True)

parser= StrOutputParser()

# Creating chain
chain= prompt | llm | parser

app = FastAPI(
    title="My LLM API",
    description="My first LLM API",
    version="1.0",)

add_routes(app,
           chain,
           path='/chain')

if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8000)
    
# to see localhost in browser give following /chain/playground/ in end of the localhost link
# http://localhost:8000/chain/playground/