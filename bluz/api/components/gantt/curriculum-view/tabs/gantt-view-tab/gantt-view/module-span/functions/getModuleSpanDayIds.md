[**TypeDoc API**](../../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../../index.md) / [components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/module-span](../index.md) / getModuleSpanDayIds

# Function: getModuleSpanDayIds()

> **getModuleSpanDayIds**(`__namedParameters`): `Set`\<`string`\>

Defined in: [ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/module-span.ts:25](https://github.com/System-B90/Bluz/blob/04ebae9cb334a01c6e7a55f885993f021e83cd92/ui/src/components/gantt/curriculum-view/tabs/gantt-view-tab/gantt-view/module-span.ts#L25)

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
