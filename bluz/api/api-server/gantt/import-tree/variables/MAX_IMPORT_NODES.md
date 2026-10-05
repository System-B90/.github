[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/import-tree](../index.md) / MAX\_IMPORT\_NODES

# Variable: MAX\_IMPORT\_NODES

> `const` **MAX\_IMPORT\_NODES**: `50000` = `50_000`

Defined in: [ui/src/api-server/gantt/import-tree.ts:34](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-server/gantt/import-tree.ts#L34)

Upper bound on the total number of entities a single import may create.
Guards the recursive walk against a hostile/corrupt payload that would
otherwise fan out into an unbounded number of inserts (#162).
