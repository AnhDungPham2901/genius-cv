from google import genai
from openai import OpenAI
import os.path
from . import utils


def generate_cv(career_story: str, jd: str, customized_criteria: str, model: str) -> str:
    # Load system message from file
    system_message_path = os.path.join(os.path.dirname(__file__), "..", "prompts", "sys_gen_draft_cv.txt")
    system_message = utils.load_system_message(file_path=system_message_path)
    edu_info_path = os.path.join(os.path.dirname(__file__), "..", "data", "edu_info.txt")
    education_info = utils.load_edu_info(file_path=edu_info_path)
    contact_info_path = os.path.join(os.path.dirname(__file__), "..", "data", "contact_info.txt")
    contact_info = utils.load_contact_info(file_path=contact_info_path)
    
    if 'gpt' in model or 'o1' in model:
        client = OpenAI()

        completion = client.beta.chat.completions.parse(
            model=model,
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": f"Education Information: {education_info}"},
                {"role": "user", "content": f"Contact Information: {contact_info}"},
                {"role": "user", "content": f"Career Story: {career_story}"},
                {"role": "user", "content": f"Job Description: {jd}"},
                {"role": "user", "content": f"Customized Criteria to focus: {customized_criteria}"},

            ],
        )

        return completion.choices[0].message.content
    elif 'gemini' in model:
        raise NotImplementedError("Gemini model not implemented yet")
    else:
        raise ValueError(f"Model not supported: {model}")


def rewrite_cv():
    '''rewrite to improve given points in cv'''
    pass