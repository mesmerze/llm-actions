from langchain.chains import LLMChain
from langchain.output_parsers import StructuredOutputParser, ResponseSchema, OutputFixingParser
from langchain.prompts import PromptTemplate, ChatPromptTemplate, HumanMessagePromptTemplate
from langchain.chat_models import ChatOpenAI

import os
import sys

from langchain.chat_models import ChatOpenAI
from langchain.prompts import (
    PromptTemplate
)
from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
)

def main(openai_api_key):

    # Create prompt template and run chain to return pathname of the error
    human_message_prompt = HumanMessagePromptTemplate(
        prompt=PromptTemplate(
            template="""
Tell me a joke about {lang} language
""",
            input_variables=["lang"]
        )
    )
    chat_prompt_template = ChatPromptTemplate.from_messages([human_message_prompt])
    chat = ChatOpenAI(temperature=0, openai_api_key=openai_api_key)
    chain = LLMChain(llm=chat, prompt=chat_prompt_template)
    joke = chain.run('Python')

    print(joke)

if __name__ == "__main__":
    openai_api_key = sys.argv[1]
    main(openai_api_key)
