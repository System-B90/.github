[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/break-windows](../index.md) / breakAppliesTo

# Function: breakAppliesTo()

> **breakAppliesTo**(`window`, `event`): `boolean`

Defined in: [ui/src/api-shared/break-windows.ts:89](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/api-shared/break-windows.ts#L89)

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
