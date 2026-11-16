[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/schedule/event-context-menu/InstructorSubmenu](../index.md) / InstructorSubmenuProps

# Type Alias: InstructorSubmenuProps

> **InstructorSubmenuProps** = `object`

Defined in: [ui/src/components/schedule/event-context-menu/InstructorSubmenu.tsx:23](https://github.com/System-B90/Bluz/blob/182d51c797407c7b0ea37986b1a45ab0e64c4df0/ui/src/components/schedule/event-context-menu/InstructorSubmenu.tsx#L23)

## Properties

### disabled?

> `optional` **disabled?**: `boolean`

Defined in: [ui/src/components/schedule/event-context-menu/InstructorSubmenu.tsx:27](https://github.com/System-B90/Bluz/blob/182d51c797407c7b0ea37986b1a45ab0e64c4df0/ui/src/components/schedule/event-context-menu/InstructorSubmenu.tsx#L27)

***

### onToggle

> **onToggle**: (`instructorId`) => `void`

Defined in: [ui/src/components/schedule/event-context-menu/InstructorSubmenu.tsx:26](https://github.com/System-B90/Bluz/blob/182d51c797407c7b0ea37986b1a45ab0e64c4df0/ui/src/components/schedule/event-context-menu/InstructorSubmenu.tsx#L26)

#### Parameters

##### instructorId

`number`

#### Returns

`void`

***

### stateOf

> **stateOf**: (`instructorId`) => `"all"` \| `"none"` \| `"some"`

Defined in: [ui/src/components/schedule/event-context-menu/InstructorSubmenu.tsx:25](https://github.com/System-B90/Bluz/blob/182d51c797407c7b0ea37986b1a45ab0e64c4df0/ui/src/components/schedule/event-context-menu/InstructorSubmenu.tsx#L25)

Whether all, some or none of the targeted events are staffed by them.

#### Parameters

##### instructorId

`number`

#### Returns

`"all"` \| `"none"` \| `"some"`
