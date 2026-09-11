[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [app/api/integrations/google-calendar/connect/route](../index.md) / POST

# Variable: POST

> `const` **POST**: (`request`, `context?`) => `Promise`\<`Response`\>

Defined in: [ui/src/app/api/integrations/google-calendar/connect/route.ts:25](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/app/api/integrations/google-calendar/connect/route.ts#L25)

POST /api/integrations/google-calendar/connect — receives the authorization
code produced by the browser-side Google Identity Services popup
("Continue with Google") and exchanges it for tokens. The GIS popup code
model redeems the code against the reserved `"postmessage"` redirect_uri,
so no redirect URI is ever registered or configured server-side.

## Parameters

### request

`NextRequest`

### context?

`any`

## Returns

`Promise`\<`Response`\>
