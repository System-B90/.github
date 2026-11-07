[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/event](../index.md) / defaultSplitAcrossBreaks

# Function: defaultSplitAcrossBreaks()

> **defaultSplitAcrossBreaks**(`type`): `boolean`

Defined in: [ui/src/api-shared/types/event.ts:246](https://github.com/System-B90/Bluz/blob/1b02178048002eee34d502b2e3e2a402e1b9c9c0/ui/src/api-shared/types/event.ts#L246)

Default value for `splitAcrossBreaks` when an event's type is picked/changed:
on for exercises and workshops, off for everything else (lectures included).

## Parameters

### type

[`EventType`](../enumerations/EventType.md)

The EventType to check.

## Returns

`boolean`

The default `splitAcrossBreaks` value for that type.
