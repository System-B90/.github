[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/instructor-dnd/assign](../index.md) / PersonMovePlan

# Type Alias: PersonMovePlan

> **PersonMovePlan** = \{ `allowed`: `false`; `reason`: `"target-cannot-hold"`; \} \| \{ `allowed`: `true`; `field`: [`PersonField`](../../types/type-aliases/PersonField.md); \}

Defined in: [ui/src/components/schedule/calendar/instructor-dnd/assign.ts:47](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/components/schedule/calendar/instructor-dnd/assign.ts#L47)

Why a chip dragged from one event to another cannot make the trip, or the
field it lands in when it can.

A move is two writes, and both have to be possible before either happens:
the source giving the person up, and the target taking them. Deciding that
up front is what stops a person being dropped from the source and added
nowhere (#625). A locked (מתואם) source gives people up like any other:
the lock pins timing, not staffing (#1016).
