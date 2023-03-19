import requests
import time
import json
from discord_webhook import DiscordWebhook, DiscordEmbed


#Coloque seus dados abaixo 

session = requests.session() 
session.cookies['_RoliData'] = '000' 
session.cookies['_RoliVerification'] = '000'



url = 'https://www.rolimons.com/tradeapi/create' 

tradead = {
  "player_id": 0000000, #Seu UID
  "offer_item_ids":[0000000,], #UID da sua ofertas
  "request_item_ids": [], #UID da sua requisicao
  "request_tags": ["any"], #Tags 
}


while True: 
  post = session.post(url,json=tradead)
  postJson = json.loads(post.text)
  
  success = postJson['success']
  print(success)
  messageLiteral = 's'
  print(post.text)
  messageLiteral = 'A TradeAd foi publicada com sucesso.' if success else 'Houve uma falha na publicação da TradeAd.'
  myColor = '32a852' if success else 'f70a0a' 
  try: 
    errorMessage = postJson['message']
  except KeyError: pass
  
  builtDescription = 'A TradeAd foi publicada sem objeções do servidor, uma nova TradeAd sera postada em breve.' if success else 'Ocorreu um erro ao criar uma nova TradeAds uma nova tentiva de postagem sera feita em algums minutos por favor espere. A resposta dada pelo servidor foi:\n\n> Mensagem do servidor: `' + errorMessage + '`.'

  fakeContent = '' if success else '@here'

  myWebhook = DiscordWebhook(url = '', content = fakeContent) #Coloque seu webhook em url ''
  myEmbed = DiscordEmbed(title = messageLiteral, description = builtDescription, color = myColor)
  myEmbed.set_timestamp()

  myEmbed.set_image(url='000') # Coloque a imagem (opcional)
  myWebhook.add_embed(myEmbed)
  webhookResponse = myWebhook.execute()
  time.sleep(1830)
