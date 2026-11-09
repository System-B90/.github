[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/schedule/event-context-menu/SliceDialog](../index.md) / halfWorkingMs

# Function: halfWorkingMs()

> **halfWorkingMs**(`event`): `number`

Defined in: [ui/src/components/schedule/event-context-menu/SliceDialog.tsx:39](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/components/schedule/event-context-menu/SliceDialog.tsx#L39)

Half the event's working time, rounded to the nearest 5 minutes, so both
pieces are multiples of 5 whenever the whole is (45 → 25 + 20). An event too
short to give two 5-minute pieces is refused by the slice itself.

## Parameters

### event

[`Event`](../../../../../api-shared/types/event/type-aliases/Event.md)

## Returns

`number`
