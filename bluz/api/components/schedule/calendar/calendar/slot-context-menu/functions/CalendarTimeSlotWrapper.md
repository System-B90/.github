[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/calendar/slot-context-menu](../index.md) / CalendarTimeSlotWrapper

# Function: CalendarTimeSlotWrapper()

> **CalendarTimeSlotWrapper**(`__namedParameters`): `ReactNode`

Defined in: [ui/src/components/schedule/calendar/calendar/slot-context-menu.tsx:20](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/components/schedule/calendar/calendar/slot-context-menu.tsx#L20)

react-big-calendar `timeSlotWrapper`: stamps each slot with its start time
and room column so a right-click can be resolved to a paste target. Events
are drawn in an overlay above the slots, so the slot is found by position
([slotUnderPointer](slotUnderPointer.md)) rather than by the click's own target.

## Parameters

### \_\_namedParameters

`PropsWithChildren`\<\{ `resource?`: `string` \| `number`; `value?`: `Date`; \}\>

## Returns

`ReactNode`
