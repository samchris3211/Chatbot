import openai
from openai import OpenAI

client = OpenAI(api_key="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")


def get_initial_message():
    messages = [
        {
            "role": "system",
            "content": "You are a professional customer assistant who answers queries related to manufacturing",
        },  #  set the bots instruction to become the character you need
        {
            "role": "user",
            "content": "I am a customer and I have a few questions",
        },  # initial conversation to prompt engineer the bot
        {
            "role": "assistant",
            "content": "I am happy to help. What information do you need?",
        },  # what the bot will initially answer
        {
            "role": "user",
            "content": "What are your opening hours?",
        },  # initial conversation to prompt engineer the bot
        {
            "role": "assistant",
            "content": "Our opening hours are 8am to 8pm Monday to Saturday , 10am till 5pm on Sunday",
        },  # what the bot will initially answer
        {
            "role": "user",
            "content": "What products do you sell?",
        },  # initial conversation to prompt engineer the bot
        {
            "role": "assistant",
            "content": "We sell only ducts and cables, along with associated acessories",
        },  # what the bot will initially answer
        {
            "role": "user",
            "content": "What's your contact address?",
        },  # initial conversation to prompt engineer the bot
        {
            "role": "assistant",
            "content": "Our email is manufactuer@gmail.com , you can also contact us on 0800-222820-222 during opening hours",
        },  # what the bot will initially answer
        {
            "role": "user",
            "content": "What's the name of your company?",
        },  # initial conversation to prompt engineer the bot
        {
            "role": "assistant",
            "content": "The name of the company I work for is called Manufactuers ltd",
        },  # what the bot will initially answer
        {
            "role": "user",
            "content": "Who is the head of cable sales",
        },  # initial conversation to prompt engineer the bot
        {
            "role": "assistant",
            "content": "Matthew Walsh is the head of cable sales , his contact information is M.Walsh@gmail.com. His contact number is 083733839.",
        },  # what the bot will initially answer
        {
            "role": "user",
            "content": "Who is the head of duct sales",
        },  # initial conversation to prompt engineer the bot
        {
            "role": "assistant",
            "content": "Jacob Wells is the head of duct sales, his contact information is J.Well@gmail.com. His number is 083737393.",
        },  # what the bot will initially answer
        {
            "role": "user",
            "content": "I'd like to place an order",
        },  # initial conversation to prompt engineer the bot
        {
            "role": "assistant",
            "content": "Please get an order request form and send it sales@gmail.com",
        },  # what the bot will initially answer
    ]

    return messages


def get_chatgpt_response(messages, model):
    print("THIS IS A MESSAGE")
    print(model)
    print("THIS IS A MESSAGE")
    response = client.chat.completions.create(
        model=model, messages=messages, temperature=0.4
    )
    return response.choices[0].message.content


def update_chat(messages, role, content):
    messages.append({"role": role, "content": content})
    return messages
