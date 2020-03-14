# coding=utf-8
import logging

import tornado.escape
import tornado.ioloop
import tornado.locks
import tornado.web

from settings import app_settings, config
from urls import url_patterns

logger = logging.getLogger('application.' + __name__)


class Application(tornado.web.Application):
    def __init__(self):
        super(Application, self).__init__(url_patterns, **app_settings)

        self.config = config


def main():
    app = Application()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(config['port'])
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    logger.info("----------------------------------------------")
    logger.info("Started on port %s..." % (config['port'],))
    logger.info("----------------------------------------------")

    main()
