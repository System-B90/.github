[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [app/api/access-tokens/\[id\]/route](../index.md) / DELETE

# Variable: DELETE

> `const` **DELETE**: (`request`, `context?`) => `Promise`\<`Response`\>

Defined in: [ui/src/app/api/access-tokens/\[id\]/route.ts:24](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/app/api/access-tokens/[id]/route.ts#L24)

DELETE /api/access-tokens/:id — revoke immediately. A ReadWrite token may
revoke itself or a sibling; a ReadOnly one is stopped by its scope.

## Parameters

### request

`NextRequest`

### context?

`RouteContext`

## Returns

`Promise`\<`Response`\>
