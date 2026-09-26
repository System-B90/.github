[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/gantt/curriculum-fab/action-items/CutToScheduleAction](../index.md) / CutToScheduleAction

# Function: CutToScheduleAction()

> **CutToScheduleAction**(`__namedParameters`): `Element`

Defined in: [ui/src/components/gantt/curriculum-fab/action-items/CutToScheduleAction.tsx:22](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/gantt/curriculum-fab/action-items/CutToScheduleAction.tsx#L22)

"גזירה ללו"ז" / "משיכה חזרה" — a single status-aware action. Once a
curriculum has been cut, the cut button is replaced by a pull-back button
that soft-deletes the generated schedule events. Cut status is fetched from
the endpoint and re-synced whenever either action succeeds. Draft gating and
every other precondition are enforced server-side and surfaced by the dialog.

## Parameters

### \_\_namedParameters

[`CurriculumAwareActionItemProps`](../../ActionItemProps/type-aliases/CurriculumAwareActionItemProps.md)

## Returns

`Element`
