#!/usr/bin/env python3
import json
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone

TOPICS = {
    "头条": "https://news.google.com/rss?hl=zh-CN&gl=CN&ceid=CN:zh-Hans",
    "世界": "https://news.google.com/rss/headlines/section/topic/WORLD?hl=zh-CN&gl=CN&ceid=CN:zh-Hans",
    "中国": "https://news.google.com/rss/headlines/section/topic/NATION?hl=zh-CN&gl=CN&ceid=CN:zh-Hans",
    "商业": "https://news.google.com/rss/headlines/section/topic/BUSINESS?hl=zh-CN&gl=CN&ceid=CN:zh-Hans",
    "科技": "https://news.google.com/rss/headlines/section/topic/TECHNOLOGY?hl=zh-CN&gl=CN&ceid=CN:zh-Hans",
    "娱乐": "https://news.google.com/rss/headlines/section/topic/ENTERTAINMENT?hl=zh-CN&gl=CN&ceid=CN:zh-Hans",
    "体育": "https://news.google.com/rss/headlines/section/topic/SPORTS?hl=zh-CN&gl=CN&ceid=CN:zh-Hans",
    "健康": "https://news.google.com/rss/headlines/section/topic/HEALTH?hl=zh-CN&gl=CN&ceid=CN:zh-Hans",
}


def parse_rss(url: str, limit: int = 30):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=20) as resp:
        xml_data = resp.read()

    root = ET.fromstring(xml_data)
    items = []
    for item in root.findall("./channel/item")[:limit]:
        items.append(
            {
                "title": (item.findtext("title") or "").strip(),
                "link": (item.findtext("link") or "").strip(),
                "source": (item.findtext("source") or "").strip(),
                "published": (item.findtext("pubDate") or "").strip(),
            }
        )
    return items


def main():
    categories = {}
    errors = {}
    for name, url in TOPICS.items():
        try:
            categories[name] = parse_rss(url, 30)
        except Exception as e:
            categories[name] = []
            errors[name] = str(e)

    output = {
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S"),
        "categories": categories,
        "errors": errors,
    }
    with open("data/news.json", "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
