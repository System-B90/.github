[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/app-onboarding/schedule/ScheduleHelpButton](../index.md) / ScheduleHelpButton

# Function: ScheduleHelpButton()

> **ScheduleHelpButton**(): `Element`

Defined in: [ui/src/components/app-onboarding/schedule/ScheduleHelpButton.tsx:17](https://github.com/System-B90/Bluz/blob/90114c31e10132d84c8c3bab079c25588fbe0459/ui/src/components/app-onboarding/schedule/ScheduleHelpButton.tsx#L17)

The schedule's way into the help panel, and so into every schedule tour.

The gantt has `BluzHelpButton` among its status actions; the schedule had no
"?" at all, which left every tour but the auto-started one unreachable. Its
toolbar takes `ToolbarIconButton`s only (docs/ux-guidelines.md §5.2), hence
a button of its own — registering the same `app.help` anchor, so a tour's
"this is how you get back here" step finds it on either screen.

## Returns

`Element`
