[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/db-constraints](../index.md) / getConstraintsForModule

# Function: getConstraintsForModule()

> **getConstraintsForModule**(`moduleId`): `Promise`\<`object`[]\>

Defined in: [ui/src/api-server/gantt/db-constraints.ts:306](https://github.com/System-B90/Bluz/blob/901cc8f4c754d82c12fc600337c5991c07a64502/ui/src/api-server/gantt/db-constraints.ts#L306)

Retrieves all constraints owned by a specific module or its nested events.

## Parameters

### moduleId

`string`

The unique identifier of the module.

## Returns

`Promise`\<`object`[]\>

An array of constraints found.
