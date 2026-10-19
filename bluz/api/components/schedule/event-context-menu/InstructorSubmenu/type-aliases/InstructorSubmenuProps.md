[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/schedule/event-context-menu/InstructorSubmenu](../index.md) / InstructorSubmenuProps

# Type Alias: InstructorSubmenuProps

> **InstructorSubmenuProps** = `object`

Defined in: [ui/src/components/schedule/event-context-menu/InstructorSubmenu.tsx:23](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/components/schedule/event-context-menu/InstructorSubmenu.tsx#L23)

## Properties

### disabled?

> `optional` **disabled?**: `boolean`

Defined in: [ui/src/components/schedule/event-context-menu/InstructorSubmenu.tsx:27](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/components/schedule/event-context-menu/InstructorSubmenu.tsx#L27)

***

### onToggle

> **onToggle**: (`instructorId`) => `void`

Defined in: [ui/src/components/schedule/event-context-menu/InstructorSubmenu.tsx:26](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/components/schedule/event-context-menu/InstructorSubmenu.tsx#L26)

#### Parameters

##### instructorId

`number`

#### Returns

`void`

***

### stateOf

> **stateOf**: (`instructorId`) => `"all"` \| `"none"` \| `"some"`

Defined in: [ui/src/components/schedule/event-context-menu/InstructorSubmenu.tsx:25](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/components/schedule/event-context-menu/InstructorSubmenu.tsx#L25)

Whether all, some or none of the targeted events are staffed by them.

#### Parameters

##### instructorId

`number`

#### Returns

`"all"` \| `"none"` \| `"some"`
