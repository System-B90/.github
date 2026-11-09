[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/shuffle-alignment](../index.md) / AlignmentContext

# Type Alias: AlignmentContext

> **AlignmentContext** = `object`

Defined in: [ui/src/api-shared/shuffle-alignment.ts:46](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-shared/shuffle-alignment.ts#L46)

## Properties

### isShuffle

> **isShuffle**: (`courseId`) => `boolean`

Defined in: [ui/src/api-shared/shuffle-alignment.ts:48](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-shared/shuffle-alignment.ts#L48)

True for course ids that are shuffles.

#### Parameters

##### courseId

`string`

#### Returns

`boolean`

***

### shuffleName

> **shuffleName**: (`courseId`) => `string`

Defined in: [ui/src/api-shared/shuffle-alignment.ts:50](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-shared/shuffle-alignment.ts#L50)

Shuffle course id → display name.

#### Parameters

##### courseId

`string`

#### Returns

`string`

***

### syllabusName

> **syllabusName**: (`subjectId`) => `string`

Defined in: [ui/src/api-shared/shuffle-alignment.ts:52](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-shared/shuffle-alignment.ts#L52)

Hive subject id → syllabus display name.

#### Parameters

##### subjectId

`number` \| `string`

#### Returns

`string`

***

### timezone?

> `optional` **timezone?**: `string`

Defined in: [ui/src/api-shared/shuffle-alignment.ts:53](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-shared/shuffle-alignment.ts#L53)
