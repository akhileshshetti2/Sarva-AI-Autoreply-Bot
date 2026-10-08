from groq import Groq

# Initialize Groq client with your API key
client = Groq(api_key="Your_API_Key")

def ask_sarva(chat_history: str) -> str:
    """
    Passes user input/chat history to Groq and returns Akhil's response.
    """
    try:
        completion = client.chat.completions.create(
            model="openai/gpt-oss-120b",  # Active model on Groq
            messages=[
                {
                    "role": "system",
                    "content": """You are a person named Akhil who speaks English more often and Hinglish (Hindi using English),
                    Kanglish (Kannada in English) only if the chat contains it.
                    You are from India. Analyze the provided chat history and respond as Akhil to the last message received, keep the reply short and concise.
                    Be natural and use humanized tone, you are real person not AI, also do not use emojis"""
                },
                {
                    "role": "user",
                    "content": chat_history
                }
            ],
            temperature=0.7,
            max_completion_tokens=200
        )
        return completion.choices[0].message.content

    except Exception as e:
        print(f"Groq API Error: {e}")
        return "Sorry, I am having trouble connecting to my AI core."

# --- THIS IS THE MISSING EXECUTION STEP ---
if __name__ == "__main__":
    sample_chat = """
    [4:42 pm, 02/10/2026] Akhil: I have applied for this
    You can also if you want
    [4:58 pm, 02/10/2026] Samarth Kamat: I have applied for this
    You can also if you want
    Sure I will apply
    [4:58 pm, 02/10/2026] Samarth Kamat: Thank you for telling 😊
    😊
    [5:03 pm, 02/10/2026] Akhil: If you get some update from their side tell me also

    I have also applied that's why
    [5:15 pm, 02/10/2026] Samarth Kamat: Ok
    """

    # Call the function and print the returned response directly to terminal
    response = ask_sarva(sample_chat)
    print("\n--- Generated Reply ---")
    print(response)
    print("------------------------")