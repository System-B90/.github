[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/import-tree](../index.md) / junctionSortOrder

# Function: junctionSortOrder()

> **junctionSortOrder**(`link`): `number`

Defined in: [ui/src/api-server/gantt/import-tree.ts:40](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-server/gantt/import-tree.ts#L40)

Junction rows come back from the export with their `sortOrder`, but the
shared `Api*` junction shapes do not declare it; read it defensively.

## Parameters

### link

`unknown`

## Returns

`number`
