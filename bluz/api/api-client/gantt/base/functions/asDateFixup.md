[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-client/gantt/base](../index.md) / asDateFixup

# Function: asDateFixup()

> **asDateFixup**\<`T`\>(): [`DateFixup`](../type-aliases/DateFixup.md)\<`T`\>

Defined in: [ui/src/api-client/gantt/base.ts:44](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-client/gantt/base.ts#L44)

Adapts `baseDocumentFixup` — precisely typed as
`(doc: T) => T & BaseDocument` — to the looser `DateFixup<T>` shape
`clientGantApiBuilder` needs (`rawItem: unknown`, since it calls
`dateFixup` with several not-quite-`T` argument types across
apiGet/apiCreate/apiUpdate/apiGetMany/apiLink: `ApiT<TEntity>`, `TEntity`,
and `unknown`). Every simple entity builder (day/module/module-event/
syllabus/week/curriculum) needs exactly this adaptation, so it used to be
duplicated as `baseDocumentFixup as any` at each of those five call sites
— one unchecked cast per file, each hiding a real type mismatch behind
`any` rather than the specific, intentional widening this is. Centralizing
it here means there is exactly one cast to audit instead of five.

## Type Parameters

### T

`T` *extends* [`RawBaseDocument`](../../../../api-shared/types/gantt/api-layer/type-aliases/RawBaseDocument.md)

## Returns

[`DateFixup`](../type-aliases/DateFixup.md)\<`T`\>
