[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [app/api/integrations/google-calendar/calendars/route](../index.md) / GET

# Variable: GET

> `const` **GET**: (`request`, `context?`) => `Promise`\<`Response`\>

Defined in: [ui/src/app/api/integrations/google-calendar/calendars/route.ts:36](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/app/api/integrations/google-calendar/calendars/route.ts#L36)

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
