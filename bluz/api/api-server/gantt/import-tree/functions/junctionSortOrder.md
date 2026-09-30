[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/import-tree](../index.md) / junctionSortOrder

# Function: junctionSortOrder()

> **junctionSortOrder**(`link`): `number`

Defined in: [ui/src/api-server/gantt/import-tree.ts:41](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-server/gantt/import-tree.ts#L41)

Junction rows come back from the export with their `sortOrder`, but the
shared `Api*` junction shapes do not declare it; read it defensively.

## Parameters

### link

`unknown`

## Returns

`number`
