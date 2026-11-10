[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/unavailability](../index.md) / newUnavailabilityClashes

# Function: newUnavailabilityClashes()

> **newUnavailabilityClashes**(`saved`, `events`): [`UnavailabilityClash`](../type-aliases/UnavailabilityClash.md)[]

Defined in: [ui/src/api-shared/unavailability.ts:151](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-shared/unavailability.ts#L151)

Clashes a save creates: those of each saved event against the events in
state, minus the ones its previous version already had. Re-saving an event
that already clashed (a rename, say) stays quiet; assigning a person, or
moving the event, into their unavailability does not.

## Parameters

### saved

readonly [`Event`](../../types/event/type-aliases/Event.md)[]

The events as written.

### events

readonly [`Event`](../../types/event/type-aliases/Event.md)[]

The events in state before the write.

## Returns

[`UnavailabilityClash`](../type-aliases/UnavailabilityClash.md)[]
