[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/app-commands/use-schedule-event-commands](../index.md) / useScheduleEventCommands

# Function: useScheduleEventCommands()

> **useScheduleEventCommands**(`__namedParameters`): `void`

Defined in: [ui/src/components/app-commands/use-schedule-event-commands.tsx:24](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/app-commands/use-schedule-event-commands.tsx#L24)

Entity lane over the events currently loaded on the schedule page — the
palette equivalent of scrolling the calendar to find one. Scoped to
whatever range the calendar has fetched (`startDate`/`endDate`), so it
only ever lists what's actually on screen.

Contributed by the schedule page only — the calendar owns the loaded event
list, and there is no equivalent surface on the gantt page.

## Parameters

### \_\_namedParameters

[`ScheduleEventCommandActions`](../type-aliases/ScheduleEventCommandActions.md)

## Returns

`void`
