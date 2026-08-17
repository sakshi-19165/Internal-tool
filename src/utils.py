import logging

from pathlib import Path

from urllib.parse import urlparse


def validate_url(url):

    parsed_url = urlparse(url)

    if not parsed_url.scheme:

        raise ValueError(
            "URL must start with http:// or https://"
        )

    if parsed_url.scheme not in [
        "http",
        "https"
    ]:

        raise ValueError(
            "Only HTTP and HTTPS URLs are allowed."
        )

    if not parsed_url.netloc:

        raise ValueError(
            "Invalid website address."
        )

    return True


def setup_logger():

    log_folder = Path("logs")

    log_folder.mkdir(
        exist_ok=True
    )

    logger = logging.getLogger(
        "research_tool"
    )

    logger.setLevel(
        logging.INFO
    )

    if not logger.handlers:

        file_handler = logging.FileHandler(
            "logs/tool.log"
        )

        formatter = logging.Formatter(

            "%(asctime)s - "
            "%(levelname)s - "
            "%(message)s"
        )

        file_handler.setFormatter(
            formatter
        )

        logger.addHandler(
            file_handler
        )

    return logger