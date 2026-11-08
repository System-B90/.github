[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/split/SplitCalendarContext](../index.md) / useDragOf

# Function: useDragOf()

> **useDragOf**(`eventId`): [`ActiveDrag`](../type-aliases/ActiveDrag.md) \| `null`

Defined in: [ui/src/components/schedule/calendar/split/SplitCalendarContext.tsx:130](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/components/schedule/calendar/split/SplitCalendarContext.tsx#L130)

The drag in flight if it is `eventId`'s, else `null`. Every other tile gets
`null` throughout a drag and never re-renders for it.

## Parameters

### eventId

`string`

## Returns

[`ActiveDrag`](../type-aliases/ActiveDrag.md) \| `null`
