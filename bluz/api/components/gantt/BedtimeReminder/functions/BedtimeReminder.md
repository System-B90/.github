[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/gantt/BedtimeReminder](../index.md) / BedtimeReminder

# Function: BedtimeReminder()

> **BedtimeReminder**(): `Element`

Defined in: [ui/src/components/gantt/BedtimeReminder.tsx:36](https://github.com/System-B90/Bluz/blob/d77dcf130db661461363a52910f62a34b3514ebd/ui/src/components/gantt/BedtimeReminder.tsx#L36)

Friendly nudge to go to sleep when the Gantt page is in use late at night.
Checks the local clock every minute while the tab is visible; after the
user dismisses a reminder, the next one waits SNOOZE\_MS.

## Returns

`Element`
