[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/recurrence](../index.md) / getFirstRequiredRecurrenceWeekIdx

# Function: getFirstRequiredRecurrenceWeekIdx()

> **getFirstRequiredRecurrenceWeekIdx**(`recurrenceStartDate`, `weeks`, `dateOf`): `number`

Defined in: [ui/src/api-shared/gantt/recurrence.ts:154](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-shared/gantt/recurrence.ts#L154)

Index of the first timeline week the recurrence must cover, given its
configured start date (#468). Returns 0 when there is no start date or it
cannot be resolved to a week, preserving the "must start in week 1" rule.

## Parameters

### recurrenceStartDate

`string` \| `null` \| `undefined`

### weeks

readonly `object`[]

### dateOf

(`dayId`) => `string` \| `undefined`

## Returns

`number`
