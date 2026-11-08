[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/db-constraints](../index.md) / getConstraintsForModule

# Function: getConstraintsForModule()

> **getConstraintsForModule**(`moduleId`): `Promise`\<`object`[]\>

Defined in: [ui/src/api-server/gantt/db-constraints.ts:306](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/api-server/gantt/db-constraints.ts#L306)

Retrieves all constraints owned by a specific module or its nested events.

## Parameters

### moduleId

`string`

The unique identifier of the module.

## Returns

`Promise`\<`object`[]\>

An array of constraints found.
