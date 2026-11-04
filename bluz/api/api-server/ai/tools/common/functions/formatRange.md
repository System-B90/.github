[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/ai/tools/common](../index.md) / formatRange

# Function: formatRange()

> **formatRange**(`start`, `end`): `string`

Defined in: [ui/src/api-server/ai/tools/common.ts:99](https://github.com/System-B90/Bluz/blob/901cc8f4c754d82c12fc600337c5991c07a64502/ui/src/api-server/ai/tools/common.ts#L99)

Renders a range the way the approval card should show it.

The card is the last thing a human reads before agreeing to a change, and
`2026-03-01T09:00:00Z` is not something anyone verifies correctly at a
glance. An unparsable value falls through to the raw string rather than
throwing: this runs inside `describe`, which must never break the gate it
is describing.

## Parameters

### start

`string`

### end

`string`

## Returns

`string`
