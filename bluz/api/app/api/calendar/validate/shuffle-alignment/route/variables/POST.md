[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [app/api/calendar/validate/shuffle-alignment/route](../index.md) / POST

# Variable: POST

> `const` **POST**: (`request`, `context?`) => `Promise`\<`Response`\>

Defined in: [ui/src/app/api/calendar/validate/shuffle-alignment/route.ts:21](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/app/api/calendar/validate/shuffle-alignment/route.ts#L21)

POST /api/calendar/validate/shuffle-alignment (#1000) — R-50/R-51 over one
of: `{ start, end }` (live calendar), `{ draftId }` (saved draft) or
`{ events }` (unsaved draft). Returns the violations; empty means aligned.
Read-only, so past iterations may be checked too. The schedule validator
runs every rule one by one at `/api/calendar/validate/[ruleId]`.

## Parameters

### request

`Request`

### context?

`any`

## Returns

`Promise`\<`Response`\>
