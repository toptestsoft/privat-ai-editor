#!/usr/bin/env python3
"""
Автопостинг: берёт СЛЕДУЮЩИЙ неопубликованный пост из posts_week.md
и шлёт в канал toptestsoft через бота.
Прогресс хранится в posted.txt (номер последнего опубликованного поста).
Токен берётся из TELEGRAM_BOT_TOKEN либо из файла .token.
Запуск: python3 auto_post.py
"""
import os, re, sys, urllib.request, json

BASE = os.path.dirname(os.path.abspath(__file__))
TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
if not TOKEN:
    try:
        TOKEN = open(os.path.join(BASE, ".token"), encoding="utf-8").read().strip()
    except FileNotFoundError:
        print("ОШИБКА: нет TELEGRAM_BOT_TOKEN и нет файла .token"); sys.exit(1)

CHANNEL = os.environ.get("CHANNEL", "-1004465637168")
POSTS_FILE = os.path.join(BASE, "posts_week.md")
PROGRESS = os.path.join(BASE, "posted.txt")

def send(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    for ch in [text[i:i+4000] for i in range(0, len(text), 4000)]:
        data = json.dumps({"chat_id": CHANNEL, "text": ch}).encode()
        req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=30) as r:
            res = json.loads(r.read())
            if not res.get("ok"):
                raise RuntimeError(str(res))

# парсим посты "## Пост N — ..."
md = open(POSTS_FILE, encoding="utf-8").read()
parts = re.split(r"\n## Пост (\d+).*?\n", md)
# parts: [header, num1, body1, num2, body2, ...]
entries = []
for i in range(1, len(parts), 2):
    num = int(parts[i]); body = parts[i+1].strip()
    if body and not body.startswith("Что постить дальше"):
        entries.append((num, body))
entries.sort()

# прогресс
last = 0
if os.path.exists(PROGRESS):
    try: last = int(open(PROGRESS, encoding="utf-8").read().strip() or 0)
    except: last = 0

next_entry = next((e for e in entries if e[0] > last), None)
if not next_entry:
    print("Все посты уже опубликованы (последний №%d)." % last)
    sys.exit(0)

num, text = next_entry
print(f">>> Пост №{num} ({len(text)} симв.) -> канал {CHANNEL}")
send(text)
open(PROGRESS, "w", encoding="utf-8").write(str(num))
print(f"Опубликовано. Следующий раз будет №{num+1}.")
