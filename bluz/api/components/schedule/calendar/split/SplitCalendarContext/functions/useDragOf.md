[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/split/SplitCalendarContext](../index.md) / useDragOf

# Function: useDragOf()

> **useDragOf**(`eventId`): [`ActiveDrag`](../type-aliases/ActiveDrag.md) \| `null`

Defined in: [ui/src/components/schedule/calendar/split/SplitCalendarContext.tsx:130](https://github.com/System-B90/Bluz/blob/2fa23325da73d58527b069b0943f3bd1e838efee/ui/src/components/schedule/calendar/split/SplitCalendarContext.tsx#L130)

The drag in flight if it is `eventId`'s, else `null`. Every other tile gets
`null` throughout a drag and never re-renders for it.

## Parameters

### eventId

`string`

## Returns

[`ActiveDrag`](../type-aliases/ActiveDrag.md) \| `null`
