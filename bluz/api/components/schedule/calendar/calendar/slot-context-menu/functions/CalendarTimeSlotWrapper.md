[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/calendar/slot-context-menu](../index.md) / CalendarTimeSlotWrapper

# Function: CalendarTimeSlotWrapper()

> **CalendarTimeSlotWrapper**(`__namedParameters`): `ReactNode`

Defined in: [ui/src/components/schedule/calendar/calendar/slot-context-menu.tsx:32](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/components/schedule/calendar/calendar/slot-context-menu.tsx#L32)

react-big-calendar `timeSlotWrapper`: stamps each slot with its start time
and room column so a right-click can be resolved to a paste target. Events
are drawn in an overlay above the slots, so the slot is found by position
([slotUnderPointer](slotUnderPointer.md)) rather than by the click's own target.

## Parameters

### \_\_namedParameters

`PropsWithChildren`\<\{ `resource?`: `string` \| `number`; `value?`: `Date`; \}\>

## Returns

`ReactNode`
