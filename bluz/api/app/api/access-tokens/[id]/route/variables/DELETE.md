[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [app/api/access-tokens/\[id\]/route](../index.md) / DELETE

# Variable: DELETE

> `const` **DELETE**: (`request`, `context?`) => `Promise`\<`Response`\>

Defined in: [ui/src/app/api/access-tokens/\[id\]/route.ts:24](https://github.com/System-B90/Bluz/blob/182d51c797407c7b0ea37986b1a45ab0e64c4df0/ui/src/app/api/access-tokens/[id]/route.ts#L24)

DELETE /api/access-tokens/:id — revoke immediately. A ReadWrite token may
revoke itself or a sibling; a ReadOnly one is stopped by its scope.

## Parameters

### request

`NextRequest`

### context?

`RouteContext`

## Returns

`Promise`\<`Response`\>
