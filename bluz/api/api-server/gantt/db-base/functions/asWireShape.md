[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/db-base](../index.md) / asWireShape

# Function: asWireShape()

> **asWireShape**\<`T`\>(`row`): `T`

Defined in: [ui/src/api-server/gantt/db-base.ts:154](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/gantt/db-base.ts#L154)

Hand a relational-query row out under its `Api*` type.

The one real difference between the two is the timestamp axis: a row carries
`Date` for `createdAt`/`updatedAt`, while the `Api*` types describe the
*wire* shape, where `JSON.stringify` has already turned those into ISO
strings. They cannot simply be unified - `Api*` lives in api-shared and is
consumed by the browser, which never sees a `Date` - so some assertion is
unavoidable here.

What this replaces is three anonymous `as any` / `as unknown as` casts that
waived *every* difference silently (#538 item 14). Routing them through one
named helper keeps the waiver greppable and documented. It is still a
waiver: a field renamed on one side of the boundary will not break the
build. Closing that needs the readers to build their result explicitly
rather than returning the row.

## Type Parameters

### T

`T`

## Parameters

### row

`unknown`

## Returns

`T`
