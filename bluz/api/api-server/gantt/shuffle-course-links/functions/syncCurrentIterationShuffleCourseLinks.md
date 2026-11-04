[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/shuffle-course-links](../index.md) / syncCurrentIterationShuffleCourseLinks

# Function: syncCurrentIterationShuffleCourseLinks()

> **syncCurrentIterationShuffleCourseLinks**(): `Promise`\<`number`\>

Defined in: [ui/src/api-server/gantt/shuffle-course-links.ts:115](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/api-server/gantt/shuffle-course-links.ts#L115)

Boot-time backfill for the current iteration: courses cut before a shuffle
was linked never got the link. Idempotent, so it runs on every start.
Never throws.

## Returns

`Promise`\<`number`\>

How many courses were relinked.
