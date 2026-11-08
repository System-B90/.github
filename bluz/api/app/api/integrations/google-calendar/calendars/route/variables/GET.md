[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [app/api/integrations/google-calendar/calendars/route](../index.md) / GET

# Variable: GET

> `const` **GET**: (`request`, `context?`) => `Promise`\<`Response`\>

Defined in: [ui/src/app/api/integrations/google-calendar/calendars/route.ts:38](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/app/api/integrations/google-calendar/calendars/route.ts#L38)

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
