[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [app/api/\[...unknown\]/route](../index.md) / GET

# Variable: GET

> `const` **GET**: (`request`) => `Promise`\<`Response`\> = `notFound`

Defined in: [ui/src/app/api/\[...unknown\]/route.ts:39](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/app/api/[...unknown]/route.ts#L39)

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
