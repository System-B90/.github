[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/gantt/curriculum-fab/action-items/CreateCurriculumHoverMenu](../index.md) / CreateCurriculumHoverMenuProps

# Type Alias: CreateCurriculumHoverMenuProps

> **CreateCurriculumHoverMenuProps** = `object`

Defined in: [ui/src/components/gantt/curriculum-fab/action-items/CreateCurriculumHoverMenu.tsx:9](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/gantt/curriculum-fab/action-items/CreateCurriculumHoverMenu.tsx#L9)

## Properties

### activeAction

> **activeAction**: `null` \| `string`

Defined in: [ui/src/components/gantt/curriculum-fab/action-items/CreateCurriculumHoverMenu.tsx:11](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/gantt/curriculum-fab/action-items/CreateCurriculumHoverMenu.tsx#L11)

***

### isDisabled

> **isDisabled**: `boolean`

Defined in: [ui/src/components/gantt/curriculum-fab/action-items/CreateCurriculumHoverMenu.tsx:10](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/gantt/curriculum-fab/action-items/CreateCurriculumHoverMenu.tsx#L10)

***

### makeProcessingHandler

> **makeProcessingHandler**: (`key`) => (`loading`) => `void`

Defined in: [ui/src/components/gantt/curriculum-fab/action-items/CreateCurriculumHoverMenu.tsx:13](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/gantt/curriculum-fab/action-items/CreateCurriculumHoverMenu.tsx#L13)

#### Parameters

##### key

`"createDraft"` \| `"createFromTemplate"` \| `"duplicate"`

#### Returns

(`loading`) => `void`

***

### onCreate

> **onCreate**: (`newCurriculum`) => `void`

Defined in: [ui/src/components/gantt/curriculum-fab/action-items/CreateCurriculumHoverMenu.tsx:12](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/gantt/curriculum-fab/action-items/CreateCurriculumHoverMenu.tsx#L12)

#### Parameters

##### newCurriculum

[`GanttCurriculumDocument`](../../../../../../api-client/gantt/curriculum/type-aliases/GanttCurriculumDocument.md)

#### Returns

`void`

***

### sourceCurriculum?

> `optional` **sourceCurriculum?**: [`GanttCurriculumDocument`](../../../../../../api-client/gantt/curriculum/type-aliases/GanttCurriculumDocument.md) \| `null`

Defined in: [ui/src/components/gantt/curriculum-fab/action-items/CreateCurriculumHoverMenu.tsx:16](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/gantt/curriculum-fab/action-items/CreateCurriculumHoverMenu.tsx#L16)
