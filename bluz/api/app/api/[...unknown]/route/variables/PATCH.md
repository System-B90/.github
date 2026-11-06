[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [app/api/\[...unknown\]/route](../index.md) / PATCH

# Variable: PATCH

> `const` **PATCH**: (`request`) => `Promise`\<`Response`\> = `notFound`

Defined in: [ui/src/app/api/\[...unknown\]/route.ts:42](https://github.com/System-B90/Bluz/blob/90114c31e10132d84c8c3bab079c25588fbe0459/ui/src/app/api/[...unknown]/route.ts#L42)

Every `/api/*` path no real route matches lands here — Next resolves a
catch-all last. Answers the same 404 to everyone; a student session is
additionally logged, since the board only ever calls real routes and a
stream of misses is directory busting.

Anonymous misses are not logged: internet scanners would bury the signal.

## Parameters

### request

`NextRequest`

## Returns

`Promise`\<`Response`\>
