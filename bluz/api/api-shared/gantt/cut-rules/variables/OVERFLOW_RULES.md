[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/cut-rules](../index.md) / OVERFLOW\_RULES

# Variable: OVERFLOW\_RULES

> `const` **OVERFLOW\_RULES**: `object`

Defined in: [ui/src/api-shared/gantt/cut-rules.ts:130](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/cut-rules.ts#L130)

What happens when a week is over capacity even after the balancer has packed
every day in it — the load simply does not fit into the week's working hours.

The cut never silently invents time. It surfaces the week as a decision
(`week-overflow`) and lets the user choose; [defaultResolution](#defaultresolution) is
what the dialog pre-selects and what a non-interactive caller gets.

## Type Declaration

### defaultResolution

> `readonly` **defaultResolution**: `"overlap-source"`

`overlap-source` — leftovers stay on the day they were mapped to and
overlap the events already there. Honours "always prefer overlapping
events rather than placing events outside working hours".

### resolutions

> `readonly` **resolutions**: readonly \[`"overlap-source"`, `"overlap-least-full"`, `"extend-day"`, `"drop"`\]

Every resolution the dialog may offer for an overflowing week.
