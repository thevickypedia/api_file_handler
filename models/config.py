from pydantic import BaseModel


class LogConfig(BaseModel):
    """Custom log configuration that matches uvicorn log format.

    >>> LogConfig

    See Also:
        - ``LOGGER_NAME`` should match the name passed to ``getLogger`` when this class is used for ``dictConfig``
        - ``LOG_FORMAT`` is set to match the format of ``uvicorn.access`` logs.
    """

    LOGGER_NAME = 'LOGGER'
    LOG_FORMAT = '%(levelname)s:\t  %(message)s'

    version = 1
    disable_existing_loggers = False
    formatters = {
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": LOG_FORMAT,
            "datefmt": None,
        }
    }
    handlers = {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",
        }
    }
    loggers = {
        LOGGER_NAME: {"handlers": ["default"], "level": "DEBUG"},
    }
