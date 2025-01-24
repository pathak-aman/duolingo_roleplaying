from ollama import chat, ChatResponse

# MODEL = "llama3-chatqa"
MODEL = "deepseek-r1:8b"

# # No streaming
# response = chat(
#     model = MODEL, messages= [{'role' : "user",'content' : "Why is sky blue?"}]
#     )
# print(response["message"]["content"])

# With streaming
stream_response = chat(
    model = MODEL,
    messages = [{"role":"user", "content":"Why do you think high cortisol levels are bad for men?"}],
    stream = True
)

for chunk in stream_response:
    print(chunk['message']['content'], end='', flush=True)