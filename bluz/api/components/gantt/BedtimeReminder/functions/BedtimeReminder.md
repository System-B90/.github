[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/gantt/BedtimeReminder](../index.md) / BedtimeReminder

# Function: BedtimeReminder()

> **BedtimeReminder**(): `Element`

Defined in: [ui/src/components/gantt/BedtimeReminder.tsx:36](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/components/gantt/BedtimeReminder.tsx#L36)

Friendly nudge to go to sleep when the Gantt page is in use late at night.
Checks the local clock every minute while the tab is visible; after the
user dismisses a reminder, the next one waits SNOOZE\_MS.

## Returns

`Element`
