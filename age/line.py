import base64
import hashlib
import hmac

channel_secret = '...' # Channel secret string
body = '...' # Request body string
hash = hmac.new(channel_secret.encode('utf-8'),body.encode('utf-8'), hashlib.sha256).digest()
signature = base64.b64encode(hash)
# Compare X-Line-Signature request header and the signature