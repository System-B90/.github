[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/reload-diff](../index.md) / GANTT\_OWNED\_FIELDS

# Variable: GANTT\_OWNED\_FIELDS

> `const` **GANTT\_OWNED\_FIELDS**: `ReadonlyArray`\<keyof [`DbEventDocument`](../../../types/event/type-aliases/DbEventDocument.md)\>

Defined in: [ui/src/api-shared/gantt/reload-diff.ts:19](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/reload-diff.ts#L19)

Fields the gantt owns. Everything else on a cut event (rooms, tags, colors,
locked/hidden flags, …) is schedule-side data the cut never wrote, so a
reload must not touch it — comparing it would report phantom drift.
