[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [api-shared/types/gantt/models/event](../index.md) / defaultModuleEventSplitAcrossBreaks

# Function: defaultModuleEventSplitAcrossBreaks()

> **defaultModuleEventSplitAcrossBreaks**(`type`): `boolean`

Defined in: [ui/src/api-shared/types/gantt/models/event.ts:106](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/api-shared/types/gantt/models/event.ts#L106)

Default value for `splitAcrossBreaks` when an event's type is picked/changed:
on for exercises, off for everything else.

## Parameters

### type

[`ModuleEventType`](../enumerations/ModuleEventType.md)

The ModuleEventType to check.

## Returns

`boolean`

The default `splitAcrossBreaks` value for that type.
