[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/common](../index.md) / requireJsonObjectBody

# Function: requireJsonObjectBody()

> **requireJsonObjectBody**\<`T`\>(`request`): `Promise`\<`T`\>

Defined in: [ui/src/api-server/common.ts:81](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/common.ts#L81)

Read a request body that must be a JSON object, and reject anything else at
the boundary.

Handlers used to cast `await request.json()` straight to a domain type with
`as`. That is a lie the type system cannot catch: a literal `null` body
survives a `typeof body === "object"` guard and crashes the first
destructuring, an array passes a truthiness check, and wrong-typed fields
travel all the way into Mongo/Postgres and come back as an opaque 500
instead of the 400 the caller earned (#522).

The returned value is still cast — this validates the *shape*, not the
fields — so callers that care about individual fields must still check them.

## Type Parameters

### T

`T`

## Parameters

### request

`Request`

## Returns

`Promise`\<`T`\>
