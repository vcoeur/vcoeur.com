import logging

handler = logging.StreamHandler()
handler.setLevel(logging.INFO)
logging.getLogger().handlers = [handler]
logging.getLogger().setLevel(logging.INFO)
