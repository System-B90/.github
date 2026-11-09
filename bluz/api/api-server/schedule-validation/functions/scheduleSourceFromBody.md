[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/schedule-validation](../index.md) / scheduleSourceFromBody

# Function: scheduleSourceFromBody()

> **scheduleSourceFromBody**(`body`): [`ScheduleSource`](../type-aliases/ScheduleSource.md)

Defined in: [ui/src/api-server/schedule-validation.ts:38](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-server/schedule-validation.ts#L38)

The source a validation body names: `{ events }` (unsaved draft),
`{ draftId }` (saved draft) or `{ start, end }` (live calendar).

## Parameters

### body

[`RuleValidationRequest`](../../../api-shared/schedule-validation/types/type-aliases/RuleValidationRequest.md)

## Returns

[`ScheduleSource`](../type-aliases/ScheduleSource.md)
