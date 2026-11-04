[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [app/api/calendar/validate/shuffle-alignment/route](../index.md) / POST

# Variable: POST

> `const` **POST**: (`request`, `context?`) => `Promise`\<`Response`\>

Defined in: [ui/src/app/api/calendar/validate/shuffle-alignment/route.ts:21](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/app/api/calendar/validate/shuffle-alignment/route.ts#L21)

POST /api/calendar/validate/shuffle-alignment (#1000) — R-50/R-51 over one
of: `{ start, end }` (live calendar), `{ draftId }` (saved draft) or
`{ events }` (unsaved draft). Returns the violations; empty means aligned.
Read-only, so past iterations may be checked too.

## Parameters

### request

`Request`

### context?

`any`

## Returns

`Promise`\<`Response`\>
