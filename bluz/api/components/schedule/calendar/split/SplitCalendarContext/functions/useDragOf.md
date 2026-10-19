[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/split/SplitCalendarContext](../index.md) / useDragOf

# Function: useDragOf()

> **useDragOf**(`eventId`): [`ActiveDrag`](../type-aliases/ActiveDrag.md) \| `null`

Defined in: [ui/src/components/schedule/calendar/split/SplitCalendarContext.tsx:125](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/components/schedule/calendar/split/SplitCalendarContext.tsx#L125)

The drag in flight if it is `eventId`'s, else `null`. Every other tile gets
`null` throughout a drag and never re-renders for it.

## Parameters

### eventId

`string`

## Returns

[`ActiveDrag`](../type-aliases/ActiveDrag.md) \| `null`
