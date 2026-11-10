[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/schedule/event-component/use-event-duration](../index.md) / useEventDuration

# Function: useEventDuration()

> **useEventDuration**(`event`): `object`

Defined in: [ui/src/components/schedule/event-component/use-event-duration.ts:30](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/components/schedule/event-component/use-event-duration.ts#L30)

Start/end moments of an event plus its length split into whole hours and
remaining minutes. Callers format the parts to taste.

## Parameters

### event

[`Event`](../../../../../api-shared/types/event/type-aliases/Event.md)

## Returns

`object`

### durationMinutes

> **durationMinutes**: `number`

### end

> **end**: `Moment`

### hours

> **hours**: `number`

### minutes

> **minutes**: `number`

### start

> **start**: `Moment`

### timeRange

> **timeRange**: `string`
