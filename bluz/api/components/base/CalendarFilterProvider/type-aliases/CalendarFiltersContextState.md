[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/base/CalendarFilterProvider](../index.md) / CalendarFiltersContextState

# Type Alias: CalendarFiltersContextState

> **CalendarFiltersContextState** = `object`

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:17](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/base/CalendarFilterProvider.tsx#L17)

## Properties

### clearFilters

> **clearFilters**: () => `void`

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:37](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/base/CalendarFilterProvider.tsx#L37)

Resets every filter to its default, showing the full calendar again.

#### Returns

`void`

***

### default

> **default**: `boolean`

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:18](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/base/CalendarFilterProvider.tsx#L18)

***

### eventFilteredOpacity

> **eventFilteredOpacity**: (`event`) => `number`

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:32](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/base/CalendarFilterProvider.tsx#L32)

#### Parameters

##### event

[`Event`](../../../../api-shared/types/event/type-aliases/Event.md)

#### Returns

`number`

***

### filteredCourses

> **filteredCourses**: [`CourseId`](../../../../api-shared/types/course/type-aliases/CourseId.md)[]

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:21](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/base/CalendarFilterProvider.tsx#L21)

***

### filteredInstructors

> **filteredInstructors**: `number`[]

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:19](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/base/CalendarFilterProvider.tsx#L19)

***

### filteredRoom

> **filteredRoom**: `null` \| `string`

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:25](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/base/CalendarFilterProvider.tsx#L25)

***

### hasActiveFilters

> **hasActiveFilters**: `boolean`

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:35](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/base/CalendarFilterProvider.tsx#L35)

True when any filter is narrowing the calendar.

***

### hidePrayers

> **hidePrayers**: `boolean`

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:27](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/base/CalendarFilterProvider.tsx#L27)

***

### setFilteredCourses

> **setFilteredCourses**: `Dispatch`\<`SetStateAction`\<[`CourseId`](../../../../api-shared/types/course/type-aliases/CourseId.md)[]\>\>

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:22](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/base/CalendarFilterProvider.tsx#L22)

***

### setFilteredInstructors

> **setFilteredInstructors**: `Dispatch`\<`SetStateAction`\<`number`[]\>\>

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:20](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/base/CalendarFilterProvider.tsx#L20)

***

### setFilteredRoom

> **setFilteredRoom**: `Dispatch`\<`SetStateAction`\<`null` \| `string`\>\>

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:26](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/base/CalendarFilterProvider.tsx#L26)

***

### setHidePrayers

> **setHidePrayers**: `Dispatch`\<`SetStateAction`\<`boolean`\>\>

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:28](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/base/CalendarFilterProvider.tsx#L28)

***

### setShowMisconfigurations

> **setShowMisconfigurations**: `Dispatch`\<`SetStateAction`\<`boolean`\>\>

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:30](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/base/CalendarFilterProvider.tsx#L30)

***

### setShowPAsFor

> **setShowPAsFor**: `Dispatch`\<`SetStateAction`\<`null` \| `number`\>\>

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:24](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/base/CalendarFilterProvider.tsx#L24)

***

### showMisconfigurations

> **showMisconfigurations**: `boolean`

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:29](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/base/CalendarFilterProvider.tsx#L29)

***

### showPAsFor

> **showPAsFor**: `null` \| `number`

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:23](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/base/CalendarFilterProvider.tsx#L23)
