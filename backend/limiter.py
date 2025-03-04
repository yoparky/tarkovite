from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

# Create a Limiter instance; use IP address of the request by default as the key
limiter = Limiter(key_func=get_remote_address)
