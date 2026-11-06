[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/db-base](../index.md) / DrizzleOperationsBuilderProps

# Type Alias: DrizzleOperationsBuilderProps\<TTable\>

> **DrizzleOperationsBuilderProps**\<`TTable`\> = `object`

Defined in: [ui/src/api-server/gantt/db-base.ts:226](https://github.com/System-B90/Bluz/blob/90114c31e10132d84c8c3bab079c25588fbe0459/ui/src/api-server/gantt/db-base.ts#L226)

## Type Parameters

### TTable

`TTable` *extends* `PgTableWithColumns`\<`any`\>

## Properties

### idPrefix

> **idPrefix**: `"c"` \| `"d"` \| `"e"` \| `"m"` \| `"s"` \| `"w"`

Defined in: [ui/src/api-server/gantt/db-base.ts:233](https://github.com/System-B90/Bluz/blob/90114c31e10132d84c8c3bab079c25588fbe0459/ui/src/api-server/gantt/db-base.ts#L233)

***

### junction?

> `optional` **junction?**: [`JunctionConfig`](JunctionConfig.md)[] \| [`JunctionConfig`](JunctionConfig.md)

Defined in: [ui/src/api-server/gantt/db-base.ts:231](https://github.com/System-B90/Bluz/blob/90114c31e10132d84c8c3bab079c25588fbe0459/ui/src/api-server/gantt/db-base.ts#L231)

***

### labelColumn?

> `optional` **labelColumn?**: `AnyPgColumn`

Defined in: [ui/src/api-server/gantt/db-base.ts:236](https://github.com/System-B90/Bluz/blob/90114c31e10132d84c8c3bab079c25588fbe0459/ui/src/api-server/gantt/db-base.ts#L236)

***

### parentJunction?

> `optional` **parentJunction?**: [`ParentJunctionConfig`](ParentJunctionConfig.md)

Defined in: [ui/src/api-server/gantt/db-base.ts:232](https://github.com/System-B90/Bluz/blob/90114c31e10132d84c8c3bab079c25588fbe0459/ui/src/api-server/gantt/db-base.ts#L232)

***

### table

> **table**: `TTable`

Defined in: [ui/src/api-server/gantt/db-base.ts:229](https://github.com/System-B90/Bluz/blob/90114c31e10132d84c8c3bab079c25588fbe0459/ui/src/api-server/gantt/db-base.ts#L229)

***

### typeName

> **typeName**: `string`

Defined in: [ui/src/api-server/gantt/db-base.ts:230](https://github.com/System-B90/Bluz/blob/90114c31e10132d84c8c3bab079c25588fbe0459/ui/src/api-server/gantt/db-base.ts#L230)
