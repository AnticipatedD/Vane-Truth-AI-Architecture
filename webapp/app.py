# Packages
from sentry_sdk.integrations.flask import FlaskIntegration
# ... [keep your existing imports here]

# Local
from webapp.sentry_config import sentry_before_send
# ... [keep the rest of your local imports here]

logger = logging.getLogger(__name__)

# [Keep all your existing configuration down to the sentry declaration block]

# Sentry setup
sentry_dsn = get_flask_env("SENTRY_DSN")
environment = get_flask_env("FLASK_ENV", "production")

# Note: sentry_before_send is now cleanly imported from webapp.sentry_config
