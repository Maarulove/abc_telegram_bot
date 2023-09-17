from typing import final
from telegram import Update
from telegram.ext import CommandHandler, MessageHandler, Application,filters, ContextTypes

token = "6673112703:AAH3eB37mZxMzS-lsVxzLUwPu57yRCMDG5A"
bot_usermame = "abc_bot"




async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hi every one! don't worry this is just a bot")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("if you need some help you can ask that to google or chat gpt")

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE): 
    await update.message.reply_text("This is custom command")



def handler_response(text: str) -> str:
    processed: str = text.lower()

    if "hello" in processed:
        return "Hi there!"

    if "what is this about" in processed:
        return "im just a tele bot"
    
    return "I don't understand what do you mean!)"

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text
    print(f"User {update.message.chat.id} in {message_type}, {text}")
    

    if message_type == "group":
        if bot_usermame in text:
            new_text: str = text.replace(bot_usermame, " ").strip()
            responce: str = handler_response(new_text)
        
        else:
            return
        
    else:
        responce: str = handler_response(text)

    print("Bot:", responce)
    await update.message.reply_text(responce)



async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Update{update}, caused error {context.error}")



if __name__ == "__main__":

    print("bot started")

    app = Application.builder().token(token).build()

    # COMMANDS
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("custom", custom_command))
     

    #message
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
 

    # ERRORS
    app.add_error_handler(error)

    print("Polling ....")
    app.run_polling(poll_interval=3)
