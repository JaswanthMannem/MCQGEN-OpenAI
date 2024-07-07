import pandas as pd
import os,json
from dotenv import load_dotenv
from src.mcqgenerator.utils import read_file,get_table_data
from src.mcqgenerator.loggers import logging

from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain

load_dotenv()

key=os.getenv("OPENAI_API_KEY")

llm=ChatOpenAI(openai_api_key=key,model="gpt-3.5-turbo",temperature=0.5)



template1="""
    Text:{text}
    You are an expert MCQ maker. Given the above text, it is your job to \
    Create a quiz of {number} multiple choice questions for {subject} students in {tone} tone.
    Mkae sure the questions are not repeated and check all the questions to be conforming the text as well.
    Make sure to format your response like RESPONSE_JSON below and use it as a guide. \
    Ensure to make {number} MCQs
    ### RESPONSE_JSON
    {response_json}
"""



quiz_generation_prompt=PromptTemplate(
    input_variables=["text","number","subject","tone","response_json"],
    template=template1
)

quiz_chain=LLMChain(llm=llm,prompt=quiz_generation_prompt,output_key="quiz",verbose=True)

template2="""
    You are an expert english grammerian writer. Given a Multiple Choice Quiz for {subject} students.\
    You need to evaluate the complexity of the question and give a complete analysis of the quiz. Only use at max 50 words for complexity
    if the quiz is not at per with cognitive and analytical abilities of the students,\
    Upadate the quiz questions which needs to be change the tone such that it perfectly fits the students abilities
    Quiz_MCQs:
    {quiz}

    Check from an expert English Writer of the above quiz:
"""
quiz_evaluation_prompt=PromptTemplate(
    input_variables=["subject","quiz"],
    template=template2
)

review_chain=LLMChain(llm=llm,prompt=quiz_evaluation_prompt,output_key="review",verbose=True)

generate_evalution_chain=SequentialChain(
    chains=[quiz_chain,review_chain],
    input_variables=["text","number","subject","tone","response_json"],
    output_variables=["quiz","review"],
    verbose=True
)


