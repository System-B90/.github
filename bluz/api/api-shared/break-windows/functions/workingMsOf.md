[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/break-windows](../index.md) / workingMsOf

# Function: workingMsOf()

> **workingMsOf**(`event`): `number`

Defined in: [ui/src/api-shared/break-windows.ts:50](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/break-windows.ts#L50)

Net working length of an event. `endTime` is a derivative of `startTime` and
this duration — it is never inflated by the breaks the event steps over.

## Parameters

### event

`Pick`\<[`SplittableEvent`](../type-aliases/SplittableEvent.md), `"endTime"` \| `"startTime"`\>

## Returns

`number`
