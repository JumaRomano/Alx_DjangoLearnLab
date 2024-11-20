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

# Enforce HTTPS connections
SECURE_SSL_REDIRECT = True  # Redirect HTTP requests to HTTPS

# HTTP Strict Transport Security (HSTS)
SECURE_HSTS_SECONDS = 31536000  # One year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True  # Apply HSTS to all subdomains
SECURE_HSTS_PRELOAD = True  # Allow browser preload of HSTS policies

# Secure Cookies
SESSION_COOKIE_SECURE = True  # Ensure cookies are only sent over HTTPS
CSRF_COOKIE_SECURE = True  # Ensure CSRF tokens are only sent over HTTPS

# Additional Security Headers
X_FRAME_OPTIONS = "DENY"  # Protect against clickjacking
SECURE_CONTENT_TYPE_NOSNIFF = True  # Prevent browsers from sniffing MIME types
SECURE_BROWSER_XSS_FILTER = True  # Enable XSS protection in modern browsers

# Debugging and Production Config
DEBUG = False  # Ensure DEBUG is set to False in production
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']  # Add your domain(s)
