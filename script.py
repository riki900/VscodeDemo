""" 
    requests module sandbox
"""

import requests


r = requests.get("https://coreyms.com")
print(r.status_code)
