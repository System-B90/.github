[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [app/api/\[...unknown\]/route](../index.md) / POST

# Variable: POST

> `const` **POST**: (`request`) => `Promise`\<`Response`\> = `notFound`

Defined in: [ui/src/app/api/\[...unknown\]/route.ts:40](https://github.com/System-B90/Bluz/blob/901cc8f4c754d82c12fc600337c5991c07a64502/ui/src/app/api/[...unknown]/route.ts#L40)

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
