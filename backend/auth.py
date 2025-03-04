from functools import wraps
from flask import request, abort
from config import Config
# implemented, but auth not used in app

def require_api_key(f):
    """Decorator to require a valid API key for a route."""
    @wraps(f)
    def decorated(*args, **kwargs):
        client_key = request.headers.get('X-API-KEY')
        if not client_key or client_key not in Config.ALLOWED_API_KEYS:
            # Reject requests without valid API key, set in config and env
            abort(401, description="Unauthorized: Valid API key required")
        return f(*args, **kwargs)
    return decorated
