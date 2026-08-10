from openai import OpenAI
from dotenv import load_dotenv
from typing import Iterable
from openai.types.chat.chat_completion_message_param import ChatCompletionMessageParam

import os
import argparse

def main():
    parser = argparse.ArgumentParser(description='Chatbot')
    parser.add_argument('user_prompt', type=str, help="User prompt")
    parser.add_argument('--verbose', action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    
    load_dotenv()
    api_key = os.environ.get('OPENROUTER_API_KEY')
    
    if api_key is None:
        raise RuntimeError("api_key isn't configured yet")
    
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key
    )
    
    messages: Iterable[ChatCompletionMessageParam] = [
        {"role": "user", "content": args.user_prompt}
    ]
    
    response = client.chat.completions.create(model='openrouter/free', messages=messages)
   
    usages = response.usage
    if usages is None:
        raise RuntimeError("failed to make request, try again")
    prompt_tokens = usages.prompt_tokens
    completion_tokens = usages.completion_tokens
   
    if args.verbose:
        print("User prompt:", args.user_prompt)
        print("Prompt tokens:", prompt_tokens)
        print("Response tokens:", completion_tokens) 
    print("Response:")
    print(response.choices[0].message.content)

if __name__ == "__main__":
    main()
