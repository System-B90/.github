[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [app/api/integrations/google-calendar/sync/route](../index.md) / POST

# Variable: POST

> `const` **POST**: (`request`, `context?`) => `Promise`\<`Response`\>

Defined in: [ui/src/app/api/integrations/google-calendar/sync/route.ts:23](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/app/api/integrations/google-calendar/sync/route.ts#L23)

POST /api/integrations/google-calendar/sync — manual "sync now": pushes the
signed-in user's own upcoming events and pulls their Google busy blocks.

## Parameters

### request

`Request`

### context?

`any`

## Returns

`Promise`\<`Response`\>
