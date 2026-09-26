[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [app/api/integrations/google-calendar/connect/route](../index.md) / POST

# Variable: POST

> `const` **POST**: (`request`, `context?`) => `Promise`\<`Response`\>

Defined in: [ui/src/app/api/integrations/google-calendar/connect/route.ts:25](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/app/api/integrations/google-calendar/connect/route.ts#L25)

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
