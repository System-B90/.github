[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/schedule-validation](../index.md) / ScheduleSource

# Type Alias: ScheduleSource

> **ScheduleSource** = \{ `draftId`: `string`; \} \| \{ `end`: `Date`; `start`: `Date`; \} \| \{ `events`: [`RuleCheckEvent`](../../../api-shared/schedule-validation/types/type-aliases/RuleCheckEvent.md)[]; \}

Defined in: [ui/src/api-server/schedule-validation.ts:29](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-server/schedule-validation.ts#L29)

What a check runs over: the live calendar in a range, a saved draft, or inline events.
