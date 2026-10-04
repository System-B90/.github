[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/ai/tools/common](../index.md) / changedFieldsImpact

# Function: changedFieldsImpact()

> **changedFieldsImpact**(`args`, `labels`): `string`[]

Defined in: [ui/src/api-server/ai/tools/common.ts:116](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/api-server/ai/tools/common.ts#L116)

Names the fields a partial update will write, in Hebrew. A human approving
"עדכון X" has no way to tell a rename from a reschedule otherwise.

## Parameters

### args

`Record`\<`string`, `unknown`\>

### labels

`Record`\<`string`, `string`\>

## Returns

`string`[]
