[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/ai/tools/common](../index.md) / changedFieldsImpact

# Function: changedFieldsImpact()

> **changedFieldsImpact**(`args`, `labels`): `string`[]

Defined in: [ui/src/api-server/ai/tools/common.ts:129](https://github.com/System-B90/Bluz/blob/d77dcf130db661461363a52910f62a34b3514ebd/ui/src/api-server/ai/tools/common.ts#L129)

Names the fields a partial update will write, in Hebrew. A human approving
"עדכון X" has no way to tell a rename from a reschedule otherwise.

## Parameters

### args

`Record`\<`string`, `unknown`\>

### labels

`Record`\<`string`, `string`\>

## Returns

`string`[]
