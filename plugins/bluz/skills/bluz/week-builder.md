# Build a Week's Schedule

Input: a week number. Events are **already cut** into calendar events.
Job: re-order, re-time and room them so the week makes sense.
Never add or drop teaching content. Never change an event's total minutes without explicit permission.

The rules live in **[RULES.md](RULES.md)**. Read it fully before planning.
Cite rule IDs (`R-xx`) in every proposal and violation report.

Related:

- [cli-reference.md](cli-reference.md) — exact CLI syntax, payloads, meal-break guardrails.

## Quick Start

```bash
bluz gantt curriculums list
bluz --json gantt curriculums mappings <curriculum-id>
bluz --json events list --start <sunday>T00:00:00Z --end <next-sunday>T00:00:00Z
bluz --json gantt syllabuses shuffles <syllabus-id>
bluz --json rooms list
bluz --json courses list                          # instructorIds per course
bluz --json iterations settings <iteration-id>     # day bounds, meals, prayers
bluz --json gantt curriculums constraints <curriculum-id>

# R-50/R-51 check (exit 1 on violations) — a draft, an unsaved array, or the live week
bluz --json calendar validate-alignment --draft <draft-id>
bluz --json calendar validate-alignment --events-file draft.json
bluz --json calendar validate-alignment --start <sunday>T00:00:00Z --end <next-sunday>T00:00:00Z

# Before applying: snapshot the week
bluz --json events list --start <sunday>T00:00:00Z --end <next-sunday>T00:00:00Z > week.json
bluz calendar snapshots create --label "before /bluz week <N>" --events-file week.json
```

## Workflow

Do the steps in order. Never skip step 8.

1. **Resolve the week.** Week N → Sunday..Saturday dates + `GanttWeek.weekendDuty`.
   Several curricula match → ask.
2. **Load the week.** Events (type, syllabus, shuffles, courses,
   `splitAcrossBreaks`, calendar-event `locked` (מתואם), duration, room, Gantt order).
   Day bounds, meal and prayer times (`iterations settings`, R-45). Rooms + `lectureSeatCount` / `workstationCount`. Shuffles per
   syllabus. Ask once: "לחלק ביזורים?" (R-67).
3. **Fixed frames per day** (§1–§3): Sunday arrival, Thursday מסדרים, Friday exit, Shabbat
   window, meals, prayers, day end.
4. **Alignment grid** (§5): per syllabus, the block edges all its shuffles share.
5. **Place events** in tier order (§0). Pin מתואם (`locked`) events first, at their current times and rooms. Keep
   Gantt order within each syllabus (R-47). Split only when needed (§5.3).
6. **Rooms** (§6). Unknown shuffle sizes → `AskUserQuestion`. Instructors
   (§6.1) if requested — course members first.
7. **Constraint pass** (§8) on the draft. All constraints soft. Run
   `bluz calendar validate-alignment --events-file draft.json` and fix every
   R-50/R-51 hit before proposing; any left go under **Problems**.
8. **Propose** (format below). Save the proposed week as a shared draft and
   open it in Chrome (see **Show the Draft**). Wait for approval.
9. **Apply.** Snapshot, then write via `bluz`. Re-list the week, re-check
   every rule (`bluz calendar validate-alignment --start … --end …` for §5),
   report residual violations honestly.

## Proposal Format

The draft in Chrome **is** the schedule. No per-day tables, no event listings,
no wall of text. Lead with the draft URL, then only these sections, one short
bullet per item. Omit an empty section.

- **Problems** — rule violations and constraints left violated: rule ID, what, why unavoidable.
- **Issues** — risks and judgment calls the user should check (tight rooms, odd placements).
- **Splits** — event, pieces, why.
- **Open questions** — anything a human must decide.

## Show the Draft

The proposal is also a shared calendar draft the user sees in Bluz.

1. Write the full proposed week as an events array (same shape as
   `bluz --json events list`) to `proposal.json`.
2. Create it (or `drafts update <id>` on later revisions):
    ```bash
    bluz --json calendar drafts create --label "/bluz week <N> proposal" --events-file proposal.json
    ```
3. Open Chrome on the week, with the draft loaded (`BLUZ_URL` from `bluz auth config`):
    ```powershell
    Start-Process chrome "<BLUZ_URL>/?date=<sunday YYYY-MM-DD>&draft=<draft-id>"
    ```
4. Give the user the URL at the top of the proposal.

The page shows the draft locally only; paging weeks returns to the real
events. Approval still means step 9 — the draft is never applied by itself.
Delete the draft after applying or rejecting: `bluz calendar drafts delete <id> --yes`.

## Hard Stops — Ask, Don't Guess

- Any tier-H rule cannot be met.
- A split would leave a piece under 20 min (R-57).
- Shuffle block edges cannot align even with splits.
- Week load exceeds its windows.
- Room choice depends on shuffle/course sizes you don't know.

## Growing the Rules

`RULES.md` ends with **Open Questions**. Hit one → ask the user, then write
the answer into `RULES.md` with a new ID. Keep it formal and short.
