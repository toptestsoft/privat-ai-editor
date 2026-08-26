#!/usr/bin/env python3
"""
Постит готовые посты из telegram_posts.md в канал через Telegram-бота.
Токен берётся из переменной окружения TELEGRAM_BOT_TOKEN (не хардкодим!).
Канал — из CHANNEL (по умолчанию @toptestsoft).
Запуск:
  TELEGRAM_BOT_TOKEN=123456:ABC-DEF... python3 post_to_telegram.py
"""
import os, re, sys, urllib.request, json

TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
if not TOKEN:
    # читаем из локального файла .token (не в репозитории)
    tok_path = os.path.join(os.path.dirname(__file__), ".token")
    try:
        TOKEN = open(tok_path, encoding="utf-8").read().strip()
    except FileNotFoundError:
        pass
CHANNEL = os.environ.get("CHANNEL", "-1004465637168")  # приватный канал toptestsoft (числовой ID)
POSTS_FILE = os.path.join(os.path.dirname(__file__), "telegram_posts.md")

if not TOKEN:
    print("ОШИБКА: не задан TELEGRAM_BOT_TOKEN")
    print('Запусти так: TELEGRAM_BOT_TOKEN=твой_токен python3 post_to_telegram.py')
    sys.exit(1)

def send(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    # режем слишком длинные посты (лимит Telegram ~4096)
    chunks = [text[i:i+4000] for i in range(0, len(text), 4000)]
    last = None
    for ch in chunks:
        data = json.dumps({"chat_id": CHANNEL, "text": ch}).encode()
        req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=30) as r:
            last = json.loads(r.read())
    return last

# Парсим только секции "## Пост N — ..."
md = open(POSTS_FILE, encoding="utf-8").read()
parts = re.split(r"\n## Пост \d+.*?\n", md)
# parts[0] — заголовок файла, дальше — тела постов 1,2,3
posts = [p.strip() for p in parts[1:] if p.strip()]
# отсекаем блок "Что постить дальше", если попал
posts = [p for p in posts if not p.startswith("Что постить дальше")]

print(f"Найдено постов: {len(posts)}")
for i, post in enumerate(posts, 1):
    print(f">>> отправляю пост {i} ({len(post)} симв.)...")
    try:
        res = send(post)
        print("   OK" if res and res.get("ok") else "   FAIL: " + str(res))
    except Exception as e:
        print("   ERROR:", e)
    print()
print("Готово.")
