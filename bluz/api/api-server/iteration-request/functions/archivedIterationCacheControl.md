[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/iteration-request](../index.md) / archivedIterationCacheControl

# Function: archivedIterationCacheControl()

> **archivedIterationCacheControl**(`iteration`): [`ApiCacheControl`](../../common/type-aliases/ApiCacheControl.md) \| `undefined`

Defined in: [ui/src/api-server/iteration-request.ts:24](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/iteration-request.ts#L24)

Cache directive for a response built from an archived iteration's frozen
Hive snapshot: a week, and `private` because every route sits behind Hive
SSO and a shared cache must not hold a copy. The current iteration is live
data, so it gets no directive at all.

## Parameters

### iteration

[`Iteration`](../../../api-shared/types/iteration/type-aliases/Iteration.md) \| `null` \| `undefined`

## Returns

[`ApiCacheControl`](../../common/type-aliases/ApiCacheControl.md) \| `undefined`
