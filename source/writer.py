from google import genai
from openai import OpenAI
from pydantic import BaseModel, Field
 
class ExperienceSchema(BaseModel):
    pass

class SummarySchema(BaseModel):
    pass
class SkillSchema(BaseModel):
    skills: list[str] = Field(..., title="List of skills")

class CVOutputSchema(BaseModel):
    summary: SummarySchema = Field(..., title="Summary of the CV")
    experience: list[ExperienceSchema] = Field(..., title="List of experiences")
    skills: SkillSchema = Field(..., title="List of skills")


def generate_draft_cv(career_story: str, jd: str, model: str) -> str:
    if 'gpt' in model:
        client = OpenAI()

        completion = client.beta.chat.completions.parse(
            model=model,
            messages=[
                {"role": "system", "content": "Generate a draft CV."},
                {"role": "user", "content": f"Career Story: {career_story}"},
                {"role": "user", "content": f"Job Description: {jd}"},
            ],
        )

        return completion.choices[0].message.content
    elif 'gemini' in model:
        client = genai.Client()
    else:
        raise ValueError("Model not supported: {model}")