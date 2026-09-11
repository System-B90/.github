[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/db-constraints](../index.md) / getConstraintsForModule

# Function: getConstraintsForModule()

> **getConstraintsForModule**(`moduleId`): `Promise`\<`object`[]\>

Defined in: [ui/src/api-server/gantt/db-constraints.ts:222](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/gantt/db-constraints.ts#L222)

Retrieves all constraints owned by a specific module or its nested events.

## Parameters

### moduleId

`string`

The unique identifier of the module.

## Returns

`Promise`\<`object`[]\>

An array of constraints found.
