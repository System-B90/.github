[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/recurrence](../index.md) / isRecurrenceSatisfied

# Function: isRecurrenceSatisfied()

> **isRecurrenceSatisfied**(`recurrence`, `startWeekIdx`, `firstRequiredWeekIdx?`): `boolean`

Defined in: [ui/src/api-shared/gantt/recurrence.ts:139](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/gantt/recurrence.ts#L139)

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
