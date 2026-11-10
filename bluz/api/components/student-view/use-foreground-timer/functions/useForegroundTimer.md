[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/student-view/use-foreground-timer](../index.md) / useForegroundTimer

# Function: useForegroundTimer()

> **useForegroundTimer**(): `void`

Defined in: [ui/src/components/student-view/use-foreground-timer.ts:56](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/components/student-view/use-foreground-timer.ts#L56)

Counts the time this page spends open and in the foreground, flushing it to
the server on a heartbeat and whenever the page stops being foreground
(#656).

Time is measured as deltas between foreground transitions rather than by
counting ticks, so a throttled background timer cannot under- or over-count:
a hidden tab's interval simply has nothing to add. The deltas come from the
monotonic clock, never the device's wall clock — winding that forward while
focused must not bank hours.

## Returns

`void`
