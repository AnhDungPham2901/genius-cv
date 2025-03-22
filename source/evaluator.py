import os.path 
from . import utils
from openai import OpenAI
from pydantic import BaseModel, Field
from typing import List, Optional

def gen_customized_cv_criteria(jd: str, model: str):
    '''
    This is to check the best fit criteria of the CV
    '''
    system_message_path = os.path.join(os.path.dirname(__file__), "..", "prompts", "gen_customized_cv_criteria.txt")
    system_message = utils.load_system_message(file_path=system_message_path)

    if 'gpt' in model or 'o1' in model:
        client = OpenAI()

        completion = client.beta.chat.completions.parse(
            model=model,
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": f"JD to generate customized criteria: {jd}"},
            ],
        )

        return completion.choices[0].message.content
    elif 'gemini' in model:
        raise NotImplementedError("Gemini model not implemented yet")
    else:
        raise ValueError("Model not supported: {model}")
    

def check_missing_criteria(customized_cv_criteria: str, cv_string: str, model: str) -> str:
    '''
    After generating cv_v1 with customized criteria, this function is to check if there are any missing criteria
    and suggest the missing criteria
    '''
    class ImprovementArea(BaseModel):
        missing_criteria: List[Optional[str]] = Field(..., title="Missing Criteria", description="The missing criteria in the CV")

    system_message_path = os.path.join(os.path.dirname(__file__), "..", "prompts", "check_missing_criteria.txt")
    system_message = utils.load_system_message(file_path=system_message_path)

    if 'gpt' in model or 'o1' in model:
        client = OpenAI()

        completion = client.beta.chat.completions.parse(
            model=model,
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": f"Customized CV criteria: {customized_cv_criteria}"},
                {"role": "user", "content": f"Generated CV: {cv_string}"},
            ],
            response_format=ImprovementArea,
        )

        return completion.choices[0].message.content
    elif 'gemini' in model:
        raise NotImplementedError("Gemini model not implemented yet")
    else:
        raise ValueError("Model not supported: {model}")


def grade_cv(cv_string: str, jd: str, general_criteria: str, model: str):
    '''
    This is to grade the CV based on the JD
    and suggest improvements
    '''
    pass


def check_country_spelling(cv: str, country: str, model: str):
    '''
    This is to check the Canadian spelling of words
    '''
    system_message_path = os.path.join(os.path.dirname(__file__), "..", "prompts", "check_spelling_by_country.txt")
    system_message = utils.load_system_message(file_path=system_message_path)

    if 'gpt' in model or 'o1' in model:
        client = OpenAI()

        completion = client.beta.chat.completions.parse(
            model=model,
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": f"CV to check the spelling: {cv}"},
                {"role": "user", "content": f"Country to check the spelling: {country}"},
            ],
        )

        return completion.choices[0].message.content
    elif 'gemini' in model:
        raise NotImplementedError("Gemini model not implemented yet")
    else:
        raise ValueError("Model not supported: {model}")


def check_truthfulness(cv_string: str, real_info: str, model: str):
    '''
    This is to check the truthfulness of the CV compared to the real information
    '''
    system_message_path = os.path.join(os.path.dirname(__file__), "..", "prompts", "check_truthfulness.txt")
    system_message = utils.load_system_message(file_path=system_message_path)

    if 'gpt' in model or 'o1' in model:
        client = OpenAI()

        completion = client.beta.chat.completions.parse(
            model=model,
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": f"CV to check truthfulness: {cv_string}"},
                {"role": "user", "content": f"Real information for the checking: {real_info}"},
            ],
        )

        return completion.choices[0].message.content
    elif 'gemini' in model:
        raise NotImplementedError("Gemini model not implemented yet")
    else:
        raise ValueError("Model not supported: {model}")
