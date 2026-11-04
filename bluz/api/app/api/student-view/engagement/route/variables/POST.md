[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [app/api/student-view/engagement/route](../index.md) / POST

# Variable: POST

> `const` **POST**: `ServerApiStudentEngagementPost`

Defined in: [ui/src/app/api/student-view/engagement/route.ts:40](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/app/api/student-view/engagement/route.ts#L40)

Records how long the student-view board has been open *and* focused (#656).

The body carries a duration and nothing else: the user id comes from the
session and the date from the server clock, so a student can only ever add
to their own counter, for today. The increment is clamped and the daily
total capped in `db-student-engagement`, so a forged report buys at most a
day's worth of seconds against the reporter's own number.

Staff previewing the board report too; their rows are simply never read.
