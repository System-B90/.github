[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/student-view/use-foreground-timer](../index.md) / useForegroundTimer

# Function: useForegroundTimer()

> **useForegroundTimer**(): `void`

Defined in: [ui/src/components/student-view/use-foreground-timer.ts:50](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/student-view/use-foreground-timer.ts#L50)

Counts the time this page spends open and in the foreground, flushing it to
the server on a heartbeat and whenever the page stops being foreground
(#656).

Time is measured as wall-clock deltas between foreground transitions rather
than by counting ticks, so a throttled background timer cannot under- or
over-count: a hidden tab's interval simply has nothing to add.

## Returns

`void`
