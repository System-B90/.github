[**TypeDoc API**](../../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../../index.md) / [components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/HoursCourseSelect](../index.md) / HoursCourseSelect

# Variable: HoursCourseSelect

> `const` **HoursCourseSelect**: `React.FC`\<\{ `paths`: [`StudentPath`](../../../../../student-load/type-aliases/StudentPath.md)[]; \}\>

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/HoursCourseSelect.tsx:35](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/HoursCourseSelect.tsx#L35)

Picks the course the hours totals are for. Hidden while there is only one
kind of student. Keys and clicks stay inside, so the grid's arrow keys and
the header's zoom-on-click don't fire through it (menu portals included).
