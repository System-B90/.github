[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/break-windows](../index.md) / breakAppliesTo

# Function: breakAppliesTo()

> **breakAppliesTo**(`window`, `event`): `boolean`

Defined in: [ui/src/api-shared/break-windows.ts:75](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-shared/break-windows.ts#L75)

Whether a break interrupts a given event. A break with no rooms and no
courses is base-wide and interrupts everyone; a scoped break only reaches
events it shares a room or a course with.

## Parameters

### window

[`BreakWindow`](../type-aliases/BreakWindow.md)

### event

`Pick`\<[`SplittableEvent`](../type-aliases/SplittableEvent.md), `"courses"` \| `"rooms"`\>

## Returns

`boolean`
