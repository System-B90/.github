[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/shuffle-course-links](../index.md) / syncCurrentIterationShuffleCourseLinks

# Function: syncCurrentIterationShuffleCourseLinks()

> **syncCurrentIterationShuffleCourseLinks**(): `Promise`\<`number`\>

Defined in: [ui/src/api-server/gantt/shuffle-course-links.ts:115](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-server/gantt/shuffle-course-links.ts#L115)

Boot-time backfill for the current iteration: courses cut before a shuffle
was linked never got the link. Idempotent, so it runs on every start.
Never throws.

## Returns

`Promise`\<`number`\>

How many courses were relinked.
