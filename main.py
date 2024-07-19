import telebot
import os
from dotenv import load_dotenv
from google import generativeai

load_dotenv()
TOKEN = os.getenv("TOKEN")

bot = telebot.TeleBot(TOKEN)

generativeai.configure(api_key=os.getenv("GEMINI_API_KEY"))

generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 2000,
  "response_mime_type": "text/plain",
}

model = generativeai.GenerativeModel(
  model_name="gemini-1.5-flash",
)

@bot.message_handler()
def on_message(message):
    print(message)

    chat_session = model.start_chat(
        history=[
            {   
                "role": "user",
                "parts": f""
            },
            {
                "role": "model",
                "parts": ""
            }
        ]
    )

    print(chat_session)

    bot.reply_to(message, chat_session.send_message(message.text).text)
    
    print(chat_session)

bot.infinity_polling()