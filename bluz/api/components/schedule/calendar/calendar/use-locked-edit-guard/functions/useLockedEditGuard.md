[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/calendar/use-locked-edit-guard](../index.md) / useLockedEditGuard

# Function: useLockedEditGuard()

> **useLockedEditGuard**(`eventLocks`, `confirm`): `object`

Defined in: [ui/src/components/schedule/calendar/calendar/use-locked-edit-guard.ts:25](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/components/schedule/calendar/calendar/use-locked-edit-guard.ts#L25)

Quick edits (drag, split, right-click menu) skip the event dialog and its
"being edited by" banner, so they ask loudly before touching an event
someone else has open (#775).

## Parameters

### eventLocks

`Record`\<[`EventId`](../../../../../../api-shared/types/event/type-aliases/EventId.md), [`EventLockMessage`](../../../../../../api-shared/types/type-aliases/EventLockMessage.md) \| `undefined`\>

Live locks held by other users.

### confirm

`Confirm`

The calendar's confirm dialog.

## Returns

### confirmLockedEdit

> **confirmLockedEdit**: (`eventIds`) => `Promise`\<`boolean`\>

Resolves true at once when none of the events is locked.

#### Parameters

##### eventIds

`string`[]

#### Returns

`Promise`\<`boolean`\>

### withLockGuard

> **withLockGuard**: \<`Args`\>(`run`, `idsOf`) => (...`args`) => `void`

Wraps a quick-edit handler so it runs only after the lock check.

#### Type Parameters

##### Args

`Args` *extends* `unknown`[]

#### Parameters

##### run

(...`args`) => `void`

The handler to guard.

##### idsOf

(...`args`) => `string`[] \| `null`

The events a call touches; null skips the check.

#### Returns

(...`args`) => `void`
