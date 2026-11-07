[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [components/settings-dialog/tabs/global/hive-group-links/use-curriculum-shuffles](../index.md) / useCurriculumShuffles

# Function: useCurriculumShuffles()

> **useCurriculumShuffles**(`curriculumId`): `object`

Defined in: [ui/src/components/settings-dialog/tabs/global/hive-group-links/use-curriculum-shuffles.ts:56](https://github.com/System-B90/Bluz/blob/1b02178048002eee34d502b2e3e2a402e1b9c9c0/ui/src/components/settings-dialog/tabs/global/hive-group-links/use-curriculum-shuffles.ts#L56)

The shuffles of one curriculum's syllabuses, and a writer that links a
shuffle name to a Hive group in every syllabus that defines it. `null`
curriculum ⇒ nothing loaded.

## Parameters

### curriculumId

`string` \| `null`

## Returns

`object`

### error

> **error**: \{ \} \| `null`

### isLoading

> **isLoading**: `boolean`

### linkShuffle

> **linkShuffle**: (`name`, `groupId`) => `Promise`\<`void`\>

#### Parameters

##### name

`string`

##### groupId

`number` \| `undefined`

#### Returns

`Promise`\<`void`\>

### shuffles

> **shuffles**: [`CurriculumShuffle`](../type-aliases/CurriculumShuffle.md)[]
