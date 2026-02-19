#!/usr/bin/env python3
"""Batch add entries to Jake's Brain"""
import json
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

def add_entry(data, category, title, content, tags=None, url=None):
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
    print(f"✅ Added: {title}")

data = load_data()

# Learning Todo
add_entry(data, "resources", "Startup Learning Path", """
**Courses & Content:**
- [ ] Y Combinator Startup School
- [ ] Paul Graham - Schlep Filter essay
- [ ] Paul Graham full article list: paulgraham.com/articles.html
- [ ] How to Get Startup Ideas: paulgraham.com/startupideas.html
- [ ] Lenny's Podcast (product/growth)

**Videos:**
- [ ] Vibe Coding Tutorial: youtube.com/watch?v=2FJlhoDYNPE
- [ ] "Give me 9 minutes and I'll teach you how to successfully launch a new app"

**Practice:**
- Talk to 5-10 users weekly
- Ask: "What did you try before?" / "What's annoying about this today?" / "What happens if this isn't solved?"
- Kill features ruthlessly
""", ["learning", "startup", "todo"])

# Paul Graham Wisdom
add_entry(data, "learnings", "Paul Graham - How to Get Startup Ideas", """
**Core principles:**
- Don't try to think up ideas—NOTICE problems you personally experience
- Live in the future, then build what's missing
- Ideas are noticed, not invented

**What makes a good idea:**
- Founders want it themselves
- Founders can build it
- Others underestimate it
- Small group wants it BADLY > large group mildly interested
- "A well, not a puddle"

**Key test:** Who needs this RIGHT NOW?

**Filters to turn OFF:**
1. Schlep filter - fear of messy, tedious work
2. Unsexy filter - boring but valuable domains
3. "Could this be a big company" filter

**Good trick:** Ask what you wish someone else would build, so you could use it.

**Crowded markets can be good** if you see what competitors overlook.
""", ["startup", "paul-graham", "ideas"], "https://paulgraham.com/startupideas.html")

add_entry(data, "learnings", "YC Talk - Should You Start a Startup?", """
**Most important trait: RESILIENCE**
- Startups require enduring rejection and slow progress
- Confidence ≠ resilience; quiet founders can be toughest

**Ask: "What do I have to lose?"**
- Worst case: ~1 year, little/no pay, startup fails
- If you can't live with worst case, anxiety will hurt execution

**Motivation matters less than you think**
- Starting for money or curiosity is fine
- What sustains you: interest in problem + love for co-founders

**Startup experience is valuable even if you fail**
- Learn sales, product, leadership fast
- Former founders are highly valued hires

**Signal of a good idea:**
- A few users who LOVE it > many who are indifferent
- One passionate user beats a big waitlist

**When to quit your job:**
- You're energized by side projects, drained by your job
- Great co-founder + mutual desire to start is RARE—act on it
""", ["startup", "yc", "advice"])

add_entry(data, "learnings", "Breaking Out of FAANG", """
**Common myths:**
- "I'll work on hardest problems at scale" → Most jobs are narrow, get killed
- "FAANG experience transfers to startups" → Often doesn't; must unlearn process
- "VCs fund ex-Google easily" → Brand helps briefly, then fades

**The FAANG trap:**
- Highly gamified retention (levels, promos, bonuses)
- Equity vesting = loss aversion → hard to leave
- Lifestyle inflation = no runway
- Talent "warehoused" on low-impact projects

**Warning sign to quit:**
You hate your job and fantasize daily about quitting.

**How to avoid getting stuck:**
- Keep personal burn low
- Have clear plan (what you want + when you'll leave)
- Remember: good engineers can usually come back

**Bottom line:**
If happy → stay. If miserable and staying "because math" → break the spell and leave.
""", ["career", "faang", "startup"])

# Sessions detailed notes
add_entry(data, "ideas", "Sessions - Product Details", """
**Core Loop:**
Morning + Night is the correct core loop.

**Morning session (5-10 min):**
- Purpose: reduce cognitive overload before day starts
- Outcome: clear priorities
- Prompts: "What matters today?" / "Top 1-2 non-negotiables?" / "What might get in the way?"

**Night session (5-10 min):**
- Purpose: close loops, reduce mental residue
- Outcome: emotional + cognitive closure
- Prompts: "What happened today?" / "What worked/didn't?" / "What can you let go of?"

**Key insight:** This is not therapy. It's mental bookkeeping.

**What the AI should be:** Calm, curious, slightly structured, emotionally neutral but warm
**What it should NOT be:** Therapist, life coach, motivational speaker, advice-heavy

**Key rule:** The AI should never talk for long. It exists to PULL, not push.
""", ["sessions", "product", "ai-voice"])

add_entry(data, "ideas", "Sessions - Feature Backlog", """
**Todo:**
- [ ] Time injections during calls
- [ ] Specific session types (Morning goal builder, Evening reflection)
- [ ] Calendar day scheduling
- [ ] Session edit/delete above past calls
- [ ] Allow delete of session instances
- [ ] Fix: daily scheduled sessions not showing for tomorrow
- [ ] 'Skip' feature that doesn't affect rest of sessions
- [ ] Number of sessions tracker (broken)
- [ ] Calendar picker buggy
- [ ] Store insights even if session deleted
- [ ] OpenAI Realtime phone number setup

**VAPI observations:**
- Interrupts sometimes
- Some gibberish at beginning
- Ask one question at a time
- Use 'purpose' to guide the session
""", ["sessions", "todo", "features"])

# Plannr detailed notes  
add_entry(data, "ideas", "Plannr - Full Pitch", """
**The Problem:**
- Group chats are terrible for making plans
- Messages get buried, ideas get lost, no one knows who's coming
- When 15-30 people involved, almost impossible to coordinate

**The Solution:**
Plannr replaces the group chat with a shared planning feed and calendar.
- Anyone can propose a plan
- Everyone marks: In / Tentative / Out
- Instantly see if there's enough interest
- All plans in one place, not lost in messages

**How It Works:**
1. Join or create a group with friends
2. Propose a plan ("Party at John's on Friday")
3. Plans appear in shared group feed
4. Members RSVP in one tap
5. Plans gain momentum or naturally die—no endless back-and-forth

**Key Feature - Shared Group Calendar:**
- Shows what group is doing each day
- Displays each friend's status
- Makes conflicts immediately obvious

**Initial Users:** College students - friend groups, parties, trips, clubs

**Ad Concept:** Chaotic group chat trying to plan → Cut to Plannr: one plan, clear RSVPs, done.
""", ["plannr", "pitch", "startup"])

add_entry(data, "ideas", "Plannr - Feature Backlog", """
**Todo:**
- [ ] Notifications
- [ ] Comments on plans
- [ ] "Idea" tab (coming soon)
- [ ] Tutorial/info page
- [ ] Revenue and marketing plan
- [ ] Voting process for proposed plans
- [ ] "When is everyone free" feature

**Future:**
- Activity and event suggestions based on location, preferences, group size
""", ["plannr", "todo", "features"])

# Technical learning
add_entry(data, "resources", "Technical Stack to Learn", """
**Frontend:**
- React + Next.js
- Tailwind CSS

**Backend:**
- Python FastAPI
- REST APIs
- Background jobs

**Database:**
- PostgreSQL
- Prisma ORM

**AI:**
- LLM APIs
- Prompting and eval
- Simple agents

**Practice Project - Build a product with:**
- Auth
- Database
- Payments (Stripe test mode)
- Deployed

**Resources:**
- "Build a SaaS" YouTube tutorials
- Open source projects
- Documentation
""", ["technical", "learning", "stack"])

# Vibe Coding notes
add_entry(data, "resources", "Vibe Coding - Tools & Techniques", """
**AI Coding Models:**
- Claude Code
- Codex
- Gemini
- sandbox.dev
- vibecodeapp.com (select model + stack, has preview)

**Key Tips:**
- Context management is important
- Use /clear and /cost commands
- Commit early and often
- Give instructions: "ask me questions to clarify requirements"

**Landing Page Trick:**
- Create landing page to validate idea
- Use Tally.so for forms, embed in app
- Upload image as design inspiration

**Databases:**
- InstantDB (instantdb.com) - good for auth + realtime
- Research docs for implementation

**Tools:**
- Excalidraw - draw prototypes, give to model
- Three.js for games
- kreai.ai for image models

**Deploy:**
Download code → push to GitHub → deploy to Vercel
""", ["tools", "ai-coding", "vibe-coding"], "https://www.youtube.com/watch?v=2FJlhoDYNPE")

# Product thinking
add_entry(data, "learnings", "Product Thinking Framework", """
**User Discovery:**
- Talk to 5-10 users weekly
- Ask: "What did you try before?"
- Ask: "What's annoying about this today?"
- Ask: "What happens if this isn't solved?"

**MVP Principles:**
- SLC over MVP (Simple, Lovable, Complete)
- Kill features ruthlessly
- One core workflow done well

**Metrics that matter:**
- Activation
- Retention
- Feedback loops

**Launch Channels:**
- Product Hunt
- Hacker News
- Twitter
- Subreddit communities
""", ["product", "startup", "users"])

# Other startup ideas
add_entry(data, "ideas", "Political Matching App", """
**Problem:** Hard to figure out who to vote for in every election besides presidential.

**Solution:** 
- Swipe left/right on issues (gun rights, abortion, etc.) OR fill out survey
- App tells you who aligns with you in EVERY election
- Hub with candidate bios and news
- News section for political updates

**Why it matters:** Makes informed voting accessible beyond just the presidential race.
""", ["startup", "civic-tech", "idea"])

add_entry(data, "ideas", "Personalized News Platform", """
**Concept:**
- User selects topics (general or very specific)
- Shows news stories and/or newsletter summaries for those topics
- Email/feed/newsletter/audio delivery options

**Killer Feature - Commute School:**
- Reads news in your headphones during commute
- Interactive - can ask questions, go deeper
- Voice-first news consumption

**Status:** Building as "Briefing" app
""", ["startup", "news", "ai"])

# Opportunity notes
add_entry(data, "people", "Startup/Job Opportunities", """
**Contacts:**
- Brian's friend Spencer - "pays well and is cool, guy sucks"
- Quinn Lefkofsky's dad - Tempus ("I could really see myself working here")

**Interview tip:** Say at the end: "I could really see myself working here"
""", ["networking", "opportunities"])

add_entry(data, "learnings", "How to Create AI Startup", """
1. Find out the SPECIFIC things people do that you're solving for
2. Understand: How would the BEST person do this?
3. Work backwards from there

**Key insight:** It is almost always better than a regular job.

**Strategy:**
- Make something popular (even if you don't know monetization yet)
- GET ON THE WAVE EARLY
- Consider: Quantum computing? Enterprise software?

**Important:** Get a cofounder
""", ["startup", "ai", "advice"])

save_data(data)
print(f"\n✅ Added {len(data['entries'])} total entries")
