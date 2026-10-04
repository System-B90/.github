[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/db-student-engagement](../index.md) / getStudentEngagement

# Function: getStudentEngagement()

> **getStudentEngagement**(`userId`, `date`): `Promise`\<[`StudentEngagementDocument`](../../mongo-db-controller/type-aliases/StudentEngagementDocument.md) \| `null`\>

Defined in: [ui/src/api-server/db-student-engagement.ts:66](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/api-server/db-student-engagement.ts#L66)

Reads one student's counter for a day. Staff-only callers.

## Parameters

### userId

`string`

### date

`string`

## Returns

`Promise`\<[`StudentEngagementDocument`](../../mongo-db-controller/type-aliases/StudentEngagementDocument.md) \| `null`\>
