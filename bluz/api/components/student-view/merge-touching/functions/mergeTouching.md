[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/student-view/merge-touching](../index.md) / mergeTouching

# Function: mergeTouching()

> **mergeTouching**\<`T`\>(`tiles`): `T`[]

Defined in: [ui/src/components/student-view/merge-touching.ts:19](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/components/student-view/merge-touching.ts#L19)

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
