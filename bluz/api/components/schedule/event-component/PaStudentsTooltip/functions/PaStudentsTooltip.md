[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/schedule/event-component/PaStudentsTooltip](../index.md) / PaStudentsTooltip

# Function: PaStudentsTooltip()

> **PaStudentsTooltip**(`__namedParameters`): `Element`

Defined in: [ui/src/components/schedule/event-component/PaStudentsTooltip.tsx:25](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/components/schedule/event-component/PaStudentsTooltip.tsx#L25)

Tooltip body of an event's פ"א icon: which of the PA instructor's students
(Hive mentees) are in the event's shuffles/courses, and so can be taken out
of it for a personal talk. Mounted only while the tooltip is open, so the
lookup runs on hover, never per tile.

## Parameters

### \_\_namedParameters

#### event

`Pick`\<[`Event`](../../../../../api-shared/types/event/type-aliases/Event.md), `"courses"`\>

## Returns

`Element`
