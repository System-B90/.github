[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [app/api/student-view/schedule/route](../index.md) / GET

# Variable: GET

> `const` **GET**: `ServerApiStudentScheduleGet`

Defined in: [ui/src/app/api/student-view/schedule/route.ts:29](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/app/api/student-view/schedule/route.ts#L29)

The only endpoint a student session may call (#656). It is read-only, serves
a single day, and returns the `StudentEvent` projection — never a raw event
document. There is deliberately no POST/PUT/DELETE here.

Iteration scoping: students are pinned to the current iteration. Staff may
pass `?it=` while previewing, exactly as the rest of the calendar does.
