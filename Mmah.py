import requests
import telebot
from bs4 import BeautifulSoup
import requests,time,os
from time import sleep
from telebot import types
import random

token = input("[~] Enter Token :")
bot = telebot.TeleBot(token)

sleep = 5
check = types.InlineKeyboardButton(text ="SmS List ", callback_data = 'sms')

@bot.message_handler(commands=['start'])
def start(message):
    list = ['+972552603210','+918527834283','+917428731210','+917428731268','+917428730894']
    phonenumber = f"+{rws} "
    getsmss = "https://givt.ga/sms/message?n={rws}"

    use = message.from_user.username
    fr = message.from_user.first_name
    maac = types.InlineKeyboardMarkup()
    maac.row_width = 1
    maac.add(check)
    bjj = message.chat.id
    bot.send_message(message.chat.id,text=f"""
    <strong>
Welcome {fr} ! 
- - - - - - - - - - - 
To SmS Receiver Bot! 
Now Copy This Number : 
<code>+{rws}</code>
And Click On SmS List ! 
- - - - - - - - - - -
Dev By : @y_je ~ @B_7_5
</strong>

    """,parse_mode='html',reply_to_message_id=message.message_id, reply_markup=maac)
def qwere(call):
    	if call.data == 'sms':
    		get_sms(call.message)
@bot.message_handler(func=lambda m: True)
def get_sms(message):
    try:
        
        msg = message.text
        def trakos(message): 
         req = requests.get(getsmss)
        src = req.content
        soup = BeautifulSoup(src, "lxml")
        msgs = soup.find_all("tr")
        for i in range(len(msgs)):
        	smss.append(msgs[i].text)
        	for i in range(len(smss)):
        		smss[i] = smss[i].replace('nf1222', '')
        		smss[i] = smss[i].replace(f'/{rws}n ','')
        		with open("sms.txt","a")as x:
        						x.write(f"\n{get_sms}")
        						print(sms)
        						k = open('myfile.txt')
        						contents = k.read()
        		print(msgs)
        		bot.send_message(message.chat.id,f"Your SmS List :\n{contents}\n")
        	else:
        						bot.send_message(message.chat.id,'Messages not found Or Dont Revevier')
        						time.sleep(sleep)
        			
      
    except:
        pass

bot.polling(True)
