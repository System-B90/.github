[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/student-view](../index.md) / requireStudentViewSession

# Function: requireStudentViewSession()

> **requireStudentViewSession**(): `Promise`\<[`StudentViewSession`](../type-aliases/StudentViewSession.md)\>

Defined in: [ui/src/api-server/student-view.ts:55](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/api-server/student-view.ts#L55)

Gates the student-view endpoint. Unlike every other API route this one is
reachable by a Hanich session — it is the single endpoint that is. Anything
below Hanich (i.e. no session at all) is rejected: every student reaches
Bluz through a Hive sign-in, so there is no anonymous viewer to serve.

## Returns

`Promise`\<[`StudentViewSession`](../type-aliases/StudentViewSession.md)\>
