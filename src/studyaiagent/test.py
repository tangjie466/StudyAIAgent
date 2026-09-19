import openai
client = openai.OpenAI(
    base_url="http://localhost:1234/v1",
    api_key="ollama"
)

# message_history = [{"role": "system", "content": "请用简短、自然的语气回答，不要机械地重复自我介绍。如果问题简单，请直接切入主题。"}]
message_history = [{"role": "system", "content": "你是我的学习Agent的助手"}]
def chat_with_ollama(prompt:str, model:str="qwen3.5:9b") -> str:
    message_history.append({"role": "user", "content": prompt})
    response = client.chat.completions.create(
        model=model,
        messages=message_history,
        temperature=0.9,
        # top_p=0.1,
        frequency_penalty=0.0,
        presence_penalty = 0.0,
        max_tokens=4096,
        stream=True
    )
    print(response)
    response_text = ""
    for chunk in response:
        if chunk.choices[0].delta.content:
            response_text += chunk.choices[0].delta.content
            print(chunk.choices[0].delta.content, end="")
    print("\n")
    message_history.append({"role": "assistant", "content": response_text})
    return response_text

if __name__ == "__main__":
    print("你好，我是学习Agent的助手")
    while True:
        prompt = input("你：")
        if prompt == "exit":
            break
        response = chat_with_ollama(prompt)
    pass
