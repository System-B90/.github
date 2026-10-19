[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/shuffle-alignment](../index.md) / AlignmentRule

# Type Alias: AlignmentRule

> **AlignmentRule** = `"R-50"` \| `"R-51"`

Defined in: [ui/src/api-shared/shuffle-alignment.ts:18](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/api-shared/shuffle-alignment.ts#L18)

Shuffle alignment on the calendar (#1000), one pure check behind the
server route, the CLI and the schedule button.

- **R-50** All shuffles of one syllabus share block edges: every block
  holding the syllabus starts and ends at the same times for each of its
  shuffles. A block is a maximal run of a shuffle's touching events;
  breaks and prayers are not part of a run, so they cut it.
- **R-51** A syllabus' daily minutes are equal across its shuffles.

Course-only events (no shuffle) are ignored (R-52). Syllabuses are told
apart by Hive subject, so mutually exclusive courses never meet (R-53).
