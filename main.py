from openai import OpenAI
from dotenv import load_dotenv
import os

def main():
    load_dotenv()
    api_key = os.environ.get('OPENROUTER_API_KEY')
    
    if api_key is None:
        raise RuntimeError("api_key isn't configured yet")
    
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key
    )
    
    response = client.chat.completions.create(model='openrouter/free', messages=[
        {
            "role": "user",
            "content": "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.",
        }
    ])
   
    usages = response.usage
    if usages is None:
        raise RuntimeError("failed to make request, try again")
    prompt_tokens = usages.prompt_tokens
    completion_tokens = usages.completion_tokens
   
    print("Prompt tokens:", prompt_tokens)
    print("Response tokens:", completion_tokens) 
    print("Response:")
    print(response.choices[0].message.content)

if __name__ == "__main__":
    main()
