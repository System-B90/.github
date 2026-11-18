[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/event](../index.md) / defaultSplitAcrossBreaks

# Function: defaultSplitAcrossBreaks()

> **defaultSplitAcrossBreaks**(`type`): `boolean`

Defined in: [ui/src/api-shared/types/event.ts:271](https://github.com/System-B90/Bluz/blob/04ebae9cb334a01c6e7a55f885993f021e83cd92/ui/src/api-shared/types/event.ts#L271)

Default value for `splitAcrossBreaks` when an event's type is picked/changed:
on for exercises and workshops, off for everything else (lectures included).

## Parameters

### type

[`EventType`](../enumerations/EventType.md)

The EventType to check.

## Returns

`boolean`

The default `splitAcrossBreaks` value for that type.
