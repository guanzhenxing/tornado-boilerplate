import logging

from handlers.base import BaseHandler

logger = logging.getLogger('application.' + __name__)


class IndexHandler(BaseHandler):
    def get(self):
        self.render('index.html')
