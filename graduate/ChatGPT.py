import openai

openai.api_key = "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"

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": "You are famous blogger.",
        },
        {
            "role": "user",
            "content": "Can you recommend fresh blog post theme?",
        }
    ],
)
print(completion)
'''
role을 선택해서 챗봇처럼 활용할 수 있음.
'''