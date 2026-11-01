[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/student-view/merge-touching](../index.md) / mergeTouching

# Function: mergeTouching()

> **mergeTouching**\<`T`\>(`tiles`): `T`[]

Defined in: [ui/src/components/student-view/merge-touching.ts:19](https://github.com/System-B90/Bluz/blob/2fa23325da73d58527b069b0943f3bd1e838efee/ui/src/components/student-view/merge-touching.ts#L19)

Joins tiles that continue one another into one long tile (#1028): same
name, color, room and courses, one ending exactly where the next starts.
A gap of even a minute keeps them apart. Returned in start order.

## Type Parameters

### T

`T` *extends* `Mergeable`

## Parameters

### tiles

`T`[]

## Returns

`T`[]
