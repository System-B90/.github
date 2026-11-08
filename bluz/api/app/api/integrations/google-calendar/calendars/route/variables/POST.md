[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [app/api/integrations/google-calendar/calendars/route](../index.md) / POST

# Variable: POST

> `const` **POST**: (`request`, `context?`) => `Promise`\<`Response`\>

Defined in: [ui/src/app/api/integrations/google-calendar/calendars/route.ts:54](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/app/api/integrations/google-calendar/calendars/route.ts#L54)

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
