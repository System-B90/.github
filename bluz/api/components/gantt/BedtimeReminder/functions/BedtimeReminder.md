[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/gantt/BedtimeReminder](../index.md) / BedtimeReminder

# Function: BedtimeReminder()

> **BedtimeReminder**(): `Element`

Defined in: [ui/src/components/gantt/BedtimeReminder.tsx:35](https://github.com/System-B90/Bluz/blob/9293ec523a02fdbe59b9479de6b3caee2f4be11c/ui/src/components/gantt/BedtimeReminder.tsx#L35)

Friendly nudge to go to sleep when the Gantt page is in use late at night.
Checks the local clock every minute while the tab is visible; after the
user dismisses a reminder, the next one waits SNOOZE\_MS.

## Returns

`Element`
