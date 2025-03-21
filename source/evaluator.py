import os.path 
from . import utils
from openai import OpenAI

def gen_overall_cv_criteria():
    '''
    This is to check the overall criteria of the CV
    '''
    pass

def gen_best_fit_cv_criteria():
    '''
    This is to check the best fit criteria of the CV
    '''
    pass


def gen_keywords_cv_criteria():
    '''
    This is to check the keywords criteria of the CV
    '''
    pass


def check_canadian_spelling():
    '''
    This is to check the Canadian spelling of words
    '''
    pass


def check_truthfulness(cv_string: str, real_info: str, model: str):
    '''
    This is to check the truthfulness of the CV compared to the real information
    '''
    system_message_path = os.path.join(os.path.dirname(__file__), "..", "prompts", "check_truthfulness.txt")
    system_message = utils.load_system_message(file_path=system_message_path)

    if 'gpt' in model:
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
