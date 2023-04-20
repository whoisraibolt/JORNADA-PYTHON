import logging

# Configura o nível de logging
logging.basicConfig(filename = 'log_1.txt', level = logging.ERROR)

print('Iniciando o programa...')

# Exemplo de log
logging.debug('Mensagem de debug')
logging.info('Mensagem de informação')
logging.warning('Mensagem de aviso')
logging.error('Mensagem de erro')
logging.critical('Mensagem crítica')

print('Finalizando o programa...')