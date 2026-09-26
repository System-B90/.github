[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/gantt/state/context](../index.md) / useCurriculumProviderActions

# Function: useCurriculumProviderActions()

> **useCurriculumProviderActions**(): `object`

Defined in: [ui/src/components/gantt/state/context.ts:89](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/gantt/state/context.ts#L89)

Handles low level UI & state actions on the cached curriculum.
**FOR INTERNAL USE ONLY**

## Returns

`object`

Destructable object with actions on the global curriculum provider.

### closeEventDialog

> **closeEventDialog**: [`CloseEventDialog`](../type-aliases/CloseEventDialog.md)

### closeModuleDialog

> **closeModuleDialog**: [`CloseModuleDialog`](../type-aliases/CloseModuleDialog.md)

### closeSyllabusDialog

> **closeSyllabusDialog**: [`CloseSyllabusDialog`](../type-aliases/CloseSyllabusDialog.md)

### dispatch

> **dispatch**: `Dispatch`\<[`Action`](../../reducers/actions/type-aliases/Action.md)\>

### openEventDialog

> **openEventDialog**: [`OpenEventDialog`](../type-aliases/OpenEventDialog.md)

### openModuleDialog

> **openModuleDialog**: [`OpenModuleDialog`](../type-aliases/OpenModuleDialog.md)

### openSyllabusDialog

> **openSyllabusDialog**: [`OpenSyllabusDialog`](../type-aliases/OpenSyllabusDialog.md)

### registerRevealHandler

> **registerRevealHandler**: (`handler`) => () => `void`

#### Parameters

##### handler

[`RevealGanttItem`](../type-aliases/RevealGanttItem.md)

#### Returns

() => `void`

### requestReveal

> **requestReveal**: [`RevealGanttItem`](../type-aliases/RevealGanttItem.md)
