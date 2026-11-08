[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/base/CalendarFilterProvider](../index.md) / CalendarFiltersContextState

# Type Alias: CalendarFiltersContextState

> **CalendarFiltersContextState** = `object`

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:26](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/components/base/CalendarFilterProvider.tsx#L26)

## Properties

### clearFilters

> **clearFilters**: () => `void`

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:72](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/components/base/CalendarFilterProvider.tsx#L72)

Resets every filter to its default, showing the full calendar again.

#### Returns

`void`

***

### default

> **default**: `boolean`

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:27](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/components/base/CalendarFilterProvider.tsx#L27)

***

### eventFilteredOpacity

> **eventFilteredOpacity**: (`event`) => `number`

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:67](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/components/base/CalendarFilterProvider.tsx#L67)

#### Parameters

##### event

[`Event`](../../../../api-shared/types/event/type-aliases/Event.md)

#### Returns

`number`

***

### filteredCourses

> **filteredCourses**: [`CourseId`](../../../../api-shared/types/course/type-aliases/CourseId.md)[]

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:30](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/components/base/CalendarFilterProvider.tsx#L30)

***

### filteredInstructors

> **filteredInstructors**: `number`[]

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:28](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/components/base/CalendarFilterProvider.tsx#L28)

***

### filteredRooms

> **filteredRooms**: `string`[]

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:35](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/components/base/CalendarFilterProvider.tsx#L35)

Room resource keys to show; empty shows every room (#1018).

***

### hasActiveFilters

> **hasActiveFilters**: `boolean`

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:70](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/components/base/CalendarFilterProvider.tsx#L70)

True when any filter is narrowing the calendar.

***

### setFilteredCourses

> **setFilteredCourses**: `Dispatch`\<`SetStateAction`\<[`CourseId`](../../../../api-shared/types/course/type-aliases/CourseId.md)[]\>\>

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:31](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/components/base/CalendarFilterProvider.tsx#L31)

***

### setFilteredInstructors

> **setFilteredInstructors**: `Dispatch`\<`SetStateAction`\<`number`[]\>\>

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:29](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/components/base/CalendarFilterProvider.tsx#L29)

***

### setFilteredRooms

> **setFilteredRooms**: `Dispatch`\<`SetStateAction`\<`string`[]\>\>

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:36](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/components/base/CalendarFilterProvider.tsx#L36)

***

### setShowHiveLessonIssues

> **setShowHiveLessonIssues**: `Dispatch`\<`SetStateAction`\<`boolean`\>\>

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:52](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/components/base/CalendarFilterProvider.tsx#L52)

***

### setShowMisconfigurations

> **setShowMisconfigurations**: `Dispatch`\<`SetStateAction`\<`boolean`\>\>

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:45](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/components/base/CalendarFilterProvider.tsx#L45)

***

### setShowPAsFor

> **setShowPAsFor**: `Dispatch`\<`SetStateAction`\<`null` \| `number`\>\>

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:33](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/components/base/CalendarFilterProvider.tsx#L33)

***

### setShowPrayers

> **setShowPrayers**: `Dispatch`\<`SetStateAction`\<`boolean`\>\>

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:43](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/components/base/CalendarFilterProvider.tsx#L43)

***

### setShowUnavailabilities

> **setShowUnavailabilities**: `Dispatch`\<`SetStateAction`\<`boolean`\>\>

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:65](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/components/base/CalendarFilterProvider.tsx#L65)

***

### setShowUnstaffedOnly

> **setShowUnstaffedOnly**: `Dispatch`\<`SetStateAction`\<`boolean`\>\>

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:58](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/components/base/CalendarFilterProvider.tsx#L58)

***

### showHiveLessonIssues

> **showHiveLessonIssues**: `boolean`

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:51](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/components/base/CalendarFilterProvider.tsx#L51)

Mark events whose Hive lesson is missing or will not reach their
shuffles (#1025). Off by default: a schedule still being built would be
all markers.

***

### showMisconfigurations

> **showMisconfigurations**: `boolean`

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:44](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/components/base/CalendarFilterProvider.tsx#L44)

***

### showPAsFor

> **showPAsFor**: `null` \| `number`

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:32](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/components/base/CalendarFilterProvider.tsx#L32)

***

### showPrayers

> **showPrayers**: `boolean`

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:42](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/components/base/CalendarFilterProvider.tsx#L42)

Tint the daily prayer windows and the Shabbat window (כניסת שבת → צאת
שבת, #996) light red, and show the hand-made prayer events. Off hides
all three.

***

### showUnavailabilities

> **showUnavailabilities**: `boolean`

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:64](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/components/base/CalendarFilterProvider.tsx#L64)

Show staff unavailabilities (אי זמינות), in the day view's "אי
זמינויות" column. Off by default: they are planning context, not
schedule.

***

### showUnstaffedOnly

> **showUnstaffedOnly**: `boolean`

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:57](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/components/base/CalendarFilterProvider.tsx#L57)

Show only events still missing a מבזר (#1029). Prayers and breaks never
take one, so they leave the calendar too.
