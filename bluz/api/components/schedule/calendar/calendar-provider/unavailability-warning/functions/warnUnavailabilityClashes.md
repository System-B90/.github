[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/calendar-provider/unavailability-warning](../index.md) / warnUnavailabilityClashes

# Function: warnUnavailabilityClashes()

> **warnUnavailabilityClashes**(`saved`, `events`, `personName`): `void`

Defined in: [ui/src/components/schedule/calendar/calendar-provider/unavailability-warning.ts:16](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/components/schedule/calendar/calendar-provider/unavailability-warning.ts#L16)

Warns, one snackbar per person, when a save books someone in parallel to
their own unavailability (אי זמינות) — or marks someone unavailable over
what they are already booked in. Like the instructor double-booking
warning, it flags and never blocks. Clashes the saved events already had
stay quiet.

## Parameters

### saved

readonly [`Event`](../../../../../../api-shared/types/event/type-aliases/Event.md)[]

The events as written.

### events

readonly [`Event`](../../../../../../api-shared/types/event/type-aliases/Event.md)[]

The events in state before the write.

### personName

(`id`) => `string` \| `undefined`

Display name of a staff member, by Hive id.

## Returns

`void`
