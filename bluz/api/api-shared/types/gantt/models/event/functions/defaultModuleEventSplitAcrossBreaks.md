[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [api-shared/types/gantt/models/event](../index.md) / defaultModuleEventSplitAcrossBreaks

# Function: defaultModuleEventSplitAcrossBreaks()

> **defaultModuleEventSplitAcrossBreaks**(`type`): `boolean`

Defined in: [ui/src/api-shared/types/gantt/models/event.ts:106](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/api-shared/types/gantt/models/event.ts#L106)

Default value for `splitAcrossBreaks` when an event's type is picked/changed:
on for exercises, off for everything else.

## Parameters

### type

[`ModuleEventType`](../enumerations/ModuleEventType.md)

The ModuleEventType to check.

## Returns

`boolean`

The default `splitAcrossBreaks` value for that type.
