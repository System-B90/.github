[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/split/SplitCalendarContext](../index.md) / useDragOf

# Function: useDragOf()

> **useDragOf**(`eventId`): [`ActiveDrag`](../type-aliases/ActiveDrag.md) \| `null`

Defined in: [ui/src/components/schedule/calendar/split/SplitCalendarContext.tsx:130](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/components/schedule/calendar/split/SplitCalendarContext.tsx#L130)

The drag in flight if it is `eventId`'s, else `null`. Every other tile gets
`null` throughout a drag and never re-renders for it.

## Parameters

### eventId

`string`

## Returns

[`ActiveDrag`](../type-aliases/ActiveDrag.md) \| `null`
