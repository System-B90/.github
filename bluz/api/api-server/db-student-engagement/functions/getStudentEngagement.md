[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/db-student-engagement](../index.md) / getStudentEngagement

# Function: getStudentEngagement()

> **getStudentEngagement**(`userId`, `date`): `Promise`\<[`StudentEngagementDocument`](../../mongo-db-controller/type-aliases/StudentEngagementDocument.md) \| `null`\>

Defined in: [ui/src/api-server/db-student-engagement.ts:73](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-server/db-student-engagement.ts#L73)

Reads one student's counter for a day. Staff-only callers.

## Parameters

### userId

`string`

### date

`string`

## Returns

`Promise`\<[`StudentEngagementDocument`](../../mongo-db-controller/type-aliases/StudentEngagementDocument.md) \| `null`\>
