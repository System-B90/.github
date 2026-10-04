[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/ai/tools/common](../index.md) / changedFieldsImpact

# Function: changedFieldsImpact()

> **changedFieldsImpact**(`args`, `labels`): `string`[]

Defined in: [ui/src/api-server/ai/tools/common.ts:116](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/api-server/ai/tools/common.ts#L116)

Names the fields a partial update will write, in Hebrew. A human approving
"עדכון X" has no way to tell a rename from a reschedule otherwise.

## Parameters

### args

`Record`\<`string`, `unknown`\>

### labels

`Record`\<`string`, `string`\>

## Returns

`string`[]
