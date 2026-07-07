# VAN-25 — Daily Command Center Command

## Command

`/today`

## Purpose

Answer one question: **what should Tyler work on today?**

The command must choose a starting point, not produce a backlog review.

## Project priority order

Always evaluate projects in this order:

1. Card Tracker
2. Worthlane
3. Tyler AI Assistant
4. Career Ops
5. Virtual Office — parked; only mention if every higher-priority project has no actionable work

## Linear inputs to use

When Linear data is available, check:

- project name
- issue status
- due date / target date / created or updated date when relevant
- labels, especially `MVP`
- assignee
- priority

The command should reference dates and `MVP` labels in the output when they influenced the recommendation.

## Selection rules

1. Find the **current main project** by scanning the priority list from top to bottom.
2. A project becomes today’s main project if it has at least one actionable Linear issue that is:
   - due today or overdue,
   - labeled `MVP`,
   - already in progress,
   - blocked only on Tyler making a concrete next move, or
   - the highest-priority unfinished issue in that project.
3. Select **one task by default**.
4. Select a second task only if it is small, clearly related, and helps finish or unblock the first task.
5. Never return more than two tasks.
6. Do not include parked Virtual Office work unless Card Tracker, Worthlane, Tyler AI Assistant, and Career Ops have no actionable work.
7. Prefer starting work over organizing work. No broad planning unless the selected task is explicitly a planning task.

## Default output format

Keep the response short.

```text
Today’s main project: <project>

Do this first: <single concrete task>
Why: <one sentence citing Linear issue/date/MVP label if available>

If that gets done: <optional second concrete task>

Stop after this. Do not reorganize the backlog today.
```

## Copy/paste workflow prompt

Use this prompt when a slash command is not available:

```text
Act as my daily command center.

Using Linear, tell me what Tyler should work on today.

Rules:
- Respect this project priority order exactly: Card Tracker, Worthlane, Tyler AI Assistant, Career Ops, then parked Virtual Office.
- Surface the current main project.
- Pick 1 task by default and at most 2 tasks total.
- Prefer Linear issues that are due today, overdue, labeled MVP, or already in progress.
- Reference issue dates and MVP labels when they affected the choice.
- Do not generate a big plan, backlog review, roadmap, or options list.
- Tell me what to do first in plain language.
- If Virtual Office appears, only include it if all higher-priority projects have no actionable work.

Output exactly:
Today’s main project: <project>
Do this first: <task>
Why: <one sentence>
If that gets done: <optional second task or “stop”>
Stop after this. Do not reorganize the backlog today.
```

## Example output

```text
Today’s main project: Card Tracker

Do this first: Finish VAN-46 watchlist data model persistence and open the PR.
Why: Card Tracker is the top-priority project, and VAN-46 is MVP-scoped work already queued for implementation.

If that gets done: Run the model/persistence tests and note the PR path.

Stop after this. Do not reorganize the backlog today.
```

## Acceptance check

- Current main project is surfaced.
- Day is limited to 1–2 tasks.
- Project priority order is explicit and mandatory.
- Linear issue dates and `MVP` labels can be referenced.
- Default output is short, not a huge plan.
- The first action is named directly.
