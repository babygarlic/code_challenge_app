import os
from together import Together
from typing import Dict, Any
import json
from dotenv import load_dotenv

load_dotenv()

LLM_model = Together(api_key=os.getenv("TOGETHER_API_KEY"))
def generate_challenge_ai(difficulty: str) -> Dict[str, Any]:
    """
    Generate a coding challenge based on the specified difficulty.
    """
    systemprompt ="""You are expert coding coding challenge creator.
    You task is to generate a coding question with multiple choice anwers.
    The question shoule be appropriate for the specified difficulty level.

    For easy question: Focus on basic syntax, simple operations, or common programing concepts.
    For medium questions: Cover intermediate concepts like data structures, algorithms, language features.
    For hard questions: Include  advance topics, design patterns, Optimization techniques, or complex algorithms.
    
    Return the challenge in the following JSON structure:
    {
        "title":"The question",
        "options":["option 1","option 2","option 3","option 4"],
        "correct_answer_id":0, // Index of the correct answer (0-3)
        "explanation":"Detailed explanation of why the correct answer is right"
    }
    Caution:
    Return tre format.
    Make sure the options are plausible but with only one clearly correct answer.
"""
    try:
        response = LLM_model.chat.completions.create(
            model="Qwen/Qwen3-235B-A22B-Thinking-2507",
            messages=[
                {"role": "system", "content":systemprompt},
                {"role": "user", "content": f"Generate a {difficulty} coding challenge."}
            ], 
            response_format={"type":"json_object"},
            temperature=0.6
        )
        challenge_data = json.loads(response.choices[0].message.content)
        requered_fields = ["title", "options", "correct_answer_id", "explanation"]
        for field in requered_fields:
            if field not in challenge_data:
                raise ValueError(f"Missing required field:{field}")

        return challenge_data
    except Exception as e:
        print(e)
        return {
            "title":"Basic Python List Operation",
            "option":[
                "my_list.append(5)",
                "my_list.add(5)",
                "my_list.push(5)",
                "my_list.insert(5)",
            ],
            "correct_answer_id":0,
            "explanation":"In Python, append() is the correct method to add an element to the end of the list."
        }