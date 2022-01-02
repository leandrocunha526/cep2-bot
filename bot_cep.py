# -*- coding: utf-8 -*-

import requests
import json
import telepot
from telepot.loop import MessageLoop
import time


def handle(msg):
    typemsg, typechat, chat_id = telepot.glance(msg)
    command = msg['text'].split(' ')
    if msg['text'] == '/start':
        welcome = 'Seja bem vindo ao CEP2Bot'
        bot.sendMessage(chat_id, welcome)
    if msg['text'] == '/cep':
        msg = 'Digite o cep para buscar'
        bot.sendMessage(chat_id, msg)
    if command[0] == '/cep':
        cep = command[1]
        api = "https://viacep.com.br/ws/"+cep+"/json/unicode/"
        r = requests.get(api)
        results = json.loads(r.content)
        print(results)
        txt = 'Consulta de CEP e IBGE no Telegram:\nCEP: ' + results[
            'cep'] + '\nLogradouro: ' + results['logradouro'] + '\nComplemento: ' + results[
                  'complemento'] + '\nBairro: ' + results['bairro'] + '\nLocalidade: ' + results[
                  'localidade'] + '\nUF: ' + results['uf'] + '\nIBGE: ' + results['ibge'] + '\nDDD: ' + results['ddd']
        bot.sendMessage(chat_id, txt)  # send result


TOKEN = ''  # your token

bot = telepot.Bot(TOKEN)
ot = telepot.Bot(TOKEN)
MessageLoop(handle).run_as_thread()
print('Please wait')
print('Modo de uso para consultas: /cep 12345-123')

while 1:
    time.sleep(10)
