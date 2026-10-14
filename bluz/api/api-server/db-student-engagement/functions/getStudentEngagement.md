[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/db-student-engagement](../index.md) / getStudentEngagement

# Function: getStudentEngagement()

> **getStudentEngagement**(`userId`, `date`): `Promise`\<[`StudentEngagementDocument`](../../mongo-db-controller/type-aliases/StudentEngagementDocument.md) \| `null`\>

Defined in: [ui/src/api-server/db-student-engagement.ts:66](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/api-server/db-student-engagement.ts#L66)

Reads one student's counter for a day. Staff-only callers.

## Parameters

### userId

`string`

### date

`string`

## Returns

`Promise`\<[`StudentEngagementDocument`](../../mongo-db-controller/type-aliases/StudentEngagementDocument.md) \| `null`\>
