# -*- coding: utf-8 -*-
import tweepy
import logging
from espreitador import Espreitador
from config import *

# Nivel de log
log_level = logging.INFO


def main():
    logging.basicConfig(
        level=log_level,
        datefmt='%d/%m/%Y %H:%M:%S',
        format='[%(asctime)s] <%(levelname)s> %(message)s'
    )

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)

    try:
        api.verify_credentials()
        logging.info(f"Logeado correctamente no twitter")
    except Exception as e:
        logging.error(f"Erro ao loguear no twitter")

    escoita = Espreitador(consumer_key = CONSUMER_KEY, consumer_secret = CONSUMER_SECRET, access_token = ACCESS_KEY, access_token_secret = ACCESS_SECRET, api = api, filtros = FILTROS)
    escoita.filter(track=FILTROS)
    
if __name__ == '__main__':
    main()