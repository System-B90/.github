[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-client/gantt/module-event](../index.md) / apiApplyModuleEventShuffleGroup

# Function: apiApplyModuleEventShuffleGroup()

> **apiApplyModuleEventShuffleGroup**(`eventId`, `moduleId`, `shuffles`): `Promise`\<\{ `members`: [`ModuleEventDocument`](../type-aliases/ModuleEventDocument.md)[]; `removedIds`: `string`[]; \}\>

Defined in: [ui/src/api-client/gantt/module-event.ts:41](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/api-client/gantt/module-event.ts#L41)

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
