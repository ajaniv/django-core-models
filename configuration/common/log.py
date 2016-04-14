"""
.. module::  config.common.log
   :synopsis:  Django log settings file.

Django log settings file.

"""
import os
from .root import CURRENT_ENV, LOCAL_ENV, DEV_ENV, LOG_DIR
from utils.core import mkdir


INFO_LOG_LEVEL = 'INFO'
ERROR_LOG_LEVEL = 'ERROR'
DEBUG_LOG_LEVEL = 'DEBUG'


LOG_LEVEL = (DEBUG_LOG_LEVEL
             if CURRENT_ENV == DEV_ENV or CURRENT_ENV == LOCAL_ENV
             else INFO_LOG_LEVEL)


mkdir(LOG_DIR)

_verbose_format = ('%(levelname)s %(asctime)s' +
                   ' %(module)s %(process)d' +
                   ' %(thread)d %(message)s')
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': _verbose_format
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'null': {
            'level': DEBUG_LOG_LEVEL,
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': DEBUG_LOG_LEVEL,
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'log_file': {
            'level': DEBUG_LOG_LEVEL,
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'django.log'),
            'maxBytes': 16777216,  # 16megabytes
            'formatter': 'verbose'
        },
        'mail_admins': {
            'level': ERROR_LOG_LEVEL,
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True
        }
    },
    'loggers': {
        'django.db': {
            'handlers': ['console', 'log_file'],
            'level': INFO_LOG_LEVEL,
            'propagate': True
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': LOG_LEVEL,
            'propagate': True
        },
        'applications': {
            'handlers': ['log_file', 'console'],
            'level': LOG_LEVEL,
            'propagate': True
        },
        'core_utils': {
            'handlers': ['log_file', 'console'],
            'level': LOG_LEVEL,
            'propagate': True
        },
        'utils': {
            'handlers': ['log_file', 'console'],
            'level': LOG_LEVEL,
            'propagate': True
        }
    }
}
