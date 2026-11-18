[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/gantt/BedtimeReminder](../index.md) / BedtimeReminder

# Function: BedtimeReminder()

> **BedtimeReminder**(): `Element`

Defined in: [ui/src/components/gantt/BedtimeReminder.tsx:36](https://github.com/System-B90/Bluz/blob/04ebae9cb334a01c6e7a55f885993f021e83cd92/ui/src/components/gantt/BedtimeReminder.tsx#L36)

Friendly nudge to go to sleep when the Gantt page is in use late at night.
Checks the local clock every minute while the tab is visible; after the
user dismisses a reminder, the next one waits SNOOZE\_MS.

## Returns

`Element`
