[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [app/api/access-tokens/route](../index.md) / POST

# Variable: POST

> `const` **POST**: (`request`, `context?`) => `Promise`\<`Response`\>

Defined in: [ui/src/app/api/access-tokens/route.ts:41](https://github.com/System-B90/Bluz/blob/1b02178048002eee34d502b2e3e2a402e1b9c9c0/ui/src/app/api/access-tokens/route.ts#L41)

POST /api/access-tokens — mint a token. Needs a real sign-in (browser
session, or the session `bluz login` stores): a token must not be able to
mint its own longer-lived successors.

## Parameters

### request

`Request`

### context?

`any`

## Returns

`Promise`\<`Response`\>
