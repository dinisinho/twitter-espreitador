# -*- coding: utf-8 -*-
import tweepy
import logging

class Espreitador(tweepy.Stream):
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret, api, filtros):
        tweepy.Stream.__init__(self, consumer_key, consumer_secret, access_token, access_token_secret)
        self.api = api
        self.filtros = filtros

    def on_status(self, status):
        if status.truncated:
            try:
                chio = status.extended_tweet['full_text']
            except Exception as e:
                logging.error(f"erro ao compoñer o tweet {e}")
        else:
            try:
                chio = status.text
            except Exception as e:
                logging.error(f"erro ao compoñer o tweet {e}")

        if not chio.startswith("RT @"):
            for filtro in self.filtros:
                if filtro in chio.lower():
                    try:
                        id_usuario = status.user.id
                        datos_usuario = self.api.get_user(user_id = id_usuario)
                        self.api.create_favorite(status.id)
                        self.api.retweet(status.id)
                        logging.info(f"fav e rt o chio {chio}")
                        if not datos_usuario.following:
                            self.api.create_friendship(user_id = id_usuario)
                            logging.info(f"Comezamos a seguir o usuario {id_usuario}")
                        break
                    except Exception as e:
                        logging.error(f"erro realizando accións sobre o tweet {e}")
