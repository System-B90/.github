[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/instructor-dnd/assign](../index.md) / PersonMovePlan

# Type Alias: PersonMovePlan

> **PersonMovePlan** = \{ `allowed`: `false`; `reason`: `"locked-source"` \| `"target-cannot-hold"`; \} \| \{ `allowed`: `true`; `field`: [`PersonField`](../../types/type-aliases/PersonField.md); \}

Defined in: [ui/src/components/schedule/calendar/instructor-dnd/assign.ts:45](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/calendar/instructor-dnd/assign.ts#L45)

Why a chip dragged from one event to another cannot make the trip, or the
field it lands in when it can.

A move is two writes, and both have to be possible before either happens:
the source giving the person up, and the target taking them. Deciding that
up front is what stops a person being dropped from the source and added
nowhere (#625), or added to the target while a locked source keeps them
(#626).
