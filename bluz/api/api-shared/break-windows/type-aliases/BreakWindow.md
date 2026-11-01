[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/break-windows](../index.md) / BreakWindow

# Type Alias: BreakWindow

> **BreakWindow** = [`Interval`](../../interval-layout/type-aliases/Interval.md) & `object`

Defined in: [ui/src/api-shared/break-windows.ts:36](https://github.com/System-B90/Bluz/blob/2fa23325da73d58527b069b0943f3bd1e838efee/ui/src/api-shared/break-windows.ts#L36)

A break window plus the audience it applies to.

## Type Declaration

### courseIds

> **courseIds**: `ReadonlyArray`\<[`CourseId`](../../types/course/type-aliases/CourseId.md)\>

The break's courses; empty means "not course-scoped".

### roomKeys

> **roomKeys**: `ReadonlyArray`\<`string`\>

Resource keys of the break's rooms; empty means "not room-scoped".
