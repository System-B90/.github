[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/recurrence](../index.md) / isRecurrenceSatisfied

# Function: isRecurrenceSatisfied()

> **isRecurrenceSatisfied**(`recurrence`, `startWeekIdx`, `firstRequiredWeekIdx?`): `boolean`

Defined in: [ui/src/api-shared/gantt/recurrence.ts:149](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/api-shared/gantt/recurrence.ts#L149)

Whether a recurring event's obligation is met: an occurrence exists in every
week the recurrence is supposed to cover. Since occurrences echo forward from
the start week, this holds exactly when the event starts on or before the
first required week — week 0 by default, or the week holding the configured
recurrence start date when one is set (#468).
Unmapped events (`startWeekIdx < 0`) are never satisfied. Non-recurring events
carry no obligation and are always considered satisfied.

## Parameters

### recurrence

[`EventRecurrence`](../../../types/gantt/models/event/enumerations/EventRecurrence.md)

### startWeekIdx

`number`

### firstRequiredWeekIdx?

`number` = `0`

## Returns

`boolean`
