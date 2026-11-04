[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/break-windows](../index.md) / breakAppliesTo

# Function: breakAppliesTo()

> **breakAppliesTo**(`window`, `event`): `boolean`

Defined in: [ui/src/api-shared/break-windows.ts:89](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/api-shared/break-windows.ts#L89)

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
