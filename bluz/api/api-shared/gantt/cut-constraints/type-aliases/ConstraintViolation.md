[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/cut-constraints](../index.md) / ConstraintViolation

# Type Alias: ConstraintViolation

> **ConstraintViolation** = `object`

Defined in: [ui/src/api-shared/gantt/cut-constraints.ts:71](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/gantt/cut-constraints.ts#L71)

A constraint that no legal placement can satisfy.

## Properties

### constraintId

> **constraintId**: `string`

Defined in: [ui/src/api-shared/gantt/cut-constraints.ts:76](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/gantt/cut-constraints.ts#L76)

***

### eventId

> **eventId**: `string`

Defined in: [ui/src/api-shared/gantt/cut-constraints.ts:75](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/gantt/cut-constraints.ts#L75)

The event whose placement breaks the constraint.

***

### kind

> **kind**: `"relational"` \| `"temporal"`

Defined in: [ui/src/api-shared/gantt/cut-constraints.ts:77](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/gantt/cut-constraints.ts#L77)

***

### ownerId

> **ownerId**: `string`

Defined in: [ui/src/api-shared/gantt/cut-constraints.ts:72](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/gantt/cut-constraints.ts#L72)

***

### ownerTitle

> **ownerTitle**: `string`

Defined in: [ui/src/api-shared/gantt/cut-constraints.ts:73](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/gantt/cut-constraints.ts#L73)

***

### reason

> **reason**: `string`

Defined in: [ui/src/api-shared/gantt/cut-constraints.ts:79](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-shared/gantt/cut-constraints.ts#L79)

Hebrew explanation of what could not be satisfied.
