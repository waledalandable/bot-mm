import os

BOT_TOKEN = os.getenv("7787809968:AAHpKbErc_GmNfFaK0uLmlD__4taeNojSLQ ")
ADMIN_ID = int(os.getenv("ADMIN_ID", "7496673554"))

PLANS = {
    "basic": {"price": "10$", "limit": 100},
    "pro": {"price": "25$", "limit": 500},
    "vip": {"price": "50$", "limit": 2000}
}
