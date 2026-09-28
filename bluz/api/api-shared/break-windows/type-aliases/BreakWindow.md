[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/break-windows](../index.md) / BreakWindow

# Type Alias: BreakWindow

> **BreakWindow** = [`Interval`](../../interval-layout/type-aliases/Interval.md) & `object`

Defined in: [ui/src/api-shared/break-windows.ts:30](https://github.com/System-B90/Bluz/blob/23625511d59d71bc9679adc341fb0bcb28897208/ui/src/api-shared/break-windows.ts#L30)

A break window plus the audience it applies to.

## Type Declaration

### courseIds

> **courseIds**: `ReadonlyArray`\<[`CourseId`](../../types/course/type-aliases/CourseId.md)\>

The break's courses; empty means "not course-scoped".

### roomKeys

> **roomKeys**: `ReadonlyArray`\<`string`\>

Resource keys of the break's rooms; empty means "not room-scoped".
