[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [app/api/integrations/google-calendar/calendars/route](../index.md) / POST

# Variable: POST

> `const` **POST**: (`request`, `context?`) => `Promise`\<`Response`\>

Defined in: [ui/src/app/api/integrations/google-calendar/calendars/route.ts:51](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/app/api/integrations/google-calendar/calendars/route.ts#L51)

POST /api/integrations/google-calendar/calendars — re-point the user's
link at another calendar (`{ calendarId }`) or a fresh Bluz-created one
(`{ createNew: true }`).

## Parameters

### request

`NextRequest`

### context?

`any`

## Returns

`Promise`\<`Response`\>
