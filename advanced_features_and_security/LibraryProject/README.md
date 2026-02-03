# Security Review & Deployment

## Security Review
The following security measures have been implemented:

1.  **HTTPS Enforcement**
    - `SECURE_SSL_REDIRECT = True`: Redirects all non-HTTPS requests to HTTPS.
    - `SECURE_HSTS_SECONDS = 31536000`: Enforces HSTS for 1 year.
    - `SECURE_HSTS_INCLUDE_SUBDOMAINS = True`: Applies HSTS to all subdomains.
    - `SECURE_HSTS_PRELOAD = True`: Allows preloading HSTS.

2.  **Secure Cookies**
    - `SESSION_COOKIE_SECURE = True`: Session cookies are only sent over HTTPS.
    - `CSRF_COOKIE_SECURE = True`: CSRF cookies are only sent over HTTPS.

3.  **Secure Headers**
    - `X_FRAME_OPTIONS = 'DENY'`: Prevents clickjacking.
    - `SECURE_CONTENT_TYPE_NOSNIFF = True`: Prevents MIME-sniffing.
    - `SECURE_BROWSER_XSS_FILTER = True`: Enables browser XSS filtering.

4.  **Content Security Policy (CSP)**
    - `CSP_DEFAULT_SRC`: Restricts content sources to 'self' to mitigate XSS.

## Deployment Configuration
To configure your web server (Nginx/Apache) for HTTPS:

### Nginx Example
```nginx
server {
    listen 80;
    server_name example.com;
    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl http2;
    server_name example.com;

    ssl_certificate /path/to/cert.pem;
    ssl_certificate_key /path/to/key.pem;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```
Ensure `SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')` is in `settings.py` if using a proxy.