[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/shuffle-alignment](../index.md) / AlignmentRule

# Type Alias: AlignmentRule

> **AlignmentRule** = `Extract`\<[`ScheduleRuleId`](../../schedule-rules/type-aliases/ScheduleRuleId.md), `"R-50"` \| `"R-51"`\>

Defined in: [ui/src/api-shared/shuffle-alignment.ts:26](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-shared/shuffle-alignment.ts#L26)

Shuffle alignment on the calendar (#1000), one pure check behind the
server route, the CLI and the schedule button.

- **R-50** All shuffles of one syllabus share block edges: every block
  holding the syllabus starts and ends at the same times for each of its
  shuffles. A block is a maximal run of a shuffle's touching events;
  breaks and prayers are not part of a run, so they cut it — except a
  break for exactly one shuffle (no rooms, its only course that shuffle),
  which bridges that shuffle's block instead (R-54). A bridge never sets
  a block edge on its own: blocks are trimmed to their content.
- **R-51** A syllabus' daily minutes are equal across its shuffles. Break
  minutes never count, bridging breaks included.

Course-only events (no shuffle) are ignored (R-52). Syllabuses are told
apart by Hive subject, and every shuffle holding a syllabus is compared,
even across mutually exclusive courses: syllabus membership takes
precedence over the course tree (R-53).
Rule titles and meanings: `schedule-rules.ts`.
