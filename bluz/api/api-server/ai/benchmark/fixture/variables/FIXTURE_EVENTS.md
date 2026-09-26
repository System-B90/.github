[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/ai/benchmark/fixture](../index.md) / FIXTURE\_EVENTS

# Variable: FIXTURE\_EVENTS

> `const` **FIXTURE\_EVENTS**: [`AiEventSummary`](../../../tools/calendar/type-aliases/AiEventSummary.md)[]

Defined in: [ui/src/api-server/ai/benchmark/fixture.ts:74](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/ai/benchmark/fixture.ts#L74)

Two events share a name on purpose: a model asked to change "the מתמטיקה
lesson" has to notice the ambiguity and ask rather than pick one.

Typed as the production projection so the fixture cannot answer with a shape
the real `list_events` would never produce — which is how the `type` field
here was caught carrying "lesson", a value `EventType` does not contain.
