[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [app/api/calendar/validate/\[ruleId\]/route](../index.md) / POST

# Variable: POST

> `const` **POST**: (`request`, `context?`) => `Promise`\<`Response`\>

Defined in: [ui/src/app/api/calendar/validate/\[ruleId\]/route.ts:24](https://github.com/System-B90/Bluz/blob/e82087d51f2769f8b338ee03029e86c8d2549994/ui/src/app/api/calendar/validate/[ruleId]/route.ts#L24)

POST /api/calendar/validate/[ruleId] — one schedule rule (`R-xx`, see
`rule-ids.ts`) over `{ start, end }` (live calendar), `{ draftId }` (saved
draft) or `{ events }` (unsaved draft). Returns that rule's violations,
each with the event ids to jump to; empty means it holds. Read-only, so
past iterations may be checked too. The client calls it rule by rule.

## Parameters

### request

`Request`

### context?

`RouteContext`

## Returns

`Promise`\<`Response`\>
