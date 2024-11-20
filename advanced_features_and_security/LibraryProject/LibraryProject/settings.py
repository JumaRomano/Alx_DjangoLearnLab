# Security Settings
DEBUG = False  # Ensure this is False in production

# Prevent XSS attacks
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

# Protect against clickjacking
X_FRAME_OPTIONS = 'DENY'

# Enforce cookies over HTTPS only
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

# Additional Security Settings
SECURE_SSL_REDIRECT = True  # Redirect all HTTP requests to HTTPS
SECURE_HSTS_SECONDS = 3600  # Enable HTTP Strict Transport Security
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
