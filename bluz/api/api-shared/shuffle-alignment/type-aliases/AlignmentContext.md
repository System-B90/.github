[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/shuffle-alignment](../index.md) / AlignmentContext

# Type Alias: AlignmentContext

> **AlignmentContext** = `object`

Defined in: [ui/src/api-shared/shuffle-alignment.ts:38](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/api-shared/shuffle-alignment.ts#L38)

## Properties

### isShuffle

> **isShuffle**: (`courseId`) => `boolean`

Defined in: [ui/src/api-shared/shuffle-alignment.ts:40](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/api-shared/shuffle-alignment.ts#L40)

True for course ids that are shuffles.

#### Parameters

##### courseId

`string`

#### Returns

`boolean`

***

### shuffleName

> **shuffleName**: (`courseId`) => `string`

Defined in: [ui/src/api-shared/shuffle-alignment.ts:42](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/api-shared/shuffle-alignment.ts#L42)

Shuffle course id → display name.

#### Parameters

##### courseId

`string`

#### Returns

`string`

***

### syllabusName

> **syllabusName**: (`subjectId`) => `string`

Defined in: [ui/src/api-shared/shuffle-alignment.ts:44](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/api-shared/shuffle-alignment.ts#L44)

Hive subject id → syllabus display name.

#### Parameters

##### subjectId

`number` \| `string`

#### Returns

`string`

***

### timezone?

> `optional` **timezone?**: `string`

Defined in: [ui/src/api-shared/shuffle-alignment.ts:45](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/api-shared/shuffle-alignment.ts#L45)
