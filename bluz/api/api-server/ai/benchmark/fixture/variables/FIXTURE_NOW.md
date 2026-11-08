[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/ai/benchmark/fixture](../index.md) / FIXTURE\_NOW

# Variable: FIXTURE\_NOW

> `const` **FIXTURE\_NOW**: `Date`

Defined in: [ui/src/api-server/ai/benchmark/fixture.ts:43](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/api-server/ai/benchmark/fixture.ts#L43)

The fixed "now" every run shares: Sunday 2026-03-01, 08:00 Israel time.

Pinned rather than read from the clock so "Tuesday" and "next week" resolve
to the same dates on every run — the benchmark grades the model's date
reasoning, and a moving anchor would move the right answer with it.
