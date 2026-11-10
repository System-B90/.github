[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/app-commands/use-schedule-commands](../index.md) / useScheduleCommands

# Function: useScheduleCommands()

> **useScheduleCommands**(`__namedParameters`): `void`

Defined in: [ui/src/components/app-commands/use-schedule-commands.tsx:80](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/components/app-commands/use-schedule-commands.tsx#L80)

Schedule-page commands.

These reach into page-local state (the event dialog, the calendar's own
nav/view/toolbar state) and are therefore contributed by the page itself —
they disappear from the palette on the gantt surface, where they would be
meaningless.

## Parameters

### \_\_namedParameters

[`ScheduleCommandActions`](../type-aliases/ScheduleCommandActions.md)

## Returns

`void`
