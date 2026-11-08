[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/app-commands/use-schedule-commands](../index.md) / useScheduleCommands

# Function: useScheduleCommands()

> **useScheduleCommands**(`__namedParameters`): `void`

Defined in: [ui/src/components/app-commands/use-schedule-commands.tsx:80](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/components/app-commands/use-schedule-commands.tsx#L80)

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
