[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/week-split](../index.md) / getEffectiveWeekSplit

# Function: getEffectiveWeekSplit()

> **getEffectiveWeekSplit**(`splitAcrossWeeks`, `parts`, `totalMinutes`): `number`[] \| `null`

Defined in: [ui/src/api-shared/gantt/week-split.ts:40](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-shared/gantt/week-split.ts#L40)

The split to apply, or null to run the event whole: only a flagged event
with a complete split is split.

## Parameters

### splitAcrossWeeks

`boolean` \| `undefined`

### parts

`number`[] \| `null` \| `undefined`

### totalMinutes

`number`

## Returns

`number`[] \| `null`
