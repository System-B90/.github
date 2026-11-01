[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [api-shared/types/gantt/models/event](../index.md) / defaultModuleEventSplitAcrossWeeks

# Function: defaultModuleEventSplitAcrossWeeks()

> **defaultModuleEventSplitAcrossWeeks**(`type`): `boolean`

Defined in: [ui/src/api-shared/types/gantt/models/event.ts:119](https://github.com/System-B90/Bluz/blob/2fa23325da73d58527b069b0943f3bd1e838efee/ui/src/api-shared/types/gantt/models/event.ts#L119)

Default value for `splitAcrossWeeks` when an event's type is picked/changed:
opt-out for exercises, opt-in for everything else (lectures included), the
same defaults as `splitAcrossBreaks` (#768).

## Parameters

### type

[`ModuleEventType`](../enumerations/ModuleEventType.md)

The ModuleEventType to check.

## Returns

`boolean`

The default `splitAcrossWeeks` value for that type.
