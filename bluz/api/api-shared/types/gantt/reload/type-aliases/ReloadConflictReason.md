[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-shared/types/gantt/reload](../index.md) / ReloadConflictReason

# Type Alias: ReloadConflictReason

> **ReloadConflictReason** = `object`

Defined in: [ui/src/api-shared/types/gantt/reload.ts:45](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/gantt/reload.ts#L45)

Why a change was withheld: the event carries a manual edit.

## Properties

### actorName

> **actorName**: `null` \| `string`

Defined in: [ui/src/api-shared/types/gantt/reload.ts:48](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/gantt/reload.ts#L48)

***

### changedAt

> **changedAt**: `string`

Defined in: [ui/src/api-shared/types/gantt/reload.ts:50](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/gantt/reload.ts#L50)

ISO datetime of the last manual change.

***

### initiator

> **initiator**: `string`

Defined in: [ui/src/api-shared/types/gantt/reload.ts:47](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/gantt/reload.ts#L47)

Initiator of the last manual change.
