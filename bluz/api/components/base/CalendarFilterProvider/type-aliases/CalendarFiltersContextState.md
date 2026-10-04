[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/base/CalendarFilterProvider](../index.md) / CalendarFiltersContextState

# Type Alias: CalendarFiltersContextState

> **CalendarFiltersContextState** = `object`

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:18](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/base/CalendarFilterProvider.tsx#L18)

## Properties

### clearFilters

> **clearFilters**: () => `void`

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:38](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/base/CalendarFilterProvider.tsx#L38)

Resets every filter to its default, showing the full calendar again.

#### Returns

`void`

***

### default

> **default**: `boolean`

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:19](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/base/CalendarFilterProvider.tsx#L19)

***

### eventFilteredOpacity

> **eventFilteredOpacity**: (`event`) => `number`

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:33](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/base/CalendarFilterProvider.tsx#L33)

#### Parameters

##### event

[`Event`](../../../../api-shared/types/event/type-aliases/Event.md)

#### Returns

`number`

***

### filteredCourses

> **filteredCourses**: [`CourseId`](../../../../api-shared/types/course/type-aliases/CourseId.md)[]

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:22](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/base/CalendarFilterProvider.tsx#L22)

***

### filteredInstructors

> **filteredInstructors**: `number`[]

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:20](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/base/CalendarFilterProvider.tsx#L20)

***

### filteredRoom

> **filteredRoom**: `null` \| `string`

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:26](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/base/CalendarFilterProvider.tsx#L26)

***

### hasActiveFilters

> **hasActiveFilters**: `boolean`

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:36](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/base/CalendarFilterProvider.tsx#L36)

True when any filter is narrowing the calendar.

***

### hidePrayers

> **hidePrayers**: `boolean`

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:28](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/base/CalendarFilterProvider.tsx#L28)

***

### setFilteredCourses

> **setFilteredCourses**: `Dispatch`\<`SetStateAction`\<[`CourseId`](../../../../api-shared/types/course/type-aliases/CourseId.md)[]\>\>

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:23](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/base/CalendarFilterProvider.tsx#L23)

***

### setFilteredInstructors

> **setFilteredInstructors**: `Dispatch`\<`SetStateAction`\<`number`[]\>\>

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:21](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/base/CalendarFilterProvider.tsx#L21)

***

### setFilteredRoom

> **setFilteredRoom**: `Dispatch`\<`SetStateAction`\<`null` \| `string`\>\>

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:27](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/base/CalendarFilterProvider.tsx#L27)

***

### setHidePrayers

> **setHidePrayers**: `Dispatch`\<`SetStateAction`\<`boolean`\>\>

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:29](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/base/CalendarFilterProvider.tsx#L29)

***

### setShowMisconfigurations

> **setShowMisconfigurations**: `Dispatch`\<`SetStateAction`\<`boolean`\>\>

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:31](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/base/CalendarFilterProvider.tsx#L31)

***

### setShowPAsFor

> **setShowPAsFor**: `Dispatch`\<`SetStateAction`\<`null` \| `number`\>\>

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:25](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/base/CalendarFilterProvider.tsx#L25)

***

### showMisconfigurations

> **showMisconfigurations**: `boolean`

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:30](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/base/CalendarFilterProvider.tsx#L30)

***

### showPAsFor

> **showPAsFor**: `null` \| `number`

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:24](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/base/CalendarFilterProvider.tsx#L24)
