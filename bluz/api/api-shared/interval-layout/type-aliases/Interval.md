[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/interval-layout](../index.md) / Interval

# Type Alias: Interval

> **Interval** = `object`

Defined in: [ui/src/api-shared/interval-layout.ts:9](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-shared/interval-layout.ts#L9)

Pure interval arithmetic for laying a continuous run of work around windows
it must not occupy ("jumping over" them). Deliberately domain-free —
everything is epoch milliseconds — so the same math backs the calendar
renderer, the drag preview and the gantt cut planner without any of them
re-deriving it.

## Properties

### end

> **end**: `number`

Defined in: [ui/src/api-shared/interval-layout.ts:9](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-shared/interval-layout.ts#L9)

***

### start

> **start**: `number`

Defined in: [ui/src/api-shared/interval-layout.ts:9](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-shared/interval-layout.ts#L9)
