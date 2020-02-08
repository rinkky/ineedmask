import os
import time
import logging

logger = logging.getLogger("default")
logger.setLevel(logging.DEBUG)

if not os.path.exists('log'):
    os.makedirs('log')

file_handler = logging.FileHandler(
    os.path.join('log', "{}.log".format(time.strftime('%Y%m%d%H%M%S'))),
    encoding='utf-8'
)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
file_handler.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter('%(levelname)s: %(message)s'))
console_handler.setLevel(logging.DEBUG)

logger.addHandler(file_handler)
logger.addHandler(console_handler)
