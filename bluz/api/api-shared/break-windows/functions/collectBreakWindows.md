[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/break-windows](../index.md) / collectBreakWindows

# Function: collectBreakWindows()

> **collectBreakWindows**(`events`, `expandCourses?`): [`BreakWindow`](../type-aliases/BreakWindow.md)[]

Defined in: [ui/src/api-shared/break-windows.ts:62](https://github.com/System-B90/Bluz/blob/9293ec523a02fdbe59b9479de6b3caee2f4be11c/ui/src/api-shared/break-windows.ts#L62)

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
