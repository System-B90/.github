[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/reload-diff](../index.md) / GANTT\_OWNED\_FIELDS

# Variable: GANTT\_OWNED\_FIELDS

> `const` **GANTT\_OWNED\_FIELDS**: `ReadonlyArray`\<keyof [`DbEventDocument`](../../../types/event/type-aliases/DbEventDocument.md)\>

Defined in: [ui/src/api-shared/gantt/reload-diff.ts:19](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-shared/gantt/reload-diff.ts#L19)

Fields the gantt owns. Everything else on a cut event (rooms, tags, colors,
locked/hidden flags, …) is schedule-side data the cut never wrote, so a
reload must not touch it — comparing it would report phantom drift.
