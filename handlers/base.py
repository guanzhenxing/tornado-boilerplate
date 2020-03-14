import logging
from typing import Optional, Awaitable

import tornado.web

logger = logging.getLogger('application.' + __name__)


class BaseHandler(tornado.web.RequestHandler):
    """A class to collect common handler methods - all other handlers should
    subclass this one.
    """

    def data_received(self, chunk: bytes) -> Optional[Awaitable[None]]:
        pass

    def load_json_request_body(self):
        """Load JSON from the request body and store them in
        self.request.arguments, like Tornado does by default for POSTed form
        parameters.
        If JSON cannot be decoded, raises an HTTPError with status 400.
        """
        try:
            import json
            return json.loads(self.request.body)
        except ValueError:
            msg = "Could not decode JSON: %s" % self.request.body
            logger.debug(msg)
            raise tornado.web.HTTPError(400, msg)
