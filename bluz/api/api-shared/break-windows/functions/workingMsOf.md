[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/break-windows](../index.md) / workingMsOf

# Function: workingMsOf()

> **workingMsOf**(`event`): `number`

Defined in: [ui/src/api-shared/break-windows.ts:52](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/api-shared/break-windows.ts#L52)

Net working length of an event. `endTime` is a derivative of `startTime` and
this duration — it is never inflated by the breaks the event steps over.

## Parameters

### event

`Pick`\<[`SplittableEvent`](../type-aliases/SplittableEvent.md), `"endTime"` \| `"startTime"`\>

## Returns

`number`
