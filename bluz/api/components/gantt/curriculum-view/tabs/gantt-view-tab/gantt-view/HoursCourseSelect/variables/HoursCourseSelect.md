[**TypeDoc API**](../../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../../index.md) / [components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/HoursCourseSelect](../index.md) / HoursCourseSelect

# Variable: HoursCourseSelect

> `const` **HoursCourseSelect**: `React.FC`\<\{ `paths`: [`StudentPath`](../../../../../student-load/type-aliases/StudentPath.md)[]; \}\>

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/HoursCourseSelect.tsx:36](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/HoursCourseSelect.tsx#L36)

Picks the course the hours totals are for. Hidden while there is only one
kind of student. Keys and clicks stay inside, so the grid's arrow keys and
the header's zoom-on-click don't fire through it (menu portals included).
