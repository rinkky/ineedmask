from config.logger import logger

# 请自行添加提醒方法

try:
    from .local import alert
except Exception:
    def alert(msg):
        logger.info('alert: {}'.format(msg))
