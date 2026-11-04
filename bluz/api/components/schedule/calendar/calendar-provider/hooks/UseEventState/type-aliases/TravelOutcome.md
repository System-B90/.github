[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [components/schedule/calendar/calendar-provider/hooks/UseEventState](../index.md) / TravelOutcome

# Type Alias: TravelOutcome

> **TravelOutcome** = `"applied"` \| `"conflict"` \| `"empty"`

Defined in: [ui/src/components/schedule/calendar/calendar-provider/hooks/UseEventState.ts:272](https://github.com/System-B90/Bluz/blob/901cc8f4c754d82c12fc600337c5991c07a64502/ui/src/components/schedule/calendar/calendar-provider/hooks/UseEventState.ts#L272)

What one undo/redo did: `empty` when there was no step to take, `conflict`
when every event in it had since been changed by someone else (so the step
was dropped without touching them), `applied` otherwise.
