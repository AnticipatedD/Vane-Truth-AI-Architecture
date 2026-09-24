# Copyright Advanced Micro Devices, Inc.
#
# SPDX-License-Identifier: MIT

import random
import requests
from werkzeug.exceptions import HTTPException
from requests.exceptions import ConnectionError, HTTPError, RetryError
from urllib3.exceptions import MaxRetryError

def sentry_before_send(event, hint):
    """
    Filter Sentry events.
    Excludes all 4xx errors and upstream connection failures.
    """
    if "exc_info" in hint:
        _, exc_value, _ = hint["exc_info"]
        
        # Check if the exception is an HTTPException (which includes 4xx errors)
        if (
            isinstance(exc_value, HTTPException)
            and 400 <= exc_value.code < 500
        ):
            return None
            
        # Also filter requests.exceptions.HTTPError for 4xx upstream responses
        if isinstance(exc_value, requests.exceptions.HTTPError):
            response = getattr(exc_value, "response", None)
            if response is not None and 400 <= response.status_code < 500:
                return None
                
        # Sample 5% of transient upstream connection failures
        if isinstance(exc_value, (MaxRetryError, RetryError, ConnectionError)):
            error_msg = str(exc_value)

            # Sample blog/WordPress API retry errors
            if "/wp-json/wp/v2" in error_msg:
                if random.random() > 0.05:  # Drop 95% of blog API retry errors
                    return None
    return event
