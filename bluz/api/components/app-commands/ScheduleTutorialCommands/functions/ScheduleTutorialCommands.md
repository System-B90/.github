[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/app-commands/ScheduleTutorialCommands](../index.md) / ScheduleTutorialCommands

# Function: ScheduleTutorialCommands()

> **ScheduleTutorialCommands**(): `null`

Defined in: [ui/src/components/app-commands/ScheduleTutorialCommands.tsx:20](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/components/app-commands/ScheduleTutorialCommands.tsx#L20)

The help panel and each schedule tutorial, from the palette: typing "הדרכה"
finds every tutorial even while the toolbar, and with it the "?" button, is
hidden.

Renders nothing — mount it inside the schedule calendar. A component rather
than a hook the calendar calls, because it reads the onboarding state: as a
hook it would re-render the whole grid on every tour step.

## Returns

`null`
