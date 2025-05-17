import os
import feedparser
from telegram import Bot

BOT_TOKEN = os.getenv('BOT_TOKEN')
CHANNEL_ID = os.getenv('CHANNEL_ID')  # Like '@deals_channel'
RSS_URL = "PASTE_YOUR_RSS_HERE"  # e.g. 'https://www.dealsofday.com/rss'

def send_deal():
    bot = Bot(token=BOT_TOKEN)
    feed = feedparser.parse(RSS_URL)
    latest = feed.entries[0]
    message = f"🛍️ {latest.title}\n\n{latest.description}\n🔗 {latest.link}"
    bot.send_message(chat_id=CHANNEL_ID, text=message)

if __name__ == "__main__":
    send_deal()
