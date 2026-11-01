[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/ai/tools/common](../index.md) / changedFieldsImpact

# Function: changedFieldsImpact()

> **changedFieldsImpact**(`args`, `labels`): `string`[]

Defined in: [ui/src/api-server/ai/tools/common.ts:129](https://github.com/System-B90/Bluz/blob/2fa23325da73d58527b069b0943f3bd1e838efee/ui/src/api-server/ai/tools/common.ts#L129)

Names the fields a partial update will write, in Hebrew. A human approving
"עדכון X" has no way to tell a rename from a reschedule otherwise.

## Parameters

### args

`Record`\<`string`, `unknown`\>

### labels

`Record`\<`string`, `string`\>

## Returns

`string`[]
