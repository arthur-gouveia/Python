
# coding: utf-8

# In[1]:

import logging
import os
import poplib


# In[20]:

SERVER = os.environ['SERVER']
USER = os.environ['USER']
PASS = os.environ['PASS']
AUTH_FAIL = r'Authentication failed for user '+USER

logger = logging.getLogger('Email')
logger.setLevel(logging.INFO)


# In[21]:

def busca_emails(conexão, logger=None):
    from email.parser import Parser
    
    # Lista as mensagens no servidor
    resp, items, octets = conexão.list()
    if logger is not None:
        logger.info('Retrieved %d items from server' %len(items))
    # Pega todas as mensagens do servidor
    messages = {i: conexão.retr(i) for i in range(1, len(items)+1)}
    # Decodifica de bytes para string
    messages = {key: [m.decode() for m in messages[key][1]] for key in messages.keys()}
    # Transforma a lista de strings em uma string separada por \n
    messages = {key: '\n'.join(messages[key]) for key in messages.keys()}
    # Faz o parse dessa string em um objeto email.message
    messages = {key: Parser().parsestr(messages[key]) for key in messages.keys()}
    
    return messages


logger.debug('Connecting to '+SERVER)
conexão_pop = poplib.POP3_SSL(SERVER)
try:
    logger.debug('Log in')
    conexão_pop.user(USER)
    conexão_pop.pass_(PASS)
except poplib.error_proto:
    logger.debug(AUTH_FAIL)
    print(AUTH_FAIL)
else:
    messages = busca_emails(conexão_pop, logger)
    
    for id, message in messages.items():
        if 'packtpubnotify@gmail.com' not in message['From']:
            try:
                logger.debug('Deleting message '+str(id))
                conexão_pop.dele(id)
            except:
                logger.debug('Unable to delete message '+str(id))
                print('Unable to delete message.')
finally:
    conexão_pop.quit()
    logger.debug('Closed the connection')

