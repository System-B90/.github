[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/student-view](../index.md) / requireStudentViewSession

# Function: requireStudentViewSession()

> **requireStudentViewSession**(): `Promise`\<[`StudentViewSession`](../type-aliases/StudentViewSession.md)\>

Defined in: [ui/src/api-server/student-view.ts:64](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/api-server/student-view.ts#L64)

Gates the student-view endpoint. Unlike every other API route this one is
reachable by a Hanich session — it is the single endpoint that is. Anything
below Hanich (i.e. no session at all) is rejected: every student reaches
Bluz through a Hive sign-in, so there is no anonymous viewer to serve.

## Returns

`Promise`\<[`StudentViewSession`](../type-aliases/StudentViewSession.md)\>
