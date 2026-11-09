[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [app/api/student-view/schedule/route](../index.md) / GET

# Variable: GET

> `const` **GET**: `ServerApiStudentScheduleGet`

Defined in: [ui/src/app/api/student-view/schedule/route.ts:37](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/app/api/student-view/schedule/route.ts#L37)

The only endpoint a student session may call (#656). It is read-only, serves
a single day, and returns the `StudentEvent` projection — never a raw event
document. There is deliberately no POST/PUT/DELETE here.

Iteration scoping: students are pinned to the current iteration. Staff may
pass `?it=` while previewing, exactly as the rest of the calendar does.

Shuffle selection takes no parameter: the response names the student's own
shuffles (`ownCourses`, from their own Hive login) and the board filters the
delivered day itself, so the query string stays empty for a student and
any parameter at all is still tampering.
