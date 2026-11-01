[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/week-template-cut](../index.md) / buildTemplatePins

# Function: buildTemplatePins()

> **buildTemplatePins**(`args`): [`CutPlanPinInput`](../../../../api-shared/gantt/cut-planner/type-aliases/CutPlanPinInput.md)[]

Defined in: [ui/src/api-server/gantt/week-template-cut.ts:134](https://github.com/System-B90/Bluz/blob/2fa23325da73d58527b069b0943f3bd1e838efee/ui/src/api-server/gantt/week-template-cut.ts#L134)

Pins for every gantt event a template places (#997).

A placed (not parked) template event matches a gantt event by name and by
course name. Its courses are mapped onto the iteration by name; when it has
courses and none of them exist there, it is dropped. One without courses
matches on name alone. Each match pins the event in every week given, and
the planner drops a pin whose event has no occurrence on that day.

A daily-recurring event placed once (say on Sunday 07:00) is pinned at that
time on every other weekday too, unless the template places it on that
weekday itself. Placing it seven times is never required.

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
