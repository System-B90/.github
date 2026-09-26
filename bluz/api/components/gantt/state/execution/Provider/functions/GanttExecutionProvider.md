[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/gantt/state/execution/Provider](../index.md) / GanttExecutionProvider

# Function: GanttExecutionProvider()

> **GanttExecutionProvider**(`__namedParameters`): `Element`

Defined in: [ui/src/components/gantt/state/execution/Provider.tsx:43](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/gantt/state/execution/Provider.tsx#L43)

Read-only תכנון מול ביצוע state (#121): loads the plan-vs-actual comparison
for the curriculum once and exposes a manual refresh (the event dialog
refreshes on open so the comparison is current). Load failures degrade to an
empty comparison — the gantt renders exactly as if the curriculum was not
cut — rather than surfacing an error for a purely informational overlay.

## Parameters

### \_\_namedParameters

#### children

`ReactNode`

#### curriculumId

`string`

## Returns

`Element`
