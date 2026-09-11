[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/student-view](../index.md) / requireStudentViewSession

# Function: requireStudentViewSession()

> **requireStudentViewSession**(): `Promise`\<[`StudentViewSession`](../type-aliases/StudentViewSession.md)\>

Defined in: [ui/src/api-server/student-view.ts:41](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/student-view.ts#L41)

Gates the student-view endpoint. Unlike every other API route this one is
reachable by a Hanich session — it is the single endpoint that is. Anything
below Hanich (i.e. no session at all) is rejected.

## Returns

`Promise`\<[`StudentViewSession`](../type-aliases/StudentViewSession.md)\>
