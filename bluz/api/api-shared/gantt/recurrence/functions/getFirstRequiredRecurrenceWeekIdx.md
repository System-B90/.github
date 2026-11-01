[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/recurrence](../index.md) / getFirstRequiredRecurrenceWeekIdx

# Function: getFirstRequiredRecurrenceWeekIdx()

> **getFirstRequiredRecurrenceWeekIdx**(`recurrenceStartDate`, `weeks`, `dateOf`): `number`

Defined in: [ui/src/api-shared/gantt/recurrence.ts:165](https://github.com/System-B90/Bluz/blob/2fa23325da73d58527b069b0943f3bd1e838efee/ui/src/api-shared/gantt/recurrence.ts#L165)

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
