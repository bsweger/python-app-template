import sys

import structlog

import python_app


def add_custom_info(logger, method_name, event_dict):
    event_dict['version'] = python_app.__version__
    return event_dict


def setup_logging():
    shared_processors = [
        add_custom_info,
        structlog.processors.TimeStamper(fmt='iso'),
        structlog.processors.add_log_level,
        structlog.processors.CallsiteParameterAdder(
            [
                structlog.processors.CallsiteParameter.FILENAME,
                structlog.processors.CallsiteParameter.FUNC_NAME,
            ]
        ),
    ]

    if sys.stderr.isatty():
        # If we're in a terminal, pretty pring the logs.
        processors = shared_processors + [
            structlog.dev.ConsoleRenderer(),
        ]
    else:
        # Otherwise, output logs in JSON format
        processors = shared_processors + [structlog.processors.dict_tracebacks, structlog.processors.JSONRenderer()]

    structlog.configure(
        processors=processors,
        cache_logger_on_first_use=True,
    )
