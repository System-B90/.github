[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/unavailability](../index.md) / newUnavailabilityClashes

# Function: newUnavailabilityClashes()

> **newUnavailabilityClashes**(`saved`, `events`): [`UnavailabilityClash`](../type-aliases/UnavailabilityClash.md)[]

Defined in: [ui/src/api-shared/unavailability.ts:151](https://github.com/System-B90/Bluz/blob/d77dcf130db661461363a52910f62a34b3514ebd/ui/src/api-shared/unavailability.ts#L151)

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
