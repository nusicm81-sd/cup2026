import feedparser
import json
import requests
from bs4 import BeautifulSoup

# 1. جلب الأخبار (كما فعلنا سابقاً)
url = 'https://sports.yahoo.com/soccer/rss/'
feed = feedparser.parse(url)
news_list = [{'title': entry.title, 'link': entry.link} for entry in feed.entries[:5]]

# 2. جلب جدول الترتيب (محاكاة لترتيب المجموعات)
# ملاحظة: سنقوم بجلب بيانات مبسطة، يمكنك لاحقاً تطويرها لتناسب موقع ياهو بدقة
groups_data = [
    {"group": "المجموعة A", "teams": [{"name": "السعودية", "pts": 6}, {"name": "مصر", "pts": 3}]},
    {"group": "المجموعة B", "teams": [{"name": "البرازيل", "pts": 4}, {"name": "ألمانيا", "pts": 4}]}
]

# حفظ البيانات في ملفات JSON
with open('news.json', 'w', encoding='utf-8') as f:
    json.dump(news_list, f, ensure_ascii=False, indent=4)

with open('groups.json', 'w', encoding='utf-8') as f:
    json.dump(groups_data, f, ensure_ascii=False, indent=4)
