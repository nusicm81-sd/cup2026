import json
import random

# بيانات تجريبية متغيرة
def get_random_data():
    return [
        {
            "group": "المجموعة A",
            "teams": [
                {"name": "السعودية", "pts": random.randint(0, 9)},
                {"name": "مصر", "pts": random.randint(0, 9)}
            ]
        },
        {
            "group": "المجموعة B",
            "teams": [
                {"name": "البرازيل", "pts": random.randint(0, 9)},
                {"name": "ألمانيا", "pts": random.randint(0, 9)}
            ]
        }
    ]

# كتابة الملف
with open('groups.json', 'w', encoding='utf-8') as f:
    json.dump(get_random_data(), f, ensure_ascii=False, indent=4)
