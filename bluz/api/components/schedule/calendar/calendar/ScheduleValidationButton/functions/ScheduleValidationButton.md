[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/calendar/ScheduleValidationButton](../index.md) / ScheduleValidationButton

# Function: ScheduleValidationButton()

> **ScheduleValidationButton**(`__namedParameters`): `Element`

Defined in: [ui/src/components/schedule/calendar/calendar/ScheduleValidationButton.tsx:66](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/components/schedule/calendar/calendar/ScheduleValidationButton.tsx#L66)

"בדיקת חוקי לו״ז": checks the shown week — the live calendar or the loaded
draft, whichever is on screen — against every mechanically checkable rule
(`rule-ids.ts`). One request per rule, one at a time, in rule order; each
rule's result shows as it lands. A failed rule offers a retry and doesn't
stop the rest. Closing the popover or moving the range cancels the run.
A violation row jumps to its events.

## Parameters

### \_\_namedParameters

#### onReveal

(`eventIds`, `date`) => `void`

## Returns

`Element`
