

import logging
import pathlib

audit_dir = pathlib.Path('logs')
audit_dir.mkdir(exist_ok=True)

log_file = audit_dir / 'suite.log'

logger = logging.getLogger('QA_LOGGER')
logger.setLevel(logging.INFO)

if not logger.handlers:
    file_handler = logging.FileHandler(log_file, mode='w', encoding='utf-8')

    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

logger.info("Logger initialized and ready to use.")