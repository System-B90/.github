[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-shared/types/gantt/create-payloads](../index.md) / CreateConstraintPayload

# Type Alias: CreateConstraintPayload

> **CreateConstraintPayload** = [`RelationalConstraint`](../../models/constraint/type-aliases/RelationalConstraint.md) \| [`TemporalConstraint`](../../models/constraint/type-aliases/TemporalConstraint.md)

Defined in: [ui/src/api-shared/types/gantt/create-payloads.ts:25](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/gantt/create-payloads.ts#L25)

Payload to create a new Gantt constraint: a relational or temporal
constraint. Neither `RelationalConstraint` nor `TemporalConstraint`
carries `createdAt`/`updatedAt` — those exist only on the DB row shape,
not this client-side model — so there is nothing to omit here.
