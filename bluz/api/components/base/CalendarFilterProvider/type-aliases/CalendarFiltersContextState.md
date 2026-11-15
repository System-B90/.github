[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/base/CalendarFilterProvider](../index.md) / CalendarFiltersContextState

# Type Alias: CalendarFiltersContextState

> **CalendarFiltersContextState** = `object`

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:29](https://github.com/System-B90/Bluz/blob/e82087d51f2769f8b338ee03029e86c8d2549994/ui/src/components/base/CalendarFilterProvider.tsx#L29)

## Properties

### clearFilters

> **clearFilters**: () => `void`

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:90](https://github.com/System-B90/Bluz/blob/e82087d51f2769f8b338ee03029e86c8d2549994/ui/src/components/base/CalendarFilterProvider.tsx#L90)

Resets every filter to its default, showing the full calendar again.

#### Returns

`void`

***

### default

> **default**: `boolean`

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:30](https://github.com/System-B90/Bluz/blob/e82087d51f2769f8b338ee03029e86c8d2549994/ui/src/components/base/CalendarFilterProvider.tsx#L30)

***

### eventFilteredOpacity

> **eventFilteredOpacity**: (`event`) => `number`

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:85](https://github.com/System-B90/Bluz/blob/e82087d51f2769f8b338ee03029e86c8d2549994/ui/src/components/base/CalendarFilterProvider.tsx#L85)

#### Parameters

##### event

[`Event`](../../../../api-shared/types/event/type-aliases/Event.md)

#### Returns

`number`

***

### filteredCourses

> **filteredCourses**: [`CourseId`](../../../../api-shared/types/course/type-aliases/CourseId.md)[]

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:33](https://github.com/System-B90/Bluz/blob/e82087d51f2769f8b338ee03029e86c8d2549994/ui/src/components/base/CalendarFilterProvider.tsx#L33)

***

### filteredInstructors

> **filteredInstructors**: `number`[]

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:31](https://github.com/System-B90/Bluz/blob/e82087d51f2769f8b338ee03029e86c8d2549994/ui/src/components/base/CalendarFilterProvider.tsx#L31)

***

### filteredRooms

> **filteredRooms**: `string`[]

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:42](https://github.com/System-B90/Bluz/blob/e82087d51f2769f8b338ee03029e86c8d2549994/ui/src/components/base/CalendarFilterProvider.tsx#L42)

Room resource keys to show; empty shows every room (#1018).

***

### hasActiveFilters

> **hasActiveFilters**: `boolean`

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:88](https://github.com/System-B90/Bluz/blob/e82087d51f2769f8b338ee03029e86c8d2549994/ui/src/components/base/CalendarFilterProvider.tsx#L88)

True when any filter is narrowing the calendar.

***

### setFilteredCourses

> **setFilteredCourses**: `Dispatch`\<`SetStateAction`\<[`CourseId`](../../../../api-shared/types/course/type-aliases/CourseId.md)[]\>\>

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:34](https://github.com/System-B90/Bluz/blob/e82087d51f2769f8b338ee03029e86c8d2549994/ui/src/components/base/CalendarFilterProvider.tsx#L34)

***

### setFilteredInstructors

> **setFilteredInstructors**: `Dispatch`\<`SetStateAction`\<`number`[]\>\>

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:32](https://github.com/System-B90/Bluz/blob/e82087d51f2769f8b338ee03029e86c8d2549994/ui/src/components/base/CalendarFilterProvider.tsx#L32)

***

### setFilteredRooms

> **setFilteredRooms**: `Dispatch`\<`SetStateAction`\<`string`[]\>\>

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:43](https://github.com/System-B90/Bluz/blob/e82087d51f2769f8b338ee03029e86c8d2549994/ui/src/components/base/CalendarFilterProvider.tsx#L43)

***

### setShowHiveLessonIssues

> **setShowHiveLessonIssues**: `Dispatch`\<`SetStateAction`\<`boolean`\>\>

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:59](https://github.com/System-B90/Bluz/blob/e82087d51f2769f8b338ee03029e86c8d2549994/ui/src/components/base/CalendarFilterProvider.tsx#L59)

***

### setShowMisconfigurations

> **setShowMisconfigurations**: `Dispatch`\<`SetStateAction`\<`boolean`\>\>

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:52](https://github.com/System-B90/Bluz/blob/e82087d51f2769f8b338ee03029e86c8d2549994/ui/src/components/base/CalendarFilterProvider.tsx#L52)

***

### setShowPAsFor

> **setShowPAsFor**: `Dispatch`\<`SetStateAction`\<[`PaTarget`](PaTarget.md)\>\>

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:40](https://github.com/System-B90/Bluz/blob/e82087d51f2769f8b338ee03029e86c8d2549994/ui/src/components/base/CalendarFilterProvider.tsx#L40)

***

### setShowPrayers

> **setShowPrayers**: `Dispatch`\<`SetStateAction`\<`boolean`\>\>

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:50](https://github.com/System-B90/Bluz/blob/e82087d51f2769f8b338ee03029e86c8d2549994/ui/src/components/base/CalendarFilterProvider.tsx#L50)

***

### setShowReservationsInEditMode

> **setShowReservationsInEditMode**: `Dispatch`\<`SetStateAction`\<`boolean`\>\>

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:83](https://github.com/System-B90/Bluz/blob/e82087d51f2769f8b338ee03029e86c8d2549994/ui/src/components/base/CalendarFilterProvider.tsx#L83)

The opt-in; meaningful only in week edit mode, reset on leaving it.

***

### setShowUnavailabilities

> **setShowUnavailabilities**: `Dispatch`\<`SetStateAction`\<`boolean`\>\>

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:72](https://github.com/System-B90/Bluz/blob/e82087d51f2769f8b338ee03029e86c8d2549994/ui/src/components/base/CalendarFilterProvider.tsx#L72)

***

### setShowUnstaffedOnly

> **setShowUnstaffedOnly**: `Dispatch`\<`SetStateAction`\<`boolean`\>\>

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:65](https://github.com/System-B90/Bluz/blob/e82087d51f2769f8b338ee03029e86c8d2549994/ui/src/components/base/CalendarFilterProvider.tsx#L65)

***

### setWeekEditMode

> **setWeekEditMode**: (`on`) => `void`

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:79](https://github.com/System-B90/Bluz/blob/e82087d51f2769f8b338ee03029e86c8d2549994/ui/src/components/base/CalendarFilterProvider.tsx#L79)

#### Parameters

##### on

`boolean`

#### Returns

`void`

***

### showHiveLessonIssues

> **showHiveLessonIssues**: `boolean`

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:58](https://github.com/System-B90/Bluz/blob/e82087d51f2769f8b338ee03029e86c8d2549994/ui/src/components/base/CalendarFilterProvider.tsx#L58)

Mark events whose Hive lesson is missing or will not reach their
shuffles (#1025). Off by default: a schedule still being built would be
all markers.

***

### showMisconfigurations

> **showMisconfigurations**: `boolean`

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:51](https://github.com/System-B90/Bluz/blob/e82087d51f2769f8b338ee03029e86c8d2549994/ui/src/components/base/CalendarFilterProvider.tsx#L51)

***

### showPAsFor

> **showPAsFor**: [`PaTarget`](PaTarget.md)

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:39](https://github.com/System-B90/Bluz/blob/e82087d51f2769f8b338ee03029e86c8d2549994/ui/src/components/base/CalendarFilterProvider.tsx#L39)

The פ"א view: off (`null`), every PA window (`"all"`), or the windows
of one instructor (their Hive id), dimming the slots they are busy in.

***

### showPrayers

> **showPrayers**: `boolean`

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:49](https://github.com/System-B90/Bluz/blob/e82087d51f2769f8b338ee03029e86c8d2549994/ui/src/components/base/CalendarFilterProvider.tsx#L49)

Tint the daily prayer windows and the Shabbat window (כניסת שבת → צאת
שבת, #996) light red, and show the hand-made prayer events. Off hides
all three.

***

### showReservations

> **showReservations**: `boolean`

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:81](https://github.com/System-B90/Bluz/blob/e82087d51f2769f8b338ee03029e86c8d2549994/ui/src/components/base/CalendarFilterProvider.tsx#L81)

Draw room reservations: always outside week edit mode, opt-in inside it.

***

### showUnavailabilities

> **showUnavailabilities**: `boolean`

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:71](https://github.com/System-B90/Bluz/blob/e82087d51f2769f8b338ee03029e86c8d2549994/ui/src/components/base/CalendarFilterProvider.tsx#L71)

Show staff unavailabilities (אי זמינות), in the day view's "אי
זמינויות" column. Off by default: they are planning context, not
schedule.

***

### showUnstaffedOnly

> **showUnstaffedOnly**: `boolean`

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:64](https://github.com/System-B90/Bluz/blob/e82087d51f2769f8b338ee03029e86c8d2549994/ui/src/components/base/CalendarFilterProvider.tsx#L64)

Show only events still missing a מבזר (#1029). Prayers and breaks never
take one, so they leave the calendar too.

***

### weekEditMode

> **weekEditMode**: `boolean`

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:78](https://github.com/System-B90/Bluz/blob/e82087d51f2769f8b338ee03029e86c8d2549994/ui/src/components/base/CalendarFilterProvider.tsx#L78)

Week edit mode: a working view for building the week. Room reservations
(שריון כיתה) become opt-in, instructor chips leave the tiles, and the
parked panel opens while it lasts.
