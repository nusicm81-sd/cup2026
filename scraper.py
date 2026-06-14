import feedparser
import json
import requests
from bs4 import BeautifulSoup

# 1. جلب الأخبار
url = 'https://sports.yahoo.com/soccer/rss/'
feed = feedparser.parse(url)
news_list = [{'title': entry.title, 'link': entry.link} for entry in feed.entries[:5]]

# 2. هنا نقوم بجلب جدول الترتيب الحقيقي
# سنقوم بتحديث هذا الجزء ليقرأ صفحة "Standings" من ياهو
# (هذا الكود هو البداية البرمجية لجلب البيانات الحقيقية)
groups_data = [
    {"group": "المجموعة A", "teams": ["السعودية", "مصر", "الأوروغواي", "روسيا"]},
    {"group": "المجموعة B", "teams": ["البرازيل", "ألمانيا", "فرنسا", "الأرجنتين"]}
]

# حفظ البيانات
with open('news.json', 'w', encoding='utf-8') as f:
    json.dump(news_list, f, ensure_ascii=False, indent=4)
with open('groups.json', 'w', encoding='utf-8') as f:
    json.dump(groups_data, f, ensure_ascii=False, indent=4)
