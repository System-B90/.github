[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/student-view](../index.md) / requireStudentViewSession

# Function: requireStudentViewSession()

> **requireStudentViewSession**(`__namedParameters?`): `Promise`\<[`StudentViewSession`](../type-aliases/StudentViewSession.md)\>

Defined in: [ui/src/api-server/student-view.ts:68](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-server/student-view.ts#L68)

Gates the student-view endpoint. Unlike every other API route this one is
reachable by a Hanich session — it is the single endpoint that is. Anything
below Hanich (i.e. no session at all) is rejected: every student reaches
Bluz through a Hive sign-in, so there is no anonymous viewer to serve.

## Parameters

### \_\_namedParameters?

#### allowChecker?

`boolean` = `false`

## Returns

`Promise`\<[`StudentViewSession`](../type-aliases/StudentViewSession.md)\>
