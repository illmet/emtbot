import os 
import telebot
import scraper as scr
#initiate bot
bott = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(bott)
#d = '6017373806:AAGsB6QB233I5eTzxzOnUqSdqGcudqsNYN0'
@bot.message_handler(commands=['start'])
def send_start(message):
    bot.reply_to(message, '\U0001F44B Welcome to the Euro Millions draw bot! Type "/last" to see the last win.')

#simple start command to print the most recent win!
last = '\U0001F911 Jackpot of '+scr.amount[0]+' was won on '+scr.dates[0]+'.'+scr.last[1]+'.'+' Current jackpot is '+scr.jackpot+' Million Euro. Perhaps Nataliia will win this one?'
@bot.message_handler(commands=['last'])
def send_last_win(message):
    bot.reply_to(message, last)

bot.infinity_polling()