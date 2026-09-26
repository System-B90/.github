[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/allocate-time](../index.md) / planModuleAllocation

# Function: planModuleAllocation()

> **planModuleAllocation**(`__namedParameters`): [`ModuleAllocation`](../type-aliases/ModuleAllocation.md)[]

Defined in: [ui/src/api-shared/gantt/allocate-time.ts:44](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/allocate-time.ts#L44)

Pure, synchronous split of `totalDuration` across the module's events in
order, each taking up to its `minimumDuration`. The client reducer consumes
this directly: the async `allocateTimeToModule` wrapper only runs its first
iteration synchronously, so a reducer calling it returned before the
remaining events were updated.

## Parameters

### \_\_namedParameters

`Pick`\<[`AllocateTimeToModuleProps`](../type-aliases/AllocateTimeToModuleProps.md)\<[`AllocateTimeToEventCallback`](../type-aliases/AllocateTimeToEventCallback.md)\>, `"module"` \| `"moduleEvents"` \| `"totalDuration"`\>

## Returns

[`ModuleAllocation`](../type-aliases/ModuleAllocation.md)[]
