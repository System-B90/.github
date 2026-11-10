[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [app/api/calendar/validate/shuffle-alignment/route](../index.md) / POST

# Variable: POST

> `const` **POST**: (`request`, `context?`) => `Promise`\<`Response`\>

Defined in: [ui/src/app/api/calendar/validate/shuffle-alignment/route.ts:21](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/app/api/calendar/validate/shuffle-alignment/route.ts#L21)

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
