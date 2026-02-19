#!/usr/bin/env python3
"""
Add an entry to Jake's Brain.
Usage: python add_entry.py --category thoughts --title "Title" --content "Content" [--url URL] [--tags tag1,tag2]
"""

import json
import argparse
import uuid
from datetime import datetime, timezone
from pathlib import Path

BRAIN_DIR = Path(__file__).parent
DATA_FILE = BRAIN_DIR / "data.json"

def load_data():
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def save_data(data):
    data['lastUpdated'] = datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def add_entry(category, title, content, url=None, tags=None):
    data = load_data()
    
    entry = {
        "id": str(uuid.uuid4())[:8],
        "category": category,
        "title": title,
        "content": content,
        "createdAt": datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z'),
        "tags": tags or []
    }
    
    if url:
        entry["url"] = url
    
    data['entries'].append(entry)
    save_data(data)
    
    print(f"✅ Added: {title} [{category}]")
    return entry

def main():
    parser = argparse.ArgumentParser(description="Add entry to Jake's Brain")
    parser.add_argument('--category', '-c', required=True, 
                        choices=['thoughts', 'articles', 'ideas', 'learnings', 'people', 'quotes', 'resources', 'bookmarks'])
    parser.add_argument('--title', '-t', required=True)
    parser.add_argument('--content', required=True)
    parser.add_argument('--url', '-u')
    parser.add_argument('--tags', help='Comma-separated tags')
    
    args = parser.parse_args()
    tags = [t.strip() for t in args.tags.split(',')] if args.tags else []
    
    add_entry(args.category, args.title, args.content, args.url, tags)

if __name__ == '__main__':
    main()
