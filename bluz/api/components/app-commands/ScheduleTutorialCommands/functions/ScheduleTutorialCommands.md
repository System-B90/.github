[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/app-commands/ScheduleTutorialCommands](../index.md) / ScheduleTutorialCommands

# Function: ScheduleTutorialCommands()

> **ScheduleTutorialCommands**(): `null`

Defined in: [ui/src/components/app-commands/ScheduleTutorialCommands.tsx:20](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/components/app-commands/ScheduleTutorialCommands.tsx#L20)

The help panel and each schedule tutorial, from the palette: typing "הדרכה"
finds every tutorial even while the toolbar, and with it the "?" button, is
hidden.

Renders nothing — mount it inside the schedule calendar. A component rather
than a hook the calendar calls, because it reads the onboarding state: as a
hook it would re-render the whole grid on every tour step.

## Returns

`null`
