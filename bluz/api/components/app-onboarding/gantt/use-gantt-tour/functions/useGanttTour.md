[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/app-onboarding/gantt/use-gantt-tour](../index.md) / useGanttTour

# Function: useGanttTour()

> **useGanttTour**(`setSelectedTabIndex`): `void`

Defined in: [ui/src/components/app-onboarding/gantt/use-gantt-tour.tsx:42](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/app-onboarding/gantt/use-gantt-tour.tsx#L42)

The first-run walkthrough of the gantt screen (#659).

Five concepts, in the order a planner meets them: what a gantt *is*, where
the content lives, how weeks bound it, what the preview shows, and what
cutting to the schedule does and does not touch. The last one is the reason
the tour exists — new users would not risk cutting because nothing told them
it neither overwrites nor deletes what is already on the schedule.

Registered by the component that owns the tab state, since the tour drives
the tabs as it goes.

## Parameters

### setSelectedTabIndex

`Dispatch`\<`SetStateAction`\<`number`\>\>

## Returns

`void`
