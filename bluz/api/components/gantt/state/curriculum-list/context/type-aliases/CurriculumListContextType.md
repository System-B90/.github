[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/gantt/state/curriculum-list/context](../index.md) / CurriculumListContextType

# Type Alias: CurriculumListContextType

> **CurriculumListContextType** = `object`

Defined in: [ui/src/components/gantt/state/curriculum-list/context.ts:11](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/gantt/state/curriculum-list/context.ts#L11)

## Properties

### currentCurriculum

> **currentCurriculum**: [`GanttCurriculumId`](../../../../../../api-shared/types/gantt/models/curriculum/type-aliases/GanttCurriculumId.md) \| `null`

Defined in: [ui/src/components/gantt/state/curriculum-list/context.ts:18](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/gantt/state/curriculum-list/context.ts#L18)

***

### curriculums

> **curriculums**: `Record`\<[`GanttCurriculumId`](../../../../../../api-shared/types/gantt/models/curriculum/type-aliases/GanttCurriculumId.md), [`GanttCurriculumDocument`](../../../../../../api-client/gantt/curriculum/type-aliases/GanttCurriculumDocument.md)\>

Defined in: [ui/src/components/gantt/state/curriculum-list/context.ts:13](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/gantt/state/curriculum-list/context.ts#L13)

***

### dispatch

> **dispatch**: `Dispatch`\<[`CurriculumListAction`](../../types/type-aliases/CurriculumListAction.md)\>

Defined in: [ui/src/components/gantt/state/curriculum-list/context.ts:27](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/gantt/state/curriculum-list/context.ts#L27)

***

### error

> **error**: `null` \| `string`

Defined in: [ui/src/components/gantt/state/curriculum-list/context.ts:15](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/gantt/state/curriculum-list/context.ts#L15)

***

### groups

> **groups**: [`CurriculumGroups`](../../types/type-aliases/CurriculumGroups.md)

Defined in: [ui/src/components/gantt/state/curriculum-list/context.ts:16](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/gantt/state/curriculum-list/context.ts#L16)

***

### isLoading

> **isLoading**: `boolean`

Defined in: [ui/src/components/gantt/state/curriculum-list/context.ts:14](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/gantt/state/curriculum-list/context.ts#L14)

***

### onCreate

> **onCreate**: (`newCurriculum`) => `void`

Defined in: [ui/src/components/gantt/state/curriculum-list/context.ts:20](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/gantt/state/curriculum-list/context.ts#L20)

#### Parameters

##### newCurriculum

[`GanttCurriculumDocument`](../../../../../../api-client/gantt/curriculum/type-aliases/GanttCurriculumDocument.md)

#### Returns

`void`

***

### onDelete

> **onDelete**: (`deletedCurriculumId`) => `void`

Defined in: [ui/src/components/gantt/state/curriculum-list/context.ts:21](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/gantt/state/curriculum-list/context.ts#L21)

#### Parameters

##### deletedCurriculumId

[`GanttCurriculumId`](../../../../../../api-shared/types/gantt/models/curriculum/type-aliases/GanttCurriculumId.md)

#### Returns

`void`

***

### refreshCurriculums

> **refreshCurriculums**: () => `Promise`\<`void`\>

Defined in: [ui/src/components/gantt/state/curriculum-list/context.ts:26](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/gantt/state/curriculum-list/context.ts#L26)

#### Returns

`Promise`\<`void`\>

***

### setCurrentCurriculum

> **setCurrentCurriculum**: `Dispatch`\<`SetStateAction`\<[`GanttCurriculumId`](../../../../../../api-shared/types/gantt/models/curriculum/type-aliases/GanttCurriculumId.md) \| `null`\>\>

Defined in: [ui/src/components/gantt/state/curriculum-list/context.ts:19](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/gantt/state/curriculum-list/context.ts#L19)

***

### sortedIds

> **sortedIds**: [`GanttCurriculumId`](../../../../../../api-shared/types/gantt/models/curriculum/type-aliases/GanttCurriculumId.md)[]

Defined in: [ui/src/components/gantt/state/curriculum-list/context.ts:17](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/gantt/state/curriculum-list/context.ts#L17)

***

### state

> **state**: [`CurriculumListState`](../../types/type-aliases/CurriculumListState.md)

Defined in: [ui/src/components/gantt/state/curriculum-list/context.ts:12](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/gantt/state/curriculum-list/context.ts#L12)

***

### updateCurriculum

> **updateCurriculum**: (`id`, `updates`) => `void`

Defined in: [ui/src/components/gantt/state/curriculum-list/context.ts:22](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/gantt/state/curriculum-list/context.ts#L22)

#### Parameters

##### id

[`GanttCurriculumId`](../../../../../../api-shared/types/gantt/models/curriculum/type-aliases/GanttCurriculumId.md)

##### updates

`Partial`\<[`GanttCurriculumDocument`](../../../../../../api-client/gantt/curriculum/type-aliases/GanttCurriculumDocument.md)\>

#### Returns

`void`
