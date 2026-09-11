[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/break-windows](../index.md) / workingMsOf

# Function: workingMsOf()

> **workingMsOf**(`event`): `number`

Defined in: [ui/src/api-shared/break-windows.ts:45](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/break-windows.ts#L45)

Net working length of an event. `endTime` is a derivative of `startTime` and
this duration — it is never inflated by the breaks the event steps over.

## Parameters

### event

`Pick`\<[`SplittableEvent`](../type-aliases/SplittableEvent.md), `"endTime"` \| `"startTime"`\>

## Returns

`number`
