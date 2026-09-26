[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [app/api/ai/benchmark/route](../index.md) / GET

# Variable: GET

> `const` **GET**: (`request`, `context?`) => `Promise`\<`Response`\>

Defined in: [ui/src/app/api/ai/benchmark/route.ts:27](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/app/api/ai/benchmark/route.ts#L27)

Assistant self-test against a fabricated fixture (#704).

Gated by the same staff session as `/api/ai/chat` and no more: any user can
point the deployment at a different model or key, so any user needs to be
able to check *theirs*. It is throttled hard instead, because a run costs
real tokens.

A run takes minutes — past a proxy's request timeout — so POST only starts
it in the background and answers at once; GET reports its state.

## Parameters

### request

`Request`

### context?

`any`

## Returns

`Promise`\<`Response`\>
