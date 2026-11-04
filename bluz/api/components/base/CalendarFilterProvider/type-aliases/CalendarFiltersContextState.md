[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/base/CalendarFilterProvider](../index.md) / CalendarFiltersContextState

# Type Alias: CalendarFiltersContextState

> **CalendarFiltersContextState** = `object`

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:25](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/components/base/CalendarFilterProvider.tsx#L25)

## Properties

### clearFilters

> **clearFilters**: () => `void`

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:64](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/components/base/CalendarFilterProvider.tsx#L64)

Resets every filter to its default, showing the full calendar again.

#### Returns

`void`

***

### default

> **default**: `boolean`

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:26](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/components/base/CalendarFilterProvider.tsx#L26)

***

### eventFilteredOpacity

> **eventFilteredOpacity**: (`event`) => `number`

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:59](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/components/base/CalendarFilterProvider.tsx#L59)

#### Parameters

##### event

[`Event`](../../../../api-shared/types/event/type-aliases/Event.md)

#### Returns

`number`

***

### filteredCourses

> **filteredCourses**: [`CourseId`](../../../../api-shared/types/course/type-aliases/CourseId.md)[]

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:29](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/components/base/CalendarFilterProvider.tsx#L29)

***

### filteredInstructors

> **filteredInstructors**: `number`[]

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:27](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/components/base/CalendarFilterProvider.tsx#L27)

***

### filteredRooms

> **filteredRooms**: `string`[]

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:34](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/components/base/CalendarFilterProvider.tsx#L34)

Room resource keys to show; empty shows every room (#1018).

***

### hasActiveFilters

> **hasActiveFilters**: `boolean`

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:62](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/components/base/CalendarFilterProvider.tsx#L62)

True when any filter is narrowing the calendar.

***

### setFilteredCourses

> **setFilteredCourses**: `Dispatch`\<`SetStateAction`\<[`CourseId`](../../../../api-shared/types/course/type-aliases/CourseId.md)[]\>\>

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:30](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/components/base/CalendarFilterProvider.tsx#L30)

***

### setFilteredInstructors

> **setFilteredInstructors**: `Dispatch`\<`SetStateAction`\<`number`[]\>\>

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:28](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/components/base/CalendarFilterProvider.tsx#L28)

***

### setFilteredRooms

> **setFilteredRooms**: `Dispatch`\<`SetStateAction`\<`string`[]\>\>

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:35](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/components/base/CalendarFilterProvider.tsx#L35)

***

### setShowHiveLessonIssues

> **setShowHiveLessonIssues**: `Dispatch`\<`SetStateAction`\<`boolean`\>\>

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:51](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/components/base/CalendarFilterProvider.tsx#L51)

***

### setShowMisconfigurations

> **setShowMisconfigurations**: `Dispatch`\<`SetStateAction`\<`boolean`\>\>

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:44](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/components/base/CalendarFilterProvider.tsx#L44)

***

### setShowPAsFor

> **setShowPAsFor**: `Dispatch`\<`SetStateAction`\<`null` \| `number`\>\>

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:32](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/components/base/CalendarFilterProvider.tsx#L32)

***

### setShowPrayers

> **setShowPrayers**: `Dispatch`\<`SetStateAction`\<`boolean`\>\>

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:42](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/components/base/CalendarFilterProvider.tsx#L42)

***

### setShowUnstaffedOnly

> **setShowUnstaffedOnly**: `Dispatch`\<`SetStateAction`\<`boolean`\>\>

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:57](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/components/base/CalendarFilterProvider.tsx#L57)

***

### showHiveLessonIssues

> **showHiveLessonIssues**: `boolean`

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:50](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/components/base/CalendarFilterProvider.tsx#L50)

Mark events whose Hive lesson is missing or will not reach their
shuffles (#1025). Off by default: a schedule still being built would be
all markers.

***

### showMisconfigurations

> **showMisconfigurations**: `boolean`

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:43](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/components/base/CalendarFilterProvider.tsx#L43)

***

### showPAsFor

> **showPAsFor**: `null` \| `number`

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:31](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/components/base/CalendarFilterProvider.tsx#L31)

***

### showPrayers

> **showPrayers**: `boolean`

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:41](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/components/base/CalendarFilterProvider.tsx#L41)

Tint the daily prayer windows and the Shabbat window (כניסת שבת → צאת
שבת, #996) light red, and show the hand-made prayer events. Off hides
all three.

***

### showUnstaffedOnly

> **showUnstaffedOnly**: `boolean`

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:56](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/components/base/CalendarFilterProvider.tsx#L56)

Show only events still missing a מבזר (#1029). Prayers and breaks never
take one, so they leave the calendar too.
