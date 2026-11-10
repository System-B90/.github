[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/break-windows](../index.md) / collectBreakWindows

# Function: collectBreakWindows()

> **collectBreakWindows**(`events`, `expandCourses?`): [`BreakWindow`](../type-aliases/BreakWindow.md)[]

Defined in: [ui/src/api-shared/break-windows.ts:65](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-shared/break-windows.ts#L65)

Extracts every break event in `events` as a scoped window. Pass the complete
event set, not a filtered/visible subset — a break hidden by a filter still
interrupts the day.

## Parameters

### events

`Iterable`\<[`SplittableEvent`](../type-aliases/SplittableEvent.md)\>

### expandCourses?

(`courseIds`) => `Iterable`\<`string`\>

Widens a break's courses to their descendants, so a
       Bis90 break also interrupts Apollo events (#974).

## Returns

[`BreakWindow`](../type-aliases/BreakWindow.md)[]
