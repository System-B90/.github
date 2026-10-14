[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [app/api/integrations/google-calendar/sync/route](../index.md) / POST

# Variable: POST

> `const` **POST**: (`request`, `context?`) => `Promise`\<`Response`\>

Defined in: [ui/src/app/api/integrations/google-calendar/sync/route.ts:29](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/app/api/integrations/google-calendar/sync/route.ts#L29)

POST /api/integrations/google-calendar/sync — manual "sync now": pushes the
signed-in user's own upcoming events from the iteration their calendar is
bound to, and pulls their Google busy blocks.

## Parameters

### request

`Request`

### context?

`any`

## Returns

`Promise`\<`Response`\>
