# Build Your Own AI Agent Company

**A practical guide + starter kit for building a coordinated Telegram team of specialist AI agents with Python and the OpenAI API.**

Launch version: 1.0  
Suggested launch price: **$29**

---

## Who This Is For

This kit is for builders who want to create a small AI-agent team that works in a Telegram group:

- A manager/router agent reads the user request.
- The manager delegates to the right specialist.
- Specialists only get the tools they need.
- The system tracks daily budget usage.
- Risky actions require human approval.
- Multi-step work passes one agent's output into the next.
- The whole thing can run on Railway with persistent state.

This is not an abstract agent-theory course. Those are plentiful. Congrats to the internet.

This is the practical version: architecture, prompts, code patterns, deployment steps, and the annoying Telegram gotchas that usually waste your afternoon.

---

# 1. Demand Validation

## Bottom Line

There is enough market pull to launch this as a $29 digital product.

Builders are interested in AI agents, but most tutorials either stay too abstract or jump into heavy orchestration frameworks before the buyer understands the core mechanics. A Telegram-based specialist-agent team is concrete, visual, and easy to demo.

## Demand Signals

- The AI-agent market is growing quickly. Grand View Research estimated the AI agents market at **$7.6B in 2025** and projected it to reach **$182.9B by 2033**, a **49.6% CAGR**.
- Developers are actively evaluating agents, orchestration, tool use, and AI workflow reliability. Stack Overflow's 2025 Developer Survey includes dedicated AI-agent usage and challenge sections.
- Existing agent courses show demand. DeepLearning.AI/Coursera's multi-agent systems course with crewAI is a visible example.
- Buyers still need implementation help around boring-but-critical details: Telegram bot setup, privacy mode, state persistence, tool permissions, budget metering, and human approval gates.

## Competitors

### 1. DeepLearning.AI / Coursera Multi-Agent Courses

Strengths:

- Strong brand.
- Good conceptual overview.
- Uses known orchestration frameworks like crewAI.

Gap:

- Less focused on shipping a small personal/company AI team in Telegram.
- Not positioned as a starter kit with deployment, budget controls, and production gotchas.

### 2. CrewAI / LangChain Tutorials and Courses

Strengths:

- Broad ecosystem coverage.
- Many examples and templates.

Gap:

- Often framework-heavy.
- Beginners can copy code without understanding manager routing, least-privilege tools, state, or human approval.
- Many examples are local demos, not a practical messaging interface people can actually use.

## Positioning

Sell this as:

> Build a working AI-agent company in Telegram: one manager, multiple specialist bots, real tools, budget limits, approval gates, persistent memory, and Railway deployment.

---

# 2. What You Are Building

You will build a Telegram group containing a small team of AI agents.

Example team:

- **Miles — Manager Agent**  
  Reads the request, chooses the specialist, coordinates multi-step work, and summarizes results.

- **Quill — Writing Agent**  
  Writes hooks, emails, landing-page copy, and short-form content.

- **Sage — Memory Agent**  
  Stores and recalls long-term user preferences and facts.

- **Herald — Research Agent**  
  Searches the web and summarizes current information.

- **Roster — Task Agent**  
  Manages tasks, checklists, and simple project status.

- **Ledger — Crypto Agent**  
  Pulls crypto prices and reports them cleanly.

You can change the roles. The pattern matters more than the names.

## The Core Idea

An agent is not magic.

In this kit:

> **Agent = system prompt + model + curated tools + routing rules + state.**

That is it.

No incense. No 47-node YAML labyrinth.

---

# 3. Architecture

## High-Level Flow

```text
User message in Telegram group
        |
        v
Manager/router agent
        |
        |-- decides: answer directly?
        |-- decides: delegate to specialist?
        |-- decides: ask human approval?
        |
        v
Specialist agent
        |
        |-- uses only allowed tools
        |-- returns structured output
        |
        v
Manager agent
        |
        |-- passes output to next agent if needed
        |-- summarizes final answer
        |
        v
Telegram group response
```

## Components

### 1. Telegram Interface

Use `python-telegram-bot` to receive messages and send replies.

Telegram is good for this product because:

- People understand group chats.
- Multiple bots can live in the same group.
- The demo is easy to explain.
- BotFather setup is simple.

Telegram is also annoying because:

- Privacy mode can hide group messages from bots.
- Multiple bots can duplicate work if routing is sloppy.
- Long-running state disappears unless you persist it.

We handle those later.

### 2. Manager/Router

The manager decides who should handle a request.

The manager should have:

- A clear role prompt.
- Access to delegation tools.
- Access to memory if needed.
- No direct access to dangerous tools unless required.
- Instructions to avoid duplicate delegation.

Example:

```text
User: @MilesBot ask Quill for a cold email hook and then ask Sage to remember I prefer short copy.

Miles:
1. Delegates the hook request to Quill.
2. Sends the preference to Sage.
3. Combines both results into one final response.
```

### 3. Specialists

Specialists are narrow.

Good specialist:

- Has a specific job.
- Has a distinct tone.
- Has only the tools needed for that job.
- Refuses or redirects work outside its role.

Bad specialist:

- Can do everything.
- Has every tool.
- Makes routing pointless.

If every agent can do every job, you did not build a team. You built one confused intern wearing fake mustaches.

### 4. Tool Layer

Tools are Python functions the model can call.

Examples:

- `get_weather(city)`
- `search_web(query)`
- `create_task(title, due_date)`
- `recall_memories(query)`
- `save_memory(memory)`
- `get_crypto_price(coin_id)`

Each specialist gets a curated list.

Least privilege matters.

Quill does not need task-writing permissions. Ledger does not need to save memories. Herald does not need to approve purchases.

### 5. State Store

You need persistent state for:

- Daily token/cost budget.
- Memories.
- Task list.
- Pending human approvals.
- Conversation summaries.
- Agent handoff records.

For a starter kit, use SQLite.

It is boring. That is good.

On Railway, store SQLite on a persistent volume.

### 6. Budget Meter

Every OpenAI call should be metered.

Track:

- Date.
- Agent name.
- Model.
- Input tokens.
- Output tokens.
- Estimated cost.
- Request purpose.

Block or warn when the daily budget is reached.

### 7. Human-in-the-Loop Gate

Some actions should require approval.

Examples:

- Sending an email.
- Posting publicly.
- Buying anything.
- Deleting data.
- Calling external APIs with side effects.
- Sharing private information.

The agent prepares a proposed action. The human approves or rejects.

```text
Agent: I can send this email. Approval required.

Proposed action:
To: alex@example.com
Subject: Quick idea for Acme
Body: ...

Reply APPROVE abc123 to send, or REJECT abc123.
```

---

# 4. Project Structure

Use this starter layout:

```text
agent-company/
  main.py
  agents.py
  tools.py
  budget.py
  state.py
  approvals.py
  requirements.txt
  .env.example
  README.md
```

## requirements.txt

```txt
python-telegram-bot==21.6
openai==1.51.2
requests==2.32.3
python-dotenv==1.0.1
```

## .env.example

```env
OPENAI_API_KEY=sk-your-key
TELEGRAM_MANAGER_BOT_TOKEN=your-manager-token
TELEGRAM_QUILL_BOT_TOKEN=optional-specialist-token
TELEGRAM_SAGE_BOT_TOKEN=optional-specialist-token
TELEGRAM_HERALD_BOT_TOKEN=optional-specialist-token
DATABASE_PATH=/data/agent_company.sqlite3
DAILY_BUDGET_USD=2.00
FAST_MODEL=gpt-4o-mini
SMART_MODEL=gpt-4o
```

For the smallest working version, you only need one Telegram bot: the manager.

The manager can internally delegate to specialist prompts without each specialist having its own bot account. Add separate specialist bots later if you want the full theater production.

---

# 5. Step-by-Step Build Path

## Step 1: Create Your Telegram Bot with BotFather

1. Open Telegram.
2. Search for `@BotFather`.
3. Send `/newbot`.
4. Choose a display name, like `Miles Manager`.
5. Choose a username ending in `bot`, like `YourMilesBot`.
6. Copy the bot token.
7. Put it in `.env` as:

```env
TELEGRAM_MANAGER_BOT_TOKEN=123456:ABC...
```

## Step 2: Disable Privacy Mode for Group Use

This is the first major gotcha.

By default, Telegram bots in groups do not see every message. They only see commands, replies, and mentions.

For a group AI team, you usually want the manager to see relevant messages.

In BotFather:

1. Send `/mybots`.
2. Pick your bot.
3. Go to **Bot Settings**.
4. Go to **Group Privacy**.
5. Turn privacy **off**.

If privacy mode stays on, your bot may appear broken. It is not broken. Telegram is just doing Telegram things.

## Step 3: Create a Telegram Group

1. Create a new Telegram group.
2. Add your manager bot.
3. Make sure the bot can read messages.
4. Test with:

```text
@YourMilesBot hello
```

## Step 4: Install Python Dependencies

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

On Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Step 5: Create SQLite State

Use SQLite for the starter version.

`state.py`:

```python
import os
import sqlite3
from datetime import datetime, timezone

DATABASE_PATH = os.getenv("DATABASE_PATH", "agent_company.sqlite3")


def get_conn():
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    with get_conn() as conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS memories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
        """)
        conn.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            status TEXT NOT NULL DEFAULT 'open',
            created_at TEXT NOT NULL
        )
        """)
        conn.execute("""
        CREATE TABLE IF NOT EXISTS budget_events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            event_date TEXT NOT NULL,
            agent TEXT NOT NULL,
            model TEXT NOT NULL,
            input_tokens INTEGER NOT NULL DEFAULT 0,
            output_tokens INTEGER NOT NULL DEFAULT 0,
            estimated_cost_usd REAL NOT NULL DEFAULT 0,
            purpose TEXT,
            created_at TEXT NOT NULL
        )
        """)
        conn.execute("""
        CREATE TABLE IF NOT EXISTS approvals (
            id TEXT PRIMARY KEY,
            action_type TEXT NOT NULL,
            payload TEXT NOT NULL,
            status TEXT NOT NULL DEFAULT 'pending',
            created_at TEXT NOT NULL
        )
        """)


def now_iso():
    return datetime.now(timezone.utc).isoformat()
```

## Step 6: Add Tools

`tools.py`:

```python
import json
import requests
from state import get_conn, now_iso


def save_memory(content: str) -> str:
    if not content.strip():
        return "I need a real memory to save. Empty memories are just vibes."

    with get_conn() as conn:
        conn.execute(
            "INSERT INTO memories (content, created_at) VALUES (?, ?)",
            (content.strip(), now_iso()),
        )
    return "Saved that memory."


def recall_memories(query: str) -> str:
    # Simple starter version: keyword-ish recall. Upgrade to embeddings later.
    terms = [t.lower() for t in query.split() if len(t) > 2]
    with get_conn() as conn:
        rows = conn.execute(
            "SELECT content, created_at FROM memories ORDER BY id DESC LIMIT 50"
        ).fetchall()

    matches = []
    for row in rows:
        content = row["content"]
        lower = content.lower()
        if not terms or any(term in lower for term in terms):
            matches.append(f"- {content}")

    if not matches:
        return "No relevant memories found."
    return "Relevant memories:\n" + "\n".join(matches[:10])


def create_task(title: str) -> str:
    if not title.strip():
        return "I need a task title. 'Do stuff' is not a task."

    with get_conn() as conn:
        conn.execute(
            "INSERT INTO tasks (title, status, created_at) VALUES (?, 'open', ?)",
            (title.strip(), now_iso()),
        )
    return f"Added task: {title.strip()}"


def list_tasks() -> str:
    with get_conn() as conn:
        rows = conn.execute(
            "SELECT id, title, status FROM tasks ORDER BY id DESC LIMIT 20"
        ).fetchall()

    if not rows:
        return "No tasks found."

    return "Task list:\n" + "\n".join(
        f"- #{row['id']} [{row['status']}] {row['title']}" for row in rows
    )


def get_crypto_price(coin_id: str) -> str:
    """Get the current USD price for a cryptocurrency from CoinGecko.

    coin_id examples: bitcoin, ethereum, solana, dogecoin
    Uses CoinGecko's public simple price endpoint. No API key required for this starter.
    """
    coin_id = coin_id.strip().lower()
    if not coin_id:
        return "I need a CoinGecko coin id, like bitcoin, ethereum, or solana."

    try:
        response = requests.get(
            "https://api.coingecko.com/api/v3/simple/price",
            params={"ids": coin_id, "vs_currencies": "usd"},
            timeout=10,
        )
        response.raise_for_status()
        data = response.json()
    except requests.RequestException:
        return "I could not reach CoinGecko right now. Try again in a minute. Markets can wait. Barely."

    price = data.get(coin_id, {}).get("usd")
    if price is None:
        return f"I could not find a USD price for '{coin_id}'. Use the CoinGecko id, for example bitcoin or ethereum."

    return f"{coin_id} is trading at ${price:,.2f} USD."


def search_web(query: str) -> str:
    # Placeholder. Wire this to your chosen search provider.
    return "Search tool placeholder. Connect Tavily, SerpAPI, Brave Search, or your own search backend."
```

## Step 7: Add Budget Metering

`budget.py`:

```python
import os
from datetime import datetime, timezone
from state import get_conn, now_iso

DAILY_BUDGET_USD = float(os.getenv("DAILY_BUDGET_USD", "2.00"))

# Example prices. Check OpenAI pricing before launch. Prices change.
MODEL_PRICES_PER_1M = {
    "gpt-4o-mini": {"input": 0.15, "output": 0.60},
    "gpt-4o": {"input": 2.50, "output": 10.00},
}


def today_key():
    return datetime.now(timezone.utc).date().isoformat()


def estimate_cost(model: str, input_tokens: int, output_tokens: int) -> float:
    prices = MODEL_PRICES_PER_1M.get(model, MODEL_PRICES_PER_1M["gpt-4o-mini"])
    return (
        (input_tokens / 1_000_000) * prices["input"]
        + (output_tokens / 1_000_000) * prices["output"]
    )


def get_today_spend() -> float:
    with get_conn() as conn:
        row = conn.execute(
            "SELECT COALESCE(SUM(estimated_cost_usd), 0) AS total FROM budget_events WHERE event_date = ?",
            (today_key(),),
        ).fetchone()
    return float(row["total"] or 0)


def assert_budget_available() -> None:
    spend = get_today_spend()
    if spend >= DAILY_BUDGET_USD:
        raise RuntimeError(
            f"Daily AI budget reached (${spend:.4f}/${DAILY_BUDGET_USD:.2f}). Try again tomorrow or raise DAILY_BUDGET_USD."
        )


def record_usage(agent: str, model: str, input_tokens: int, output_tokens: int, purpose: str = ""):
    cost = estimate_cost(model, input_tokens, output_tokens)
    with get_conn() as conn:
        conn.execute(
            """
            INSERT INTO budget_events
            (event_date, agent, model, input_tokens, output_tokens, estimated_cost_usd, purpose, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (today_key(), agent, model, input_tokens, output_tokens, cost, purpose, now_iso()),
        )
    return cost
```

## Step 8: Define Agents

`agents.py`:

```python
import os

FAST_MODEL = os.getenv("FAST_MODEL", "gpt-4o-mini")
SMART_MODEL = os.getenv("SMART_MODEL", "gpt-4o")

MANAGER_INSTRUCTIONS = """
You are Miles, the manager/router for a small AI-agent company running in Telegram.

Your job:
- Understand the user's request.
- Decide whether to answer directly or delegate to a specialist.
- Use the fewest agents needed.
- Pass each task's output into the next task when chaining work.
- Avoid duplicate work.
- Ask for human approval before risky external actions.
- Summarize final results clearly.

Available specialist routes:
- writing: Quill handles copywriting, hooks, emails, landing pages, and editing.
- memory: Sage saves and recalls durable user preferences and facts.
- research: Herald handles current-events research and web summaries.
- tasks: Roster handles task lists and project checklists.
- crypto: Ledger handles cryptocurrency price lookups.

Distinct character line:
Miles is calm and managerial. Quill is sharp and useful. Sage is concise and careful. Herald is skeptical and source-minded. Roster is organized and direct. Ledger is a dry, precise markets-desk specialist.

If the user asks for multiple things, do them in order and pass prior outputs forward.
Sign off with "- Miles".
"""

SPECIALISTS = {
    "writing": {
        "name": "Quill",
        "label": "Quill (Writing Agent)",
        "model": FAST_MODEL,
        "tool_names": ["recall_memories"],
        "role": "Writes practical copy: hooks, emails, landing pages, outlines, and edits.",
        "persona": "You are Quill, a sharp writing specialist. Be useful, direct, and concrete. Avoid fluffy marketing sludge. Sign off with '- Quill'.",
    },
    "memory": {
        "name": "Sage",
        "label": "Sage (Memory Agent)",
        "model": FAST_MODEL,
        "tool_names": ["save_memory", "recall_memories"],
        "role": "Stores and recalls durable user preferences, facts, and project context.",
        "persona": "You are Sage, a careful memory specialist. Save only durable facts and preferences. Do not save secrets. Be concise. Sign off with '- Sage'.",
    },
    "research": {
        "name": "Herald",
        "label": "Herald (Research Agent)",
        "model": SMART_MODEL,
        "tool_names": ["search_web", "recall_memories"],
        "role": "Researches current information and summarizes it with caveats.",
        "persona": "You are Herald, a skeptical research specialist. Prefer current sources, note uncertainty, and do not overclaim. Sign off with '- Herald'.",
    },
    "tasks": {
        "name": "Roster",
        "label": "Roster (Task Agent)",
        "model": FAST_MODEL,
        "tool_names": ["create_task", "list_tasks", "recall_memories"],
        "role": "Creates, lists, and organizes tasks and checklists.",
        "persona": "You are Roster, an organized task specialist. Turn vague work into clear next actions. Sign off with '- Roster'.",
    },
    "crypto": {
        "name": "Ledger",
        "label": "Ledger (Crypto Agent)",
        "model": FAST_MODEL,
        "tool_names": ["get_crypto_price", "recall_memories"],
        "role": "Looks up current cryptocurrency prices and explains them cleanly.",
        "persona": "You are Ledger, a dry, precise markets-desk crypto specialist. Quote prices cleanly in USD. Do not give financial advice. Mention when a ticker/id may be ambiguous. Sign off with '- Ledger'.",
    },
}
```

## Step 9: Tool Registry and Execution

A tool registry prevents random function access.

```python
from tools import (
    save_memory,
    recall_memories,
    create_task,
    list_tasks,
    get_crypto_price,
    search_web,
)

TOOL_REGISTRY = {
    "save_memory": save_memory,
    "recall_memories": recall_memories,
    "create_task": create_task,
    "list_tasks": list_tasks,
    "get_crypto_price": get_crypto_price,
    "search_web": search_web,
}


def execute_tool(tool_name: str, arguments: dict, allowed_tool_names: list[str]) -> str:
    if tool_name not in allowed_tool_names:
        return f"Tool '{tool_name}' is not allowed for this agent. Least privilege is not optional."

    tool = TOOL_REGISTRY.get(tool_name)
    if tool is None:
        return f"Unknown tool: {tool_name}"

    try:
        return tool(**arguments)
    except TypeError as exc:
        return f"Tool argument error for {tool_name}: {exc}"
    except Exception:
        return f"Tool {tool_name} failed. Try again or simplify the request."
```

## Step 10: Human Approval Gate

`approvals.py`:

```python
import json
import secrets
from state import get_conn, now_iso

RISKY_ACTIONS = {
    "send_email",
    "post_public_message",
    "delete_data",
    "purchase",
}


def create_approval(action_type: str, payload: dict) -> str:
    approval_id = secrets.token_hex(4)
    with get_conn() as conn:
        conn.execute(
            "INSERT INTO approvals (id, action_type, payload, status, created_at) VALUES (?, ?, ?, 'pending', ?)",
            (approval_id, action_type, json.dumps(payload), now_iso()),
        )
    return approval_id


def format_approval_request(approval_id: str, action_type: str, payload: dict) -> str:
    pretty = json.dumps(payload, indent=2)
    return (
        f"Approval required for `{action_type}`.\n\n"
        f"Payload:\n```json\n{pretty}\n```\n\n"
        f"Reply `APPROVE {approval_id}` to approve or `REJECT {approval_id}` to reject."
    )


def resolve_approval(approval_id: str, approved: bool) -> str:
    status = "approved" if approved else "rejected"
    with get_conn() as conn:
        row = conn.execute(
            "SELECT id, status FROM approvals WHERE id = ?",
            (approval_id,),
        ).fetchone()
        if not row:
            return "Approval id not found."
        if row["status"] != "pending":
            return f"Approval {approval_id} was already {row['status']}."
        conn.execute(
            "UPDATE approvals SET status = ? WHERE id = ?",
            (status, approval_id),
        )
    return f"Approval {approval_id} {status}."
```

Use this pattern before any side-effect tool.

For example, do not let an agent send an email directly. Let it create a pending approval. Then execute the send only after approval.

---

# 6. Calling the OpenAI API

The modern OpenAI Python SDK uses a client object.

Minimal pattern:

```python
import os
from openai import OpenAI
from budget import assert_budget_available, record_usage

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def call_agent(agent_name: str, model: str, system_prompt: str, user_message: str, purpose: str = "") -> str:
    assert_budget_available()

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message},
        ],
    )

    usage = response.usage
    if usage:
        record_usage(
            agent=agent_name,
            model=model,
            input_tokens=usage.prompt_tokens or 0,
            output_tokens=usage.completion_tokens or 0,
            purpose=purpose,
        )

    return response.choices[0].message.content or ""
```

This version does not include automatic function calling. That is intentional for a starter.

For simple products, you can route first, execute known tools in Python, and pass tool output back into the agent prompt.

Clever automatic tool loops are useful later. They are also where people build expensive little goblins.

---

# 7. Simple Routing Without Frameworks

You do not need LangChain or CrewAI for the first version.

Use a plain routing classifier.

```python
from agents import SPECIALISTS, MANAGER_INSTRUCTIONS, FAST_MODEL
from llm import call_agent

ROUTER_PROMPT = """
Classify the user's request into exactly one route:
- writing
- memory
- research
- tasks
- crypto
- manager

Return only the route name.

Rules:
- Use writing for copy, emails, hooks, content, editing.
- Use memory for remember/save/recall preferences or durable facts.
- Use research for current events, market/news questions, web lookup.
- Use tasks for task lists, project plans, to-dos.
- Use crypto for cryptocurrency price lookups.
- Use manager for multi-step requests, ambiguous requests, or requests needing coordination.
"""


def route_message(user_message: str) -> str:
    route = call_agent(
        agent_name="router",
        model=FAST_MODEL,
        system_prompt=ROUTER_PROMPT,
        user_message=user_message,
        purpose="route message",
    ).strip().lower()

    if route not in {"writing", "memory", "research", "tasks", "crypto", "manager"}:
        return "manager"
    return route


def run_specialist(route: str, user_message: str) -> str:
    spec = SPECIALISTS[route]
    system_prompt = f"""
{spec['persona']}

Role:
{spec['role']}

Allowed tools:
{', '.join(spec['tool_names'])}

If a tool result is provided in the user message, use it. If the request needs a tool that is not available, say so plainly.
"""
    return call_agent(
        agent_name=spec["name"],
        model=spec["model"],
        system_prompt=system_prompt,
        user_message=user_message,
        purpose=f"run specialist {route}",
    )
```

Then handle obvious tool calls before the specialist response.

Example for crypto:

```python
from tools import get_crypto_price


def handle_crypto(user_message: str) -> str:
    text = user_message.lower()
    known = {
        "btc": "bitcoin",
        "bitcoin": "bitcoin",
        "eth": "ethereum",
        "ethereum": "ethereum",
        "sol": "solana",
        "solana": "solana",
        "doge": "dogecoin",
        "dogecoin": "dogecoin",
    }

    coin_id = None
    for key, value in known.items():
        if key in text:
            coin_id = value
            break

    if coin_id is None:
        return "Which coin? Use a CoinGecko id like bitcoin, ethereum, or solana."

    tool_result = get_crypto_price(coin_id)
    return run_specialist("crypto", f"User asked: {user_message}\n\nTool result: {tool_result}")
```

This is crude. It works. Improve it after customers exist.

---

# 8. Passing Output From One Agent to the Next

This is the mechanism many demos skip.

If the user asks:

```text
Research this week's AI-agent news and turn it into a landing-page section.
```

The manager should:

1. Ask Herald for research.
2. Pass Herald's output to Quill.
3. Return Quill's final copy.

Do not run both agents independently against the original prompt. That creates duplication and contradictions.

Use a handoff envelope.

```python

def handoff(from_agent: str, to_agent: str, task: str, previous_output: str) -> str:
    return f"""
You are receiving a handoff.

From agent: {from_agent}
To agent: {to_agent}
Task: {task}

Previous output:
{previous_output}

Use the previous output. Do not redo upstream work unless it is clearly wrong.
"""
```

Example manager workflow:

```python
research = run_specialist("research", "Find current AI-agent news this week. Keep it tight.")
copy_prompt = handoff(
    from_agent="Herald",
    to_agent="Quill",
    task="Turn the research into a landing-page section for builders.",
    previous_output=research,
)
final = run_specialist("writing", copy_prompt)
```

## Handoff Rules

- Preserve the previous output.
- Tell the next agent what to do with it.
- Tell the next agent not to redo upstream work.
- Have the manager summarize the final result.
- Store the handoff if you need auditability.

---

# 9. Telegram Bot Entry Point

`main.py`:

```python
import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

from state import init_db
from routing import route_message, run_specialist
from approvals import resolve_approval
from crypto_handler import handle_crypto
from tools import save_memory, list_tasks, create_task

load_dotenv()

TOKEN = os.getenv("TELEGRAM_MANAGER_BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Miles online. Mention me with a task, or ask for writing, memory, research, tasks, or crypto help."
    )


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message
    if not message or not message.text:
        return

    text = message.text.strip()

    # Approval commands.
    upper = text.upper()
    if upper.startswith("APPROVE "):
        approval_id = text.split(maxsplit=1)[1].strip()
        await message.reply_text(resolve_approval(approval_id, approved=True))
        return
    if upper.startswith("REJECT "):
        approval_id = text.split(maxsplit=1)[1].strip()
        await message.reply_text(resolve_approval(approval_id, approved=False))
        return

    # Simple routing.
    try:
        route = route_message(text)

        if route == "crypto":
            reply = handle_crypto(text)
        elif route == "memory" and "remember" in text.lower():
            content = text.lower().split("remember", 1)[1].strip()
            reply = save_memory(content)
        elif route == "tasks" and "task" in text.lower() and "list" in text.lower():
            reply = list_tasks()
        elif route == "tasks":
            reply = create_task(text)
        elif route in {"writing", "research", "memory"}:
            reply = run_specialist(route, text)
        else:
            reply = run_specialist("writing", text)  # Replace with a real manager call when ready.

    except RuntimeError as exc:
        reply = str(exc)
    except Exception:
        reply = "Something broke while handling that. Check logs. Yes, logs still matter."

    await message.reply_text(reply[:4000])


def main():
    if not TOKEN:
        raise RuntimeError("TELEGRAM_MANAGER_BOT_TOKEN is missing")

    init_db()
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()


if __name__ == "__main__":
    main()
```

This is intentionally plain.

For the product starter kit, plain beats elaborate. Elaborate comes later, usually with a migration guide and regret.

---

# 10. Deploy on Railway

## Step 1: Push to GitHub

```bash
git init
git add .
git commit -m "Initial AI agent company starter"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/agent-company.git
git push -u origin main
```

## Step 2: Create Railway Project

1. Go to Railway.
2. Create a new project.
3. Deploy from GitHub repo.
4. Select your repo.
5. Add environment variables:

```env
OPENAI_API_KEY=...
TELEGRAM_MANAGER_BOT_TOKEN=...
DATABASE_PATH=/data/agent_company.sqlite3
DAILY_BUDGET_USD=2.00
FAST_MODEL=gpt-4o-mini
SMART_MODEL=gpt-4o
```

## Step 3: Add a Persistent Volume

This matters.

Without a persistent volume, your SQLite database can disappear on redeploy.

In Railway:

1. Open your service.
2. Add a volume.
3. Mount it at:

```text
/data
```

4. Set:

```env
DATABASE_PATH=/data/agent_company.sqlite3
```

## Step 4: Set Start Command

Railway usually detects Python. If needed, set:

```bash
python main.py
```

## Step 5: Watch Logs

Test in Telegram:

```text
@YourMilesBot give me a one-line hook for my cold-email pack
@YourMilesBot remember I prefer morning standups
@YourMilesBot what's on my task list?
@YourMilesBot price of bitcoin
```

If it fails, check Railway logs first. Not your feelings. Logs.

---

# 11. Ready-to-Use Agent Prompt Templates

Use these as system prompts.

## Miles — Manager / Router Agent

```text
You are Miles, the manager/router for a small AI-agent company running in Telegram.

You coordinate specialist agents. You are not trying to do every job yourself.

Your responsibilities:
- Understand the user's request.
- Decide whether to answer directly or delegate.
- Use the fewest agents needed.
- For multi-step work, run agents in order and pass each output into the next task.
- Avoid duplicate work.
- Keep specialists within their roles.
- Ask clarifying questions when the request is too vague.
- Require human approval before risky actions: sending messages, spending money, deleting data, posting publicly, or changing external systems.
- Summarize final results clearly.

Specialists:
- Quill: writing, hooks, email copy, landing-page copy, editing.
- Sage: memory, durable preferences, project facts.
- Herald: web research and current information.
- Roster: tasks, checklists, project plans.
- Ledger: crypto prices and market quotes.

Tone:
Calm, direct, competent. Light dry humor is allowed. Do not ramble.

Output format:
- State what you did.
- Include the final result.
- Mention any agent handoffs if useful.
- Sign off with "- Miles".
```

## Quill — Writing Agent

```text
You are Quill, the writing specialist.

You write:
- Hooks
- Cold emails
- Landing-page copy
- Product descriptions
- Outlines
- Short-form content
- Edits and rewrites

Rules:
- Be specific.
- Avoid hype.
- Avoid fake urgency.
- Prefer clear buyer pain over clever wordplay.
- Give usable copy, not commentary about copy.
- If given research from another agent, use it instead of re-researching.

Tone:
Sharp, practical, concise. No marketing sludge.

Sign off with "- Quill".
```

## Sage — Memory Agent

```text
You are Sage, the memory specialist.

You manage durable memory for the user.

Save only:
- Stable preferences.
- Project facts.
- Reusable context.
- Important constraints.

Do not save:
- Secrets.
- API keys.
- Passwords.
- Temporary moods.
- Random one-off details.

When recalling memory:
- Return only relevant memories.
- Say when nothing relevant is found.
- Do not invent memories.

Tone:
Careful, concise, calm.

Sign off with "- Sage".
```

## Herald — Research Agent

```text
You are Herald, the research specialist.

You research current information and summarize it for decisions.

Rules:
- Prefer recent and reputable sources.
- Separate facts from interpretation.
- Note uncertainty.
- Keep summaries tight.
- Include links when available.
- Do not overstate weak evidence.

Tone:
Skeptical, source-minded, direct.

Sign off with "- Herald".
```

## Roster — Task Agent

```text
You are Roster, the task and project specialist.

You help with:
- Task lists
- Checklists
- Project plans
- Next actions
- Prioritization
- Status summaries

Rules:
- Convert vague work into concrete tasks.
- Use action verbs.
- Keep tasks small enough to execute.
- Ask for missing deadlines only when needed.
- Do not turn every answer into a giant project plan.

Tone:
Organized, direct, low-drama.

Sign off with "- Roster".
```

## Ledger — Crypto Agent

```text
You are Ledger, the crypto-price specialist.

You handle:
- Current crypto price lookups.
- Clean USD price quotes.
- Simple market wording.

Rules:
- Use the provided tool result when available.
- Quote the asset and USD price cleanly.
- If a coin id or ticker is ambiguous, ask for clarification.
- Do not give financial advice.
- Do not predict prices.
- Do not pretend price data is real-time beyond the source's current response.

Tone:
Dry, precise markets desk. Brief.

Sign off with "- Ledger".
```

---

# 12. Real Gotchas

## Gotcha 1: Telegram Privacy Mode

Symptom:

- Bot works in DMs.
- Bot ignores group messages.

Cause:

- Privacy mode is on.

Fix:

- Disable privacy mode in BotFather.
- Or require users to mention the bot every time.

For a group-agent product, mentioning the manager is often cleaner anyway. It reduces accidental token burn.

## Gotcha 2: Multiple Bots Duplicating Work

If every bot listens to every message, several bots may respond at once.

Fix options:

1. Only the manager bot listens broadly.
2. Specialists respond only when mentioned directly.
3. Manager internally calls specialist prompts instead of relying on specialist Telegram bots.
4. Add a message prefix rule:

```text
@MilesBot = manager route
@QuillBot = writing only
@SageBot = memory only
```

Start with option 1. It is boring and reliable.

## Gotcha 3: State Disappears on Deploy

Symptom:

- Memories vanish.
- Task list resets.
- Budget meter resets.

Cause:

- SQLite file was stored on ephemeral disk.

Fix:

- Use Railway persistent volume mounted at `/data`.
- Set `DATABASE_PATH=/data/agent_company.sqlite3`.

## Gotcha 4: Agents Repeat Each Other

Symptom:

- Herald researches something.
- Quill ignores Herald and starts over.

Fix:

- Use explicit handoff envelopes.
- Tell the downstream agent not to redo upstream work.
- Have the manager pass previous output into the next prompt.

## Gotcha 5: Tool Access Is Too Broad

Symptom:

- Writing agent saves weird memories.
- Research agent creates tasks you did not ask for.
- Crypto agent starts giving portfolio advice.

Fix:

- Curate tool lists by role.
- Enforce allowed tools in Python.
- Include role boundaries in prompts.

## Gotcha 6: Budget Runs Away

Symptom:

- Group chat gets busy.
- Bot responds to everything.
- API bill gets spicy.

Fix:

- Require mentions.
- Add daily budget limit.
- Use cheaper model for routing and most specialists.
- Use smarter model only for research or complex synthesis.
- Summarize long conversations instead of passing entire history.

## Gotcha 7: Human Approval Is Missing

Symptom:

- Agent sends something it should have drafted only.

Fix:

- Classify side-effect tools as risky.
- Create approval records.
- Require `APPROVE id` before execution.

The draft is the agent's job. The decision is yours.

---

# 13. Upgrade Paths

After the starter works, improve one thing at a time.

## Add Embeddings for Memory

Replace keyword search with vector search.

Options:

- SQLite + sqlite-vss.
- Postgres + pgvector.
- Chroma for local projects.

Do this only after keyword recall becomes painful.

## Add True OpenAI Tool Calling

Let the model request tool calls directly.

Keep the same rule:

```text
Model asks for tool -> Python checks permission -> Python executes -> result goes back to model
```

Never let the model bypass permission checks.

## Add Separate Specialist Telegram Bots

Useful for branding and demos:

- `@YourQuillBot`
- `@YourSageBot`
- `@YourHeraldBot`
- `@YourRosterBot`
- `@YourLedgerBot`

But do not add them until manager-only routing works.

Separate bots add coordination complexity. They look cool. They also create five places to debug. Choose wisely.

## Add Admin Commands

Examples:

```text
/budget
/memories
/tasks
/agents
/help
```

## Add Conversation Summaries

Instead of passing full chat history, summarize periodically:

```text
Conversation summary:
- User is building a $29 AI-agent starter kit.
- Prefers concise, practical copy.
- Current focus is Telegram group agents.
```

---

# 14. Buyer Implementation Checklist

Use this checklist while building.

## Setup

- [ ] Create OpenAI API key.
- [ ] Create Telegram manager bot with BotFather.
- [ ] Disable privacy mode or require mentions.
- [ ] Create Telegram group.
- [ ] Add manager bot to group.
- [ ] Create Python project.
- [ ] Install dependencies.
- [ ] Add `.env`.

## Core Code

- [ ] Add SQLite state.
- [ ] Add memory table.
- [ ] Add task table.
- [ ] Add budget events table.
- [ ] Add approvals table.
- [ ] Add tools.
- [ ] Add tool registry.
- [ ] Add specialist prompts.
- [ ] Add router.
- [ ] Add Telegram handlers.

## Safety

- [ ] Enforce allowed tools per agent.
- [ ] Add daily budget check.
- [ ] Track usage after each OpenAI call.
- [ ] Require approval for risky actions.
- [ ] Avoid storing secrets in memory.

## Deployment

- [ ] Push repo to GitHub.
- [ ] Create Railway project.
- [ ] Add environment variables.
- [ ] Add persistent volume.
- [ ] Mount volume at `/data`.
- [ ] Set `DATABASE_PATH=/data/agent_company.sqlite3`.
- [ ] Test in Telegram.
- [ ] Check logs.

---

# 15. Example Demo Script

Use this to record a product demo.

```text
You:
@MilesBot give me a one-line hook for my cold-email pack

Miles:
Routed to Quill.
Hook: Cold emails that turn strangers into warm leads — without sounding like everyone else.
- Miles
```

```text
You:
@MilesBot remember I prefer morning standups

Miles:
Routed to Sage.
Saved that memory.
- Miles
```

```text
You:
@MilesBot what's on my task list?

Miles:
Routed to Roster.
Task list:
- #3 [open] Draft landing-page copy
- #2 [open] Record demo video
- #1 [open] Package starter kit
- Miles
```

```text
You:
@MilesBot price of bitcoin

Miles:
Routed to Ledger.
Bitcoin is trading at $63,421.12 USD.
- Miles
```

```text
You:
@MilesBot research AI-agent course competitors and turn it into landing-page bullets

Miles:
1. Herald researched competitors.
2. Quill turned the research into landing-page bullets.

Final bullets:
- Build a working Telegram AI-agent team, not another abstract agent diagram.
- Learn manager routing, specialist prompts, least-privilege tools, budget limits, and approval gates.
- Deploy it on Railway with persistent memory so your agents survive redeploys.

- Miles
```

---

# 16. Landing Page Copy

## Hero

### Build Your Own AI Agent Company

Create a coordinated Telegram team of specialist AI agents with Python and the OpenAI API.

Build one manager, multiple specialists, real tools, budget limits, human approval gates, persistent memory, and Railway deployment — without drowning in framework complexity.

**Launch price: $29**

CTA: **Get the Starter Kit**

## Subhero

Most AI-agent tutorials show a cute demo and skip the parts that make agents usable: routing, tool permissions, budget control, handoffs, approvals, deployment, and state.

This kit teaches the whole working pattern by building a Telegram group of specialist agents you can actually use.

## What You Get

- A practical architecture for a multi-agent AI team.
- A manager/router pattern that delegates work to specialists.
- Least-privilege tool access so agents only use the tools they need.
- A daily budget meter to prevent runaway API spend.
- Human-in-the-loop approval gates for risky actions.
- Handoff patterns that pass one agent's output into the next.
- Telegram BotFather setup instructions.
- `python-telegram-bot` implementation guidance.
- OpenAI API call patterns.
- Railway deployment steps with persistent volume setup.
- Ready-to-use prompts for manager and specialist agents.
- Real gotchas: privacy mode, state persistence, duplicate agent replies, and coordination failures.

## Who It Is For

This is for builders who want to:

- Learn how multi-agent systems actually work.
- Build a useful Telegram-based AI team.
- Create specialist agents for writing, memory, research, tasks, prices, or internal workflows.
- Understand agent architecture before adopting heavier frameworks.
- Ship a practical prototype fast.

## Who It Is Not For

This is not for you if you want:

- A no-code chatbot builder.
- A giant enterprise agent platform.
- A theory-only AI course.
- A promise that agents will run your company while you nap on a beach.

They will not. They will occasionally hallucinate a beach.

## The Build

You will create:

- **Miles**, the manager/router agent.
- **Quill**, the writing agent.
- **Sage**, the memory agent.
- **Herald**, the research agent.
- **Roster**, the task agent.
- **Ledger**, the crypto-price agent.

Then you will connect them through Telegram, Python, OpenAI, curated tools, SQLite state, and Railway deployment.

## Why This Is Different

Most agent courses start with frameworks.

This starts with the mechanics:

- What an agent really is.
- How routing works.
- How tools are permissioned.
- How agents pass work to each other.
- How budget gets tracked.
- How humans approve risky actions.
- How state survives deployment.

Once you understand that, frameworks make more sense. Or you may not need one yet. Beautiful outcome either way.

## Pricing

Launch price: **$29**

Includes:

- Full guide.
- Starter architecture.
- Code patterns.
- Agent prompt templates.
- Deployment checklist.
- Landing-page/demo script examples.

## FAQ

### Do I need to know Python?

Yes. Basic Python is enough. If you can install packages, edit files, and read errors without immediately blaming the universe, you are fine.

### Do I need multiple Telegram bots?

No. Start with one manager bot. The manager can internally delegate to specialist prompts. Add separate specialist bots later if you want the full group-chat experience.

### Does this require an OpenAI API key?

Yes. You need your own OpenAI API key.

### Does this use LangChain or CrewAI?

No. The starter version uses plain Python. That keeps the mechanics visible. You can migrate to a framework later if you actually need one.

### Can I deploy it?

Yes. The guide includes Railway deployment with a persistent volume for SQLite state.

### Will this productionize my entire business?

No. It gives you a practical, working foundation. Production-grade systems need monitoring, auth, richer permissions, testing, evals, and better state management.

## Final CTA

Build the agent team first. Argue about frameworks later.

**Get Build Your Own AI Agent Company for $29.**

---

# 17. Gumroad / Checkout Copy

## Product Name

Build Your Own AI Agent Company

## Short Description

A practical guide + starter kit for building a coordinated Telegram team of specialist AI agents with Python and the OpenAI API.

## Checkout Description

Build a working AI-agent team in Telegram: a manager/router, specialist agents, curated tools, budget metering, human approval gates, persistent state, and Railway deployment.

Includes ready-to-use prompts, architecture notes, code patterns, deployment steps, implementation checklists, and the real gotchas most tutorials skip.

Launch price: $29.

## Bullets

- Build a Telegram-based multi-agent AI team.
- Create a manager/router and specialist agents.
- Add least-privilege tool access.
- Track daily OpenAI API spend.
- Add human approval gates for risky actions.
- Pass outputs between agents for multi-step work.
- Deploy on Railway with persistent SQLite state.
- Use ready-made prompts for writing, memory, research, tasks, and crypto agents.

---

# 18. License / Usage Note

You may use this guide to build your own internal agent team, client prototype, or learning project.

Do not resell this document as-is. Build something useful with it. Radical concept.

---

# 19. Final Build Advice

Start with one manager bot.

Add one specialist.

Add one tool.

Add budget metering.

Add state persistence.

Then add more agents.

If you start with seven bots, three frameworks, async queues, vector databases, and a dashboard, you are not building an agent company. You are building a failure museum.

Ship the boring version first.
