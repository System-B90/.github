[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/import-tree](../index.md) / junctionSortOrder

# Function: junctionSortOrder()

> **junctionSortOrder**(`link`): `number`

Defined in: [ui/src/api-server/gantt/import-tree.ts:40](https://github.com/System-B90/Bluz/blob/182d51c797407c7b0ea37986b1a45ab0e64c4df0/ui/src/api-server/gantt/import-tree.ts#L40)

Junction rows come back from the export with their `sortOrder`, but the
shared `Api*` junction shapes do not declare it; read it defensively.

## Parameters

### link

`unknown`

## Returns

`number`
