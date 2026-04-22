import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID", "123456789"))

PLANS = {
    "basic": {"price": "10$", "limit": 100},
    "pro": {"price": "25$", "limit": 500},
    "vip": {"price": "50$", "limit": 2000}
}