import logSetting
import logging.config

import logging
LOG_SETTINGS = {

        'version': 1,

        'root': {

            'level': 'INFO',

            'handlers': ['file']

            },

        'handlers': {

            'file': {

                'class' : 'logging.FileHandler',

                'level' : 'INFO',

                'formatter' : 'simpleformatter',

                'filename': 'dictlog.log',

                'mode' : 'a'

            }

        },

        'formatters': {

            'simpleformatter' : {

                'format' : '%(asctime)s %(module)-17s line: %(lineno)-4d %(levelname)-8s %(message)s',

            }

        }

    }
logging.config.dictConfig(LOG_SETTINGS)
logger = logging.getLogger("my_log")