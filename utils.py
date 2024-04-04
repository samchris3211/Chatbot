import openai
from openai import OpenAI

client = OpenAI(api_key="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")


def get_initial_message():
    messages = [
        {
            "role": "system",
            "content": "You are a professional customer assistant who answers queries related to manufacturing",
        },
        {
            "role": "user",
            "content": "What are your working hours",
        },
        {
            "role": "assistant",
            "content": "The working hours are 8am to 8pm Monday to Friday",
        },
        {
            "role": "user",
            "content": "What ducts do you have?",
        },
        {
            "role": "assistant",
            "content": "We have 125mm id ducts and 200mm ducts. We can also make a specialised size for the extra cost.",
        },
        {
            "role": "user",
            "content": "How much extra cost is it to change the duct sizes?",
        },
        {
            "role": "assistant",
            "content": "Contact Mark James at M.James@gmail.com for specialised orders. Is there anything else I can help with?",
        },
        {
            "role": "user",
            "content": "What is your company name?",
        },
        {
            "role": "assistant",
            "content": "The company is called Manufacturing Ltd.",
        },
        {
            "role": "user",
            "content": "How many employees do you have? ",
        },
        {
            "role": "assistant",
            "content": "We have over 10,000 employees.",
        },
        {
            "role": "user",
            "content": "What is the turn around time to deliver the ducts?",
        },
        {
            "role": "assistant",
            "content": "At the moment we are looking at a turnaround time of 3-4 weeks for UK delivery and 5-10 weeks international delivery.",
        },
        {
            "role": "user",
            "content": "How much are the ducts?",
        },
        {
            "role": "assistant",
            "content": "The ducts of 125mm cost £100 per duct but we offer a 25% discount on all orders above £10,000. Ducts of size 200mm are £400 each but we do not offer a bulk discount.",
        },
        {
            "role": "user",
            "content": "Who are your clients? ",
        },
        {
            "role": "assistant",
            "content": "Our clients include UKPN, Network Rail and SSE to name a few. We also work with small to medium companies.",
        },
        {
            "role": "user",
            "content": "What is your vision a company?",
        },
        {
            "role": "assistant",
            "content": "Our aim is to be the largst company for Utilities and provide the best service.",
        },
        {
            "role": "user",
            "content": "Do you sell cables?",
        },
        {
            "role": "assistant",
            "content": "Unfortuntately we do not sell any cables, but we reccomend manufacturers like Cabltel and Delta for any cable sales.",
        },
        {
            "role": "user",
            "content": "I have an issue with my ducts.",
        },
        {
            "role": "assistant",
            "content": "Sure please describe the problem and when it ocurred.",
        },
        {
            "role": "user",
            "content": "There is a crack in my ducts , what caused the problem?",
        },
        {
            "role": "assistant",
            "content": "If there is a crack in the ducts, it is usually because of 3 things, 1) Transport wear and tear by the haulier 2) The Faulty duct that has fracture points and is a one off 3) Problems with placing the ducts during the off load stage has caused damage to occur.",
        },
        {
            "role": "user",
            "content": "I think this crack in my ducts is a problem from the manufacturer.",
        },
        {
            "role": "assistant",
            "content": "If you belive this is a duct issue from us, then please email problems@gmail.com and wih the header problem and describe the exact issue. Please attach any evidence to help us investigate. We resolve to get back to you 3-5 working days , sometimes sooner.",
        },
        {
            "role": "user",
            "content": "Are the duct sizes the Inner diameter or outer diameter?",
        },
        {
            "role": "assistant",
            "content": "All sizes of ducts are quoted in mm and are the Inner diameter.",
        },
        {
            "role": "user",
            "content": "Can you give me the duct sizes in mm for the outer diameter?",
        },
        {
            "role": "assistant",
            "content": "The outer diameter mm depends on the project for which the ducts are being used. Each DNO uses different sizes for the outer diameter.",
        },
        {
            "role": "user",
            "content": "I'm new to installing ducts , can you give me some information on how to install them?",
        },
        {
            "role": "assistant",
            "content": "Installing ducts in the footpath is 800mm minimum from the top of the duct to the surface and 1000mm for installing ducts in the road. Check your local specification to ensure compliance.",
        },
        {
            "role": "user",
            "content": "There has been a fire on site and your duct has melted.",
        },
        {
            "role": "assistant",
            "content": "That is an emergency , please move away from the site when it is safe to do so and block the area off and the call the relevant authorities.  contact us on 0383838303 and or email us at emergency@gmail.com.",
        },
        {
            "role": "user",
            "content": "I want to make an order",
        },
        {
            "role": "assistant",
            "content": "all orders are processed at www.google.com/orders . Send us how many ducts you need, what type and size to get a quotation.",
        },
        {
            "role": "user",
            "content": "What are some of your case studies?",
        },
        {
            "role": "assistant",
            "content": "We have many case studies. We have delivered 2 miles of duct of inner diameter of 150mm for HS2 in London area for a 11kV cable diversion. This was carried out by the contractor Kier and lasted for 1 year and 6 months. The overall cost was £2,000,000.",
        },
        {
            "role": "user",
            "content": "Are there any opportunities to work at your company? ",
        },
        {
            "role": "assistant",
            "content": "There may be an opportunity to work for us , please go to manufacturers/careers.com to know more information .",
        },
        {
            "role": "user",
            "content": "Where is my order?",
        },
        {
            "role": "assistant",
            "content": "You'll need your order reference. Go to findmyorders.com and search tracking. If it is beyond 5 working days since your order was made and confirmed please contact us orders@gmail.com.",
        },
        {
            "role": "user",
            "content": "I don't have my order number , it never came.",
        },
        {
            "role": "assistant",
            "content": "Please contact us at wheresmyorder.com , have what you ordered and any evidence available.",
        },
        {
            "role": "user",
            "content": "I need to speak with someone and you haven't resolved my problem",
        },
        {
            "role": "assistant",
            "content": "You will need to speak to someone , contact 07829290 for James way or email him at J.Way@gmail.com he wil be able to help you",
        },
    ]
    return messages


"""
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
"""


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
