# Jake's Second Brain 🧠

A simple, fast system for capturing and retrieving thoughts, articles, ideas, and everything worth remembering.

## How to Use

### Capture (via Telegram)
Just message Clawdbot with:
- `save: [your thought or link]` — I'll categorize and store it
- `idea: [your idea]` — Saves to ideas
- `article: [url]` — I'll fetch the title and summary
- `learned: [what you learned]` — Saves to learnings
- `quote: [the quote]` — Saves to quotes
- Or just send me anything and say "remember this"

### Browse (via Web UI)
Open `index.html` in a browser to:
- Search across everything
- Filter by category
- Click entries for full view

### Categories
- 💭 **Thoughts** — Quick ideas and reflections
- 📄 **Articles** — Saved links and reading material  
- 💡 **Ideas** — Project and startup ideas
- 🧠 **Learnings** — Things you've learned
- 👤 **People** — Notes about people
- 💬 **Quotes** — Things that resonated
- 🔗 **Resources** — Tools, references, useful stuff

## File Structure
```
brain/
├── index.html      # Web UI
├── data.json       # All entries (source of truth)
├── add_entry.py    # CLI tool to add entries
└── README.md       # This file
```

## Importing Existing Notes
Send your Apple Notes export or paste notes to Clawdbot — I'll parse and import them.
