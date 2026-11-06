[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [app/api/integrations/google-calendar/calendars/route](../index.md) / GET

# Variable: GET

> `const` **GET**: (`request`, `context?`) => `Promise`\<`Response`\>

Defined in: [ui/src/app/api/integrations/google-calendar/calendars/route.ts:38](https://github.com/System-B90/Bluz/blob/90114c31e10132d84c8c3bab079c25588fbe0459/ui/src/app/api/integrations/google-calendar/calendars/route.ts#L38)

GET /api/integrations/google-calendar/calendars — the calendars the
signed-in user can mirror into: their own, plus any a colleague shared
with write access (which is how several users end up on one calendar).

## Parameters

### request

`Request`

### context?

`any`

## Returns

`Promise`\<`Response`\>
