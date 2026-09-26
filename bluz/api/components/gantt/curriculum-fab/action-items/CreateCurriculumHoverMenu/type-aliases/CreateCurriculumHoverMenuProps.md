[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/gantt/curriculum-fab/action-items/CreateCurriculumHoverMenu](../index.md) / CreateCurriculumHoverMenuProps

# Type Alias: CreateCurriculumHoverMenuProps

> **CreateCurriculumHoverMenuProps** = `object`

Defined in: [ui/src/components/gantt/curriculum-fab/action-items/CreateCurriculumHoverMenu.tsx:12](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/gantt/curriculum-fab/action-items/CreateCurriculumHoverMenu.tsx#L12)

## Properties

### activeAction

> **activeAction**: `null` \| `string`

Defined in: [ui/src/components/gantt/curriculum-fab/action-items/CreateCurriculumHoverMenu.tsx:14](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/gantt/curriculum-fab/action-items/CreateCurriculumHoverMenu.tsx#L14)

***

### isDisabled

> **isDisabled**: `boolean`

Defined in: [ui/src/components/gantt/curriculum-fab/action-items/CreateCurriculumHoverMenu.tsx:13](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/gantt/curriculum-fab/action-items/CreateCurriculumHoverMenu.tsx#L13)

***

### makeProcessingHandler

> **makeProcessingHandler**: (`key`) => (`loading`) => `void`

Defined in: [ui/src/components/gantt/curriculum-fab/action-items/CreateCurriculumHoverMenu.tsx:16](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/gantt/curriculum-fab/action-items/CreateCurriculumHoverMenu.tsx#L16)

#### Parameters

##### key

`"createDraft"` \| `"createFromTemplate"` \| `"duplicate"`

#### Returns

(`loading`) => `void`

***

### onCreate

> **onCreate**: (`newCurriculum`) => `void`

Defined in: [ui/src/components/gantt/curriculum-fab/action-items/CreateCurriculumHoverMenu.tsx:15](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/gantt/curriculum-fab/action-items/CreateCurriculumHoverMenu.tsx#L15)

#### Parameters

##### newCurriculum

[`GanttCurriculumDocument`](../../../../../../api-client/gantt/curriculum/type-aliases/GanttCurriculumDocument.md)

#### Returns

`void`

***

### sourceCurriculum?

> `optional` **sourceCurriculum?**: [`GanttCurriculumDocument`](../../../../../../api-client/gantt/curriculum/type-aliases/GanttCurriculumDocument.md) \| `null`

Defined in: [ui/src/components/gantt/curriculum-fab/action-items/CreateCurriculumHoverMenu.tsx:19](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/gantt/curriculum-fab/action-items/CreateCurriculumHoverMenu.tsx#L19)
