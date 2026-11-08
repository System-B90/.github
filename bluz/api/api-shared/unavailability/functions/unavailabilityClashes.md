[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/unavailability](../index.md) / unavailabilityClashes

# Function: unavailabilityClashes()

> **unavailabilityClashes**(`event`, `others`): [`UnavailabilityClash`](../type-aliases/UnavailabilityClash.md)[]

Defined in: [ui/src/api-shared/unavailability.ts:110](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-shared/unavailability.ts#L110)

Every clash `event` takes part in against `others`: as an assignment, a
person on it marked unavailable over it; as an unavailability, an event its
person is booked in meanwhile. Parked events are off the grid and clash
with nothing.

## Parameters

### event

[`Event`](../../types/event/type-aliases/Event.md)

### others

readonly [`Event`](../../types/event/type-aliases/Event.md)[]

## Returns

[`UnavailabilityClash`](../type-aliases/UnavailabilityClash.md)[]
