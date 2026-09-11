[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/cut-rules](../index.md) / BREAK\_KINDS

# Variable: BREAK\_KINDS

> `const` **BREAK\_KINDS**: readonly \[`"post-long-exercise"`, `"between-syllabuses"`, `"prayer-cover"`, `"post-lecture"`, `"room-change"`\]

Defined in: [ui/src/api-shared/gantt/cut-rules.ts:166](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/gantt/cut-rules.ts#L166)

Kinds of break the post-pass can insert, in **descending priority**. When a
day has less slack than the breaks it wants, higher-priority kinds are
satisfied first and the rest are dropped — breaks never extend a day past
its end time.

Ordering rationale (see `docs/gantt-cut-rules.md` for the long form):
fatigue from a long unbroken ע"ע block is the most concrete harm; a context
switch between syllabuses is the next; covering a prayer is a scheduling win
that costs nothing when it can be arranged; a plain post-lecture breather is
the nicety that yields first.
