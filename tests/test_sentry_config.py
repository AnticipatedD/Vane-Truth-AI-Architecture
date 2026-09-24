import unittest
from werkzeug.exceptions import BadRequest, InternalServerError
from webapp.sentry_config import sentry_before_send

class TestSentryConfig(unittest.TestCase):
    def test_sentry_before_send_filters_4xx_http_exceptions(self):
        """Asserts that 4xx HTTP exceptions return None and are dropped by Sentry."""
        event = {"event_id": "test_400"}
        hint = {"exc_info": (None, BadRequest(), None)}
        
        result = sentry_before_send(event, hint)
        self.assertIsNone(result)

    def test_sentry_before_send_allows_5xx_http_exceptions(self):
        """Asserts that 5xx internal server errors pass through to Sentry."""
        event = {"event_id": "test_500"}
        hint = {"exc_info": (None, InternalServerError(), None)}
        
        result = sentry_before_send(event, hint)
        self.assertEqual(result, event)
