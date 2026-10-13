[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/db-constraints](../index.md) / getConstraintsForModule

# Function: getConstraintsForModule()

> **getConstraintsForModule**(`moduleId`): `Promise`\<`object`[]\>

Defined in: [ui/src/api-server/gantt/db-constraints.ts:271](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-server/gantt/db-constraints.ts#L271)

Retrieves all constraints owned by a specific module or its nested events.

## Parameters

### moduleId

`string`

The unique identifier of the module.

## Returns

`Promise`\<`object`[]\>

An array of constraints found.
