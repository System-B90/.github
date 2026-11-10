[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/schedule-validation](../index.md) / ScheduleSource

# Type Alias: ScheduleSource

> **ScheduleSource** = \{ `draftId`: `string`; \} \| \{ `end`: `Date`; `start`: `Date`; \} \| \{ `events`: [`RuleCheckEvent`](../../../api-shared/schedule-validation/types/type-aliases/RuleCheckEvent.md)[]; \}

Defined in: [ui/src/api-server/schedule-validation.ts:29](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-server/schedule-validation.ts#L29)

What a check runs over: the live calendar in a range, a saved draft, or inline events.
