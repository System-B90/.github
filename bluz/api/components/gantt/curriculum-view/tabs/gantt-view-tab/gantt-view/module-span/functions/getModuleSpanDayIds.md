[**TypeDoc API**](../../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../../index.md) / [components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/module-span](../index.md) / getModuleSpanDayIds

# Function: getModuleSpanDayIds()

> **getModuleSpanDayIds**(`__namedParameters`): `Set`\<`string`\>

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/module-span.ts:24](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/module-span.ts#L24)

Every day a module's block may cover. A module with events spans only the
days its allocated events actually occupy — start day, week-split parts and
surviving recurrence occurrences — so the block runs first event → last
event and never covers time holding none of them. Stale module-level
mappings are ignored then; they only place an event-less module.

## Parameters

### \_\_namedParameters

`ModuleSpanInput`

## Returns

`Set`\<`string`\>
