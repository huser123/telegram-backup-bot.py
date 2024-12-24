import telebot
import requests
import subprocess as sp
from os import listdir
from os.path import isfile, join
from datetime import date

TOKEN = 'TOKEN'
CHAT_ID = 'CHAT_ID'

bot = telebot.TeleBot(TOKEN)

mypath = '/bot/tmp/'

bot.send_message(CHAT_ID,"A feltöltés napja: "+str(date.today()))
bot.send_message(CHAT_ID, sp.getoutput('zip -r -s 49M /bot/tmp/backup-$(date +%Y-%m-%d).zip /bot/mentes/mentes-$(date +%Y-%m-%d).zip'))
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
for i in onlyfiles:
  doc = open(mypath+i, 'rb')
  bot.send_document(CHAT_ID, doc,timeout=240)
bot.send_message(CHAT_ID, sp.getoutput('rm -Rfv /bot/tmp/*'))
bot.send_message(CHAT_ID,"Vége. A mentés sikeresen befejeződőtt.")
