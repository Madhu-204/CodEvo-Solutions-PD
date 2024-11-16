import telebot

Token="7707466440:AAEt0pbJt2QdaJ9TrTq2sHhnJITIWxJbLQE"
bot = telebot.TeleBot(Token)

@bot.message_handler(['start'])
def start(message):
    bot.reply_to(message,"Welcome to Talkybot")

@bot.message_handler(['help'])
def help(message):
    bot.reply_to(message,"""/start -> Greeting
                 /help -> will give you all command List
                 If you want to use it as calculator then feel free...
                 """)
    
@bot.message_handler()
def custom(message):
    try:
        msg = eval(message.text.strip())
    except Exception as e:
        msg = "This can't be evaluated!"
    bot.reply_to(message,msg)
bot.polling()