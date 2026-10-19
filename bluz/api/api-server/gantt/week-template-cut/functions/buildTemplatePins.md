[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/week-template-cut](../index.md) / buildTemplatePins

# Function: buildTemplatePins()

> **buildTemplatePins**(`args`): [`CutPlanPinInput`](../../../../api-shared/gantt/cut-planner/type-aliases/CutPlanPinInput.md)[]

Defined in: [ui/src/api-server/gantt/week-template-cut.ts:117](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/api-server/gantt/week-template-cut.ts#L117)

Pins for every gantt event a template places (#997).

A placed (not parked) template event matches a gantt event by name and by
course name. Its courses are mapped onto the iteration by name; when it has
courses and none of them exist there, it is dropped. One without courses
matches on name alone. Each match pins the event in every week given, and
the planner drops a pin whose event has no occurrence on that day.

## Parameters

### args

#### iterationCourseNames

`Set`\<`string`\>

#### targets

[`TemplateMatchTarget`](../type-aliases/TemplateMatchTarget.md)[]

#### templateEvents

[`WeekTemplateEventDocument`](../../../../api-shared/types/week-template/type-aliases/WeekTemplateEventDocument.md)[]

#### weekIds

`string`[]

## Returns

[`CutPlanPinInput`](../../../../api-shared/gantt/cut-planner/type-aliases/CutPlanPinInput.md)[]
