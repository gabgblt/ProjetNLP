import openai
import re

openai.api_key = "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"

def generate_response(prompt):
  completions = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=2048,
    n=1,
    stop=None,
    temperature=0.7,
  )

  message = completions.choices[0].text
  return message

while True:
  prompt = input("Moi: ")
  response = generate_response(prompt)
  print("Assistant: ", response)




