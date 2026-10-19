[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/gantt/curriculum-fab/action-items/CreateCurriculumHoverMenu](../index.md) / CreateCurriculumHoverMenuProps

# Type Alias: CreateCurriculumHoverMenuProps

> **CreateCurriculumHoverMenuProps** = `object`

Defined in: [ui/src/components/gantt/curriculum-fab/action-items/CreateCurriculumHoverMenu.tsx:8](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/components/gantt/curriculum-fab/action-items/CreateCurriculumHoverMenu.tsx#L8)

## Properties

### activeAction

> **activeAction**: `null` \| `string`

Defined in: [ui/src/components/gantt/curriculum-fab/action-items/CreateCurriculumHoverMenu.tsx:10](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/components/gantt/curriculum-fab/action-items/CreateCurriculumHoverMenu.tsx#L10)

***

### isDisabled

> **isDisabled**: `boolean`

Defined in: [ui/src/components/gantt/curriculum-fab/action-items/CreateCurriculumHoverMenu.tsx:9](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/components/gantt/curriculum-fab/action-items/CreateCurriculumHoverMenu.tsx#L9)

***

### makeProcessingHandler

> **makeProcessingHandler**: (`key`) => (`loading`) => `void`

Defined in: [ui/src/components/gantt/curriculum-fab/action-items/CreateCurriculumHoverMenu.tsx:12](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/components/gantt/curriculum-fab/action-items/CreateCurriculumHoverMenu.tsx#L12)

#### Parameters

##### key

`"createDraft"` \| `"createFromTemplate"` \| `"duplicate"`

#### Returns

(`loading`) => `void`

***

### onCreate

> **onCreate**: (`newCurriculum`) => `void`

Defined in: [ui/src/components/gantt/curriculum-fab/action-items/CreateCurriculumHoverMenu.tsx:11](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/components/gantt/curriculum-fab/action-items/CreateCurriculumHoverMenu.tsx#L11)

#### Parameters

##### newCurriculum

[`GanttCurriculumDocument`](../../../../../../api-client/gantt/curriculum/type-aliases/GanttCurriculumDocument.md)

#### Returns

`void`

***

### sourceCurriculum?

> `optional` **sourceCurriculum?**: [`GanttCurriculumDocument`](../../../../../../api-client/gantt/curriculum/type-aliases/GanttCurriculumDocument.md) \| `null`

Defined in: [ui/src/components/gantt/curriculum-fab/action-items/CreateCurriculumHoverMenu.tsx:15](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/components/gantt/curriculum-fab/action-items/CreateCurriculumHoverMenu.tsx#L15)
