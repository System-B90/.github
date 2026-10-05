[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [app/api/cli-auth/redeem/route](../index.md) / POST

# Variable: POST

> `const` **POST**: (`request`, `context?`) => `Promise`\<`Response`\>

Defined in: [ui/src/app/api/cli-auth/redeem/route.ts:26](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/app/api/cli-auth/redeem/route.ts#L26)

Redeems a CLI login handoff code (#520) for the next-auth session token it
was minted for. Deliberately unauthenticated -- the caller (the CLI, not a
browser) has no session yet; the handoff code itself is the credential,
single-use and short-TTL (see db-cli-handoff.ts).

## Parameters

### request

`NextRequest`

### context?

`any`

## Returns

`Promise`\<`Response`\>
