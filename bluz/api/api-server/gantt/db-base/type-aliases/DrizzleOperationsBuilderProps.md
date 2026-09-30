[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/db-base](../index.md) / DrizzleOperationsBuilderProps

# Type Alias: DrizzleOperationsBuilderProps\<TTable\>

> **DrizzleOperationsBuilderProps**\<`TTable`\> = `object`

Defined in: [ui/src/api-server/gantt/db-base.ts:220](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-server/gantt/db-base.ts#L220)

## Type Parameters

### TTable

`TTable` *extends* `PgTableWithColumns`\<`any`\>

## Properties

### idPrefix

> **idPrefix**: `"c"` \| `"d"` \| `"e"` \| `"m"` \| `"s"` \| `"w"`

Defined in: [ui/src/api-server/gantt/db-base.ts:227](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-server/gantt/db-base.ts#L227)

***

### junction?

> `optional` **junction?**: [`JunctionConfig`](JunctionConfig.md)[] \| [`JunctionConfig`](JunctionConfig.md)

Defined in: [ui/src/api-server/gantt/db-base.ts:225](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-server/gantt/db-base.ts#L225)

***

### labelColumn?

> `optional` **labelColumn?**: `AnyPgColumn`

Defined in: [ui/src/api-server/gantt/db-base.ts:230](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-server/gantt/db-base.ts#L230)

***

### parentJunction?

> `optional` **parentJunction?**: [`ParentJunctionConfig`](ParentJunctionConfig.md)

Defined in: [ui/src/api-server/gantt/db-base.ts:226](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-server/gantt/db-base.ts#L226)

***

### table

> **table**: `TTable`

Defined in: [ui/src/api-server/gantt/db-base.ts:223](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-server/gantt/db-base.ts#L223)

***

### typeName

> **typeName**: `string`

Defined in: [ui/src/api-server/gantt/db-base.ts:224](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-server/gantt/db-base.ts#L224)
