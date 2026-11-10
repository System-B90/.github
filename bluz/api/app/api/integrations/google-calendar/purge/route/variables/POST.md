[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [app/api/integrations/google-calendar/purge/route](../index.md) / POST

# Variable: POST

> `const` **POST**: (`request`, `context?`) => `Promise`\<`Response`\>

Defined in: [ui/src/app/api/integrations/google-calendar/purge/route.ts:33](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/app/api/integrations/google-calendar/purge/route.ts#L33)

POST /api/integrations/google-calendar/purge — removes Bluz-tagged events
from the signed-in user's linked Google calendar: `orphaned` (no live,
in-scope Bluz event of the calendar's iteration behind them) or `all`.
Events created by hand in Google are never touched.

## Parameters

### request

`NextRequest`

### context?

`any`

## Returns

`Promise`\<`Response`\>
