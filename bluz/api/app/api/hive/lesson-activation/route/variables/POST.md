[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [app/api/hive/lesson-activation/route](../index.md) / POST

# Variable: POST

> `const` **POST**: `ServerApiLessonActivationRun`

Defined in: [ui/src/app/api/hive/lesson-activation/route.ts:21](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/app/api/hive/lesson-activation/route.ts#L21)

POST /api/hive/lesson-activation — run one activation pass now and report
what it did.

The pass is what the background timer runs every 30 seconds, and it is
idempotent, so triggering it by hand can only ever bring the queues forward
to where they should already be. It exists because the timer is otherwise
invisible: when a queue does not open, this is how staff (and the e2e
suite) find out whether the event was even considered, and why not.
