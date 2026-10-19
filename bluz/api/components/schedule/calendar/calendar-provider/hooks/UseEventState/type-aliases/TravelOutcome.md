[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [components/schedule/calendar/calendar-provider/hooks/UseEventState](../index.md) / TravelOutcome

# Type Alias: TravelOutcome

> **TravelOutcome** = `"applied"` \| `"conflict"` \| `"empty"`

Defined in: [ui/src/components/schedule/calendar/calendar-provider/hooks/UseEventState.ts:252](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/components/schedule/calendar/calendar-provider/hooks/UseEventState.ts#L252)

What one undo/redo did: `empty` when there was no step to take, `conflict`
when every event in it had since been changed by someone else (so the step
was dropped without touching them), `applied` otherwise.
