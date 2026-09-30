[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/event](../index.md) / defaultSplitAcrossBreaks

# Function: defaultSplitAcrossBreaks()

> **defaultSplitAcrossBreaks**(`type`): `boolean`

Defined in: [ui/src/api-shared/types/event.ts:242](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-shared/types/event.ts#L242)

Default value for `splitAcrossBreaks` when an event's type is picked/changed:
on for exercises and workshops, off for everything else (lectures included).

## Parameters

### type

[`EventType`](../enumerations/EventType.md)

The EventType to check.

## Returns

`boolean`

The default `splitAcrossBreaks` value for that type.
