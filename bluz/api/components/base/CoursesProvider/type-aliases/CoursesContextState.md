[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/base/CoursesProvider](../index.md) / CoursesContextState

# Type Alias: CoursesContextState

> **CoursesContextState** = `object`

Defined in: [ui/src/components/base/CoursesProvider.tsx:14](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/base/CoursesProvider.tsx#L14)

## Properties

### addCourse

> **addCourse**: (`course`) => `Promise`\<`void`\>

Defined in: [ui/src/components/base/CoursesProvider.tsx:18](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/base/CoursesProvider.tsx#L18)

#### Parameters

##### course

`Omit`\<[`Course`](../../../../api-shared/types/course/type-aliases/Course.md), `"id"`\>

#### Returns

`Promise`\<`void`\>

***

### courses

> **courses**: [`Course`](../../../../api-shared/types/course/type-aliases/Course.md)[]

Defined in: [ui/src/components/base/CoursesProvider.tsx:16](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/base/CoursesProvider.tsx#L16)

***

### default

> **default**: `boolean`

Defined in: [ui/src/components/base/CoursesProvider.tsx:15](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/base/CoursesProvider.tsx#L15)

***

### deleteCourse

> **deleteCourse**: (`courseId`) => `Promise`\<`void`\>

Defined in: [ui/src/components/base/CoursesProvider.tsx:24](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/base/CoursesProvider.tsx#L24)

#### Parameters

##### courseId

[`CourseId`](../../../../api-shared/types/course/type-aliases/CourseId.md)

#### Returns

`Promise`\<`void`\>

***

### getCourse

> **getCourse**: (`id`) => [`Course`](../../../../api-shared/types/course/type-aliases/Course.md) \| `undefined`

Defined in: [ui/src/components/base/CoursesProvider.tsx:17](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/base/CoursesProvider.tsx#L17)

#### Parameters

##### id

[`CourseId`](../../../../api-shared/types/course/type-aliases/CourseId.md)

#### Returns

[`Course`](../../../../api-shared/types/course/type-aliases/Course.md) \| `undefined`

***

### updateCourse

> **updateCourse**: (`course`) => `Promise`\<`void`\>

Defined in: [ui/src/components/base/CoursesProvider.tsx:19](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/base/CoursesProvider.tsx#L19)

#### Parameters

##### course

[`Course`](../../../../api-shared/types/course/type-aliases/Course.md)

#### Returns

`Promise`\<`void`\>

***

### updateCoursePartial

> **updateCoursePartial**: (`id`, `changes`) => `Promise`\<`void`\>

Defined in: [ui/src/components/base/CoursesProvider.tsx:20](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/base/CoursesProvider.tsx#L20)

#### Parameters

##### id

[`CourseId`](../../../../api-shared/types/course/type-aliases/CourseId.md)

##### changes

`Partial`\<[`Course`](../../../../api-shared/types/course/type-aliases/Course.md)\>

#### Returns

`Promise`\<`void`\>
