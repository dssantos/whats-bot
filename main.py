import re
from bot import wppbot

nome_bot = '*Bot*'
bot = wppbot(nome_bot)
bot.treina('treino')
bot.inicia('Robot')
bot.saudacao([f'{nome_bot}: Oi, eu sou o Bot, o garçom virtual do Bar!', f'{nome_bot}: Para falar comigo digite 3 pontinhos (...) seguido de algo que você deseja. \n{nome_bot}: Por exemplo:   ...cardapio   ...bebidas  ...cervejas  ...tiragostos '])
ultimo_texto = ''



while True:

    texto = bot.escuta()

    if texto != ultimo_texto and re.match(r'^\.\.\.', texto):

        ultimo_texto = texto
        texto = texto.replace('...', '')
        texto = texto.lower()

        if (texto == 'aprender' or texto == ' aprender' or texto == 'ensinar' or texto == ' ensinar'):
            bot.aprender(texto,f'{nome_bot}: Escreva a pergunta e após o ? a resposta.',f'{nome_bot}: Obrigado por ensinar! Agora já sei!',f'{nome_bot}: Você escreveu algo errado! Comece novamente..')
        elif (texto == 'noticias' or texto == ' noticias' or texto == 'noticia' or texto == ' noticia' or texto == 'notícias' or texto == ' notícias' or texto == 'notícia' or texto == ' notícia'):
            bot.noticias()
        elif texto in ['cardapio', ' cardapio', 'cardápio', ' cardápio', 'Cardapio', ' Cardapio', 'Cardápio', ' Cardápio']:
            bot.cardapio()
        elif texto in ['bebidas', ' bebidas', 'bebida', ' bebida', 'Bebidas', ' Bebidas', 'Bebida', ' Bebida']:
            bot.bebidas()
        elif texto in ['cervejas', ' cervejas', 'cerveja', ' cervejas', 'Cervejas', ' Cervejas', 'Cerveja', ' Cerveja']:
            bot.cervejas()
        elif texto in ['tiragostos', ' tiragostos', 'tiragosto', ' tiragostos', 'Tiragostos', ' Tiragostos', 'Tiragosto', ' Tiragosto']:
            bot.tiragostos()
        else:
            bot.responde(texto)