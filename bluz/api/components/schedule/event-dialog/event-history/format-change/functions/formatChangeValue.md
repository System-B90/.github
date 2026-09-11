[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/event-dialog/event-history/format-change](../index.md) / formatChangeValue

# Function: formatChangeValue()

> **formatChangeValue**(`field`, `value`, `lookups`, `timeOnly?`): `string`

Defined in: [ui/src/components/schedule/event-dialog/event-history/format-change.ts:60](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/schedule/event-dialog/event-history/format-change.ts#L60)

Format one side of a change for display.

## Parameters

### field

`string`

The field the value belongs to (drives the formatting).

### value

`unknown`

The raw logged value.

### lookups

[`ChangeValueLookups`](../type-aliases/ChangeValueLookups.md)

Name resolvers for id-shaped values.

### timeOnly?

`boolean` = `false`

## Returns

`string`

A human-readable string; an em dash for empty/absent values.

## Example

```typescript
formatChangeValue("startTime", 1704614400000, lookups); // "07/01/2024 08:00"
```
