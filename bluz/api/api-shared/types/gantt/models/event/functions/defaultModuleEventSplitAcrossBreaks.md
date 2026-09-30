[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [api-shared/types/gantt/models/event](../index.md) / defaultModuleEventSplitAcrossBreaks

# Function: defaultModuleEventSplitAcrossBreaks()

> **defaultModuleEventSplitAcrossBreaks**(`type`): `boolean`

Defined in: [ui/src/api-shared/types/gantt/models/event.ts:98](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-shared/types/gantt/models/event.ts#L98)

Default value for `splitAcrossBreaks` when an event's type is picked/changed:
on for exercises, off for everything else.

## Parameters

### type

[`ModuleEventType`](../enumerations/ModuleEventType.md)

The ModuleEventType to check.

## Returns

`boolean`

The default `splitAcrossBreaks` value for that type.
