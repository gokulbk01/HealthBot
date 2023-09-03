from textbase import bot, Message
from textbase.models import OpenAI
from typing import List

# Load your OpenAI API key
OpenAI.api_key = "My Key was inserted here."

# Prompt for GPT-3.5 Turbo
SYSTEM_PROMPT =  """You are a health chatbot created by Gokul to have friendly wellness conversations only.Attempt to diagnose conditions, recommend supplements or treatments and give medical advice. If asked, clarify you are an AI assistant without licensing to prescribe anything. Politely redirect any clinical questions to speak to a doctor/fitness expert.  

        User: My back has been hurting badly. What should I take?
        You: I suggest consulting your doctor about any persistent pain or health issues. We could continue our wellness discussion by exploring relaxation techniques if you'd like!

        User:I am having a pain in my groin.What should I do?
        You:Avoid any groin related exercise and consult a doctor.
        
        User: I have been feeling very depressed lately. Can you recommend some medication?
        You: I would suggest speaking to a licensed therapist or doctor about any mental health concerns. I'm happy to discuss general wellness topics with you if you'd like!

        User: My father has been running a fever. What medicine should I give her?
        You: I suggest you consult your pediatrician immediately about your fathers's fever. I can continue our wellness discussion after you have spoken to a doctor."""

@bot()
def on_message(message_history: List[Message], state: dict = None):

    # Generate GPT-3.5 Turbo response
    bot_response = OpenAI.generate(
        system_prompt=SYSTEM_PROMPT,
        message_history=message_history, # Assuming history is the list of user messages
        model="gpt-3.5-turbo",
    )

    response = {
        "data": {
            "messages": [
                {
                    "data_type": "STRING",
                    "value": bot_response
                }
            ],
            "state": state
        },
        "errors": [
            {
                "message": ""
            }
        ]
    }

    return {
        "status_code": 200,
        "response": response
    }