[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/ai/benchmark/fixture](../index.md) / FIXTURE\_EVENTS

# Variable: FIXTURE\_EVENTS

> `const` **FIXTURE\_EVENTS**: [`AiEventSummary`](../../../tools/calendar/type-aliases/AiEventSummary.md)[]

Defined in: [ui/src/api-server/ai/benchmark/fixture.ts:113](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/api-server/ai/benchmark/fixture.ts#L113)

Typed as the production projection so the fixture cannot answer with a shape
the real `list_events` would never produce.

- fx-1 / fx-2 share a name: a model asked to move "the מתמטיקה lesson" has
  to notice the ambiguity and ask.
- fx-h1 / fx-h2 are Tuesday's hidden events; fx-h3 is hidden too but sits
  under the visible workshop fx-3, so it must be skipped; fx-h4 is a hidden
  decoy on Wednesday.
- fx-f1 / fx-f2 are existing placeholders, for the undo case.
