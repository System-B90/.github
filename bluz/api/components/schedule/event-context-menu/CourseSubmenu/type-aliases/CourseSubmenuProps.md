[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/schedule/event-context-menu/CourseSubmenu](../index.md) / CourseSubmenuProps

# Type Alias: CourseSubmenuProps

> **CourseSubmenuProps** = `object`

Defined in: [ui/src/components/schedule/event-context-menu/CourseSubmenu.tsx:18](https://github.com/System-B90/Bluz/blob/23625511d59d71bc9679adc341fb0bcb28897208/ui/src/components/schedule/event-context-menu/CourseSubmenu.tsx#L18)

## Properties

### onToggle

> **onToggle**: (`courseId`) => `void`

Defined in: [ui/src/components/schedule/event-context-menu/CourseSubmenu.tsx:21](https://github.com/System-B90/Bluz/blob/23625511d59d71bc9679adc341fb0bcb28897208/ui/src/components/schedule/event-context-menu/CourseSubmenu.tsx#L21)

#### Parameters

##### courseId

[`CourseId`](../../../../../api-shared/types/course/type-aliases/CourseId.md)

#### Returns

`void`

***

### stateOf

> **stateOf**: (`courseId`) => `"all"` \| `"none"` \| `"some"`

Defined in: [ui/src/components/schedule/event-context-menu/CourseSubmenu.tsx:20](https://github.com/System-B90/Bluz/blob/23625511d59d71bc9679adc341fb0bcb28897208/ui/src/components/schedule/event-context-menu/CourseSubmenu.tsx#L20)

Whether all, some or none of the targeted events carry the course.

#### Parameters

##### courseId

[`CourseId`](../../../../../api-shared/types/course/type-aliases/CourseId.md)

#### Returns

`"all"` \| `"none"` \| `"some"`
