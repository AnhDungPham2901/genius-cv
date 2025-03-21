from loguru import logger

def load_system_message(file_path: str) -> str:
    try:
        with open(file_path, "r") as f:
            system_message = f.read()
        return system_message
    except FileNotFoundError:
        # Fallback if file is not found
        raise FileNotFoundError(f"System message file not found at {file_path}")

def load_edu_info(file_path: str) -> str:
    try:
        with open(file_path, "r") as f:
            education_info = f.read()
        return education_info
    except FileNotFoundError:
        # Fallback if file is not found
        raise FileNotFoundError(f"Education information file not found at {file_path}")
    
def load_contact_info(file_path: str) -> str:
    try:
        with open(file_path, "r") as f:
            contact_info = f.read()
        return contact_info
    except FileNotFoundError:
        # Fallback if file is not found
        raise FileNotFoundError(f"Contact information file not found at {file_path}")
    

def load_career_story(file_path: str) -> str:
    try:
        with open(file_path, "r") as f:
            career_story = f.read()
        return career_story
    except FileNotFoundError:
        # Fallback if file is not found
        raise FileNotFoundError(f"Career story file not found at {file_path}")
    
def load_job_description(file_path: str) -> str:
    try:
        with open(file_path, "r") as f:
            job_description = f.read()
        return job_description
    except FileNotFoundError:
        # Fallback if file is not found
        raise FileNotFoundError(f"Job description file not found at {file_path}")
    

def string_to_html_file(html_content, output_filepath):
    """
    Save HTML content string to an HTML file
    
    Parameters:
        html_content (str): The HTML content as a string
        output_filepath (str): Path where the HTML file should be saved
    """
    with open(output_filepath, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    logger.success(f"HTML file created successfully at: {output_filepath}")


def extract_html_code_from_string(html_string):
    """
    Extract HTML code from a string containing markdown-style code block with HTML
    
    Parameters:
        html_string (str): The string containing HTML code in format like ```html <actual html> ```
    
    Returns:
        str: The extracted HTML code
    """
    parts = html_string.split("```html")
    if len(parts) > 1:
        # Get the part after ```html
        html_part = parts[1].split("```")[0]
        return html_part.strip()
    else:
        raise ValueError("No HTML code found in the input string")