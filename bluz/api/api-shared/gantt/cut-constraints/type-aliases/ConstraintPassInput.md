[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/cut-constraints](../index.md) / ConstraintPassInput

# Type Alias: ConstraintPassInput

> **ConstraintPassInput** = `object`

Defined in: [ui/src/api-shared/gantt/cut-constraints.ts:80](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/cut-constraints.ts#L80)

## Properties

### days

> **days**: `Record`\<`string`, [`ConstraintDayInfo`](ConstraintDayInfo.md)\>

Defined in: [ui/src/api-shared/gantt/cut-constraints.ts:82](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/cut-constraints.ts#L82)

***

### entities

> **entities**: [`ConstraintEntity`](ConstraintEntity.md)[]

Defined in: [ui/src/api-shared/gantt/cut-constraints.ts:84](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/cut-constraints.ts#L84)

Constraints owned by events and modules, indexed by owner id.

***

### eventIdsByModule

> **eventIdsByModule**: `Record`\<`string`, `string`[]\>

Defined in: [ui/src/api-shared/gantt/cut-constraints.ts:86](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/cut-constraints.ts#L86)

Module id → the event ids it contains, for module-level constraints.

***

### placements

> **placements**: [`ConstraintPlacement`](ConstraintPlacement.md)[]

Defined in: [ui/src/api-shared/gantt/cut-constraints.ts:81](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/cut-constraints.ts#L81)

***

### titleByEventId

> **titleByEventId**: `Record`\<`string`, `string`\>

Defined in: [ui/src/api-shared/gantt/cut-constraints.ts:88](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/cut-constraints.ts#L88)

Display titles for events, used in violation messages.
