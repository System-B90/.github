[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-client/gantt/constraints](../index.md) / ganttConstraintsApi

# Variable: ganttConstraintsApi

> `const` **ganttConstraintsApi**: `object`

Defined in: [ui/src/api-client/gantt/constraints.ts:198](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-client/gantt/constraints.ts#L198)

Client-side API client wrapper for managing Gantt constraints.
Provides endpoints for retrieving, creating, updating, and deleting constraints.

## Type Declaration

### apiCreate

> `readonly` **apiCreate**: (`curriculumId`, `payload`, `options?`) => `Promise`\<[`GanttConstraint`](../../../../api-shared/types/gantt/models/constraint/type-aliases/GanttConstraint.md)\> = `apiCreateConstraint`

POST: Creates a new relational or temporal constraint.
Note: Assumes the endpoint is nested under the curriculum for uniform routing.

#### Parameters

##### curriculumId

`string`

##### payload

[`CreateConstraintPayload`](../../../../api-shared/types/gantt/create-payloads/type-aliases/CreateConstraintPayload.md)

##### options?

[`ClientApiProps`](../../../common/type-aliases/ClientApiProps.md)

#### Returns

`Promise`\<[`GanttConstraint`](../../../../api-shared/types/gantt/models/constraint/type-aliases/GanttConstraint.md)\>

### apiDelete

> `readonly` **apiDelete**: (`curriculumId`, `id`, `options?`) => `Promise`\<`void`\> = `apiDeleteConstraint`

DELETE: Removes a constraint.

#### Parameters

##### curriculumId

`string`

##### id

`string`

##### options?

[`ClientApiProps`](../../../common/type-aliases/ClientApiProps.md)

#### Returns

`Promise`\<`void`\>

### apiGet

> `readonly` **apiGet**: (`curriculumId`, `__namedParameters`, `options?`) => `Promise`\<[`GanttConstraint`](../../../../api-shared/types/gantt/models/constraint/type-aliases/GanttConstraint.md)[]\> = `apiGetConstraints`

GET: Retrieves all constraints for a curriculum's modules and events.

#### Parameters

##### curriculumId

`string`

##### \_\_namedParameters

###### moduleId?

`string`

###### syllabusId?

`string`

##### options?

[`ClientApiProps`](../../../common/type-aliases/ClientApiProps.md)

#### Returns

`Promise`\<[`GanttConstraint`](../../../../api-shared/types/gantt/models/constraint/type-aliases/GanttConstraint.md)[]\>

### apiUpdate

> `readonly` **apiUpdate**: (`curriculumId`, `id`, `payload`, `options?`) => `Promise`\<[`GanttConstraint`](../../../../api-shared/types/gantt/models/constraint/type-aliases/GanttConstraint.md)\> = `apiUpdateConstraint`

PATCH: Updates an existing constraint.

#### Parameters

##### curriculumId

`string`

##### id

`string`

##### payload

`Partial`\<[`CreateConstraintPayload`](../../../../api-shared/types/gantt/create-payloads/type-aliases/CreateConstraintPayload.md)\>

##### options?

[`ClientApiProps`](../../../common/type-aliases/ClientApiProps.md)

#### Returns

`Promise`\<[`GanttConstraint`](../../../../api-shared/types/gantt/models/constraint/type-aliases/GanttConstraint.md)\>
