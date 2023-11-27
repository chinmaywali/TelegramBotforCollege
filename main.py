
import Constants as keys
from telegram.ext import * #The telegram.ext submodule is built on top of the pure API implementation
import Responses as R


print("Bot Started....")
#define few handlers , these usually take 2 arguments update and context

def start_command(update, context):  #update invokes every time when bot recives a message or command and will send user the message
    update.message.reply_text('Type someting random to get started!!')
                              
def help_command(update, context):   #sends the message when '/help' command is called
    update.message.reply_text('yes, how can i help you!!')

def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.sample_responses(text)

    update.message.reply_text(response)

def error(update , context):
    print(f"Update {update} caused error {context.error}")

def main():
     #create updater and pass it your bot's token
     #use_context is set true to use new context based callbacks
    updater = Updater(keys.API_KEY, use_context=True) # updater has api key, to specify in which bot we are adding functionalities

     #get the dispatcher to reg
     # ister handler
    dp = updater.dispatcher  #for the quicker access to the dispatcher used by updater , we introduce it locally

    dp.add_handler(CommandHandler("start", start_command)) #command handler class is used to handle any command sent by user to bot, commmand always starts with "/"
    dp.add_handler(CommandHandler("help", help_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message)) #message handler used to handle any normal message sent by user to bot

    dp.add_error_handler(error) #log all errors

     # polling - bot will be active and it will look for any new message  sent by  any users
     # and if it matches the command specified there reply accordingly
     # creates SMTP session

    updater.start_polling()

    updater.idle()



main()





