[**TypeDoc API**](../../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../../index.md) / [components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/grid-allotment](../index.md) / planWeekAllotment

# Function: planWeekAllotment()

> **planWeekAllotment**(`input`): [`AllotmentPlan`](../type-aliases/AllotmentPlan.md)

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/grid-allotment.ts:52](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/grid-allotment.ts#L52)

Plans a week-cell edit. Mappings already in the week take the new value
(several: the last one absorbs the difference). An empty week gets a
mapping on the same weekday as the event's first mapping.

## Parameters

### input

[`AllotmentInput`](../type-aliases/AllotmentInput.md)

## Returns

[`AllotmentPlan`](../type-aliases/AllotmentPlan.md)
