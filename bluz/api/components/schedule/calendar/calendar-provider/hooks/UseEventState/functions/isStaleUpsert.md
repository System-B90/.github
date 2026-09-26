[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [components/schedule/calendar/calendar-provider/hooks/UseEventState](../index.md) / isStaleUpsert

# Function: isStaleUpsert()

> **isStaleUpsert**(`existing`, `incoming`): `boolean`

Defined in: [ui/src/components/schedule/calendar/calendar-provider/hooks/UseEventState.ts:30](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/schedule/calendar/calendar-provider/hooks/UseEventState.ts#L30)

Optimistic-concurrency guard (#156). Returns true when `incoming` must NOT
replace `existing` because it is not strictly newer. When both carry a
client `updatedAt` revision, only a strictly-greater revision wins; equal or
older revisions (a self-echo of our own save, or a stale WS broadcast that
raced a newer local edit) are dropped. Missing revisions on either side fall
back to always-overwrite for backward compatibility with legacy events.

## Parameters

### existing

[`Event`](../../../../../../../api-shared/types/event/type-aliases/Event.md)

### incoming

[`Event`](../../../../../../../api-shared/types/event/type-aliases/Event.md)

## Returns

`boolean`
