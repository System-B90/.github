[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/app-commands/use-schedule-commands](../index.md) / useScheduleCommands

# Function: useScheduleCommands()

> **useScheduleCommands**(`__namedParameters`): `void`

Defined in: [ui/src/components/app-commands/use-schedule-commands.tsx:44](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/components/app-commands/use-schedule-commands.tsx#L44)

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
