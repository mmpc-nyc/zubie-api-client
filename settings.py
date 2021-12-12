from dotenv import load_dotenv
from os import environ

load_dotenv()

LOGLEVEL = 'DEBUG'
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'simple': {
            'format': '%(asctime)s [%(levelname)s] %(module)s - %(message)s',
            'datefmt': '%Y/%m/%d %H:%M:%S'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': LOGLEVEL,
            'formatter': 'simple'
        }
    },
    'root': {
        'level': LOGLEVEL,
        'handlers': ['console'],
        'propagate': False
    }
}

ZUBIE_CLIENT_ID = environ.get('ZUBIE_CLIENT_ID')
ZUBIE_API_KEY = environ.get('ZUBIE_API_KEY')

if __name__ == '__main__':
    import logging
    import logging.config

    logging.config.dictConfig(LOGGING)