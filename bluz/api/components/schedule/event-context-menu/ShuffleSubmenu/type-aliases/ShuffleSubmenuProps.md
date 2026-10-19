[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/schedule/event-context-menu/ShuffleSubmenu](../index.md) / ShuffleSubmenuProps

# Type Alias: ShuffleSubmenuProps

> **ShuffleSubmenuProps** = `object`

Defined in: [ui/src/components/schedule/event-context-menu/ShuffleSubmenu.tsx:12](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/components/schedule/event-context-menu/ShuffleSubmenu.tsx#L12)

## Properties

### disabled?

> `optional` **disabled?**: `boolean`

Defined in: [ui/src/components/schedule/event-context-menu/ShuffleSubmenu.tsx:18](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/components/schedule/event-context-menu/ShuffleSubmenu.tsx#L18)

***

### onToggle

> **onToggle**: (`courseId`) => `void`

Defined in: [ui/src/components/schedule/event-context-menu/ShuffleSubmenu.tsx:17](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/components/schedule/event-context-menu/ShuffleSubmenu.tsx#L17)

#### Parameters

##### courseId

[`CourseId`](../../../../../api-shared/types/course/type-aliases/CourseId.md)

#### Returns

`void`

***

### shuffles

> **shuffles**: `ReadonlyArray`\<[`Course`](../../../../../api-shared/types/course/type-aliases/Course.md)\>

Defined in: [ui/src/components/schedule/event-context-menu/ShuffleSubmenu.tsx:14](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/components/schedule/event-context-menu/ShuffleSubmenu.tsx#L14)

The event's syllabus shuffles, already resolved.

***

### stateOf

> **stateOf**: (`courseId`) => `"all"` \| `"none"` \| `"some"`

Defined in: [ui/src/components/schedule/event-context-menu/ShuffleSubmenu.tsx:16](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/components/schedule/event-context-menu/ShuffleSubmenu.tsx#L16)

Whether all, some or none of the targeted events carry the shuffle.

#### Parameters

##### courseId

[`CourseId`](../../../../../api-shared/types/course/type-aliases/CourseId.md)

#### Returns

`"all"` \| `"none"` \| `"some"`
