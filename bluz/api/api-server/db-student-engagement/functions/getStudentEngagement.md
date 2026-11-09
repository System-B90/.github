[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/db-student-engagement](../index.md) / getStudentEngagement

# Function: getStudentEngagement()

> **getStudentEngagement**(`userId`, `date`): `Promise`\<[`StudentEngagementDocument`](../../mongo-db-controller/type-aliases/StudentEngagementDocument.md) \| `null`\>

Defined in: [ui/src/api-server/db-student-engagement.ts:73](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-server/db-student-engagement.ts#L73)

Reads one student's counter for a day. Staff-only callers.

## Parameters

### userId

`string`

### date

`string`

## Returns

`Promise`\<[`StudentEngagementDocument`](../../mongo-db-controller/type-aliases/StudentEngagementDocument.md) \| `null`\>
