[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/cut-rules](../index.md) / OVERFLOW\_RULES

# Variable: OVERFLOW\_RULES

> `const` **OVERFLOW\_RULES**: `object`

Defined in: [ui/src/api-shared/gantt/cut-rules.ts:130](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/api-shared/gantt/cut-rules.ts#L130)

What happens when a week is over capacity even after the balancer has packed
every day in it — the load simply does not fit into the week's working hours.

The cut never silently invents time. It surfaces the week as a decision
(`week-overflow`) and lets the user choose; [defaultResolution](#defaultresolution) is
what the dialog pre-selects and what a non-interactive caller gets.

## Type Declaration

### defaultResolution

> `readonly` **defaultResolution**: `"park"`

`park` — what does not fit its day goes to the schedule's unassigned
box (ארגז), to be placed by hand. Nothing overlaps and nothing runs
past working hours. `overlap-source` (leftovers stay on their day and
overlap what is there) was the default before.

### resolutions

> `readonly` **resolutions**: readonly \[`"park"`, `"overlap-source"`, `"overlap-least-full"`, `"extend-day"`, `"drop"`\]

Every resolution the dialog may offer for an overflowing week.
