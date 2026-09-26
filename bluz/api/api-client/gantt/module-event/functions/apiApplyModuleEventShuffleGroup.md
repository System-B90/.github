[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-client/gantt/module-event](../index.md) / apiApplyModuleEventShuffleGroup

# Function: apiApplyModuleEventShuffleGroup()

> **apiApplyModuleEventShuffleGroup**(`eventId`, `moduleId`, `shuffles`): `Promise`\<\{ `members`: [`ModuleEventDocument`](../type-aliases/ModuleEventDocument.md)[]; `removedIds`: `string`[]; \}\>

Defined in: [ui/src/api-client/gantt/module-event.ts:40](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-client/gantt/module-event.ts#L40)

Reconciles the event's shuffle group so it covers exactly `shuffles`, one
sibling event per name (#699). Returns the surviving members and the ids of
members dropped because their shuffle is no longer part of the group.

## Parameters

### eventId

`string`

### moduleId

`string`

### shuffles

`string`[]

## Returns

`Promise`\<\{ `members`: [`ModuleEventDocument`](../type-aliases/ModuleEventDocument.md)[]; `removedIds`: `string`[]; \}\>
