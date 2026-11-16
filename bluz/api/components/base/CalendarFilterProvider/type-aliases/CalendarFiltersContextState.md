[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/base/CalendarFilterProvider](../index.md) / CalendarFiltersContextState

# Type Alias: CalendarFiltersContextState

> **CalendarFiltersContextState** = `object`

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:29](https://github.com/System-B90/Bluz/blob/9da30d3fe7bc9583b86fb81afc4a7774c580c249/ui/src/components/base/CalendarFilterProvider.tsx#L29)

## Properties

### clearFilters

> **clearFilters**: () => `void`

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:95](https://github.com/System-B90/Bluz/blob/9da30d3fe7bc9583b86fb81afc4a7774c580c249/ui/src/components/base/CalendarFilterProvider.tsx#L95)

Resets every filter to its default, showing the full calendar again.

#### Returns

`void`

***

### default

> **default**: `boolean`

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:30](https://github.com/System-B90/Bluz/blob/9da30d3fe7bc9583b86fb81afc4a7774c580c249/ui/src/components/base/CalendarFilterProvider.tsx#L30)

***

### eventFilteredOpacity

> **eventFilteredOpacity**: (`event`) => `number`

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:90](https://github.com/System-B90/Bluz/blob/9da30d3fe7bc9583b86fb81afc4a7774c580c249/ui/src/components/base/CalendarFilterProvider.tsx#L90)

#### Parameters

##### event

[`Event`](../../../../api-shared/types/event/type-aliases/Event.md)

#### Returns

`number`

***

### filteredCourses

> **filteredCourses**: [`CourseId`](../../../../api-shared/types/course/type-aliases/CourseId.md)[]

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:33](https://github.com/System-B90/Bluz/blob/9da30d3fe7bc9583b86fb81afc4a7774c580c249/ui/src/components/base/CalendarFilterProvider.tsx#L33)

***

### filteredInstructors

> **filteredInstructors**: `number`[]

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:31](https://github.com/System-B90/Bluz/blob/9da30d3fe7bc9583b86fb81afc4a7774c580c249/ui/src/components/base/CalendarFilterProvider.tsx#L31)

***

### filteredRooms

> **filteredRooms**: `string`[]

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:43](https://github.com/System-B90/Bluz/blob/9da30d3fe7bc9583b86fb81afc4a7774c580c249/ui/src/components/base/CalendarFilterProvider.tsx#L43)

Room resource keys to show; empty shows every room (#1018).

***

### hasActiveFilters

> **hasActiveFilters**: `boolean`

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:93](https://github.com/System-B90/Bluz/blob/9da30d3fe7bc9583b86fb81afc4a7774c580c249/ui/src/components/base/CalendarFilterProvider.tsx#L93)

True when any filter is narrowing the calendar.

***

### setFilteredCourses

> **setFilteredCourses**: `Dispatch`\<`SetStateAction`\<[`CourseId`](../../../../api-shared/types/course/type-aliases/CourseId.md)[]\>\>

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:34](https://github.com/System-B90/Bluz/blob/9da30d3fe7bc9583b86fb81afc4a7774c580c249/ui/src/components/base/CalendarFilterProvider.tsx#L34)

***

### setFilteredInstructors

> **setFilteredInstructors**: `Dispatch`\<`SetStateAction`\<`number`[]\>\>

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:32](https://github.com/System-B90/Bluz/blob/9da30d3fe7bc9583b86fb81afc4a7774c580c249/ui/src/components/base/CalendarFilterProvider.tsx#L32)

***

### setFilteredRooms

> **setFilteredRooms**: `Dispatch`\<`SetStateAction`\<`string`[]\>\>

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:44](https://github.com/System-B90/Bluz/blob/9da30d3fe7bc9583b86fb81afc4a7774c580c249/ui/src/components/base/CalendarFilterProvider.tsx#L44)

***

### setShowHiveLessonIssues

> **setShowHiveLessonIssues**: `Dispatch`\<`SetStateAction`\<`boolean`\>\>

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:60](https://github.com/System-B90/Bluz/blob/9da30d3fe7bc9583b86fb81afc4a7774c580c249/ui/src/components/base/CalendarFilterProvider.tsx#L60)

***

### setShowInstructorsInEditMode

> **setShowInstructorsInEditMode**: `Dispatch`\<`SetStateAction`\<`boolean`\>\>

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:88](https://github.com/System-B90/Bluz/blob/9da30d3fe7bc9583b86fb81afc4a7774c580c249/ui/src/components/base/CalendarFilterProvider.tsx#L88)

The opt-in; meaningful only in week edit mode, reset on leaving it.

***

### setShowMisconfigurations

> **setShowMisconfigurations**: `Dispatch`\<`SetStateAction`\<`boolean`\>\>

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:53](https://github.com/System-B90/Bluz/blob/9da30d3fe7bc9583b86fb81afc4a7774c580c249/ui/src/components/base/CalendarFilterProvider.tsx#L53)

***

### setShowPAsFor

> **setShowPAsFor**: `Dispatch`\<`SetStateAction`\<[`PaTarget`](PaTarget.md)\>\>

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:41](https://github.com/System-B90/Bluz/blob/9da30d3fe7bc9583b86fb81afc4a7774c580c249/ui/src/components/base/CalendarFilterProvider.tsx#L41)

***

### setShowPrayers

> **setShowPrayers**: `Dispatch`\<`SetStateAction`\<`boolean`\>\>

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:51](https://github.com/System-B90/Bluz/blob/9da30d3fe7bc9583b86fb81afc4a7774c580c249/ui/src/components/base/CalendarFilterProvider.tsx#L51)

***

### setShowReservationsInEditMode

> **setShowReservationsInEditMode**: `Dispatch`\<`SetStateAction`\<`boolean`\>\>

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:84](https://github.com/System-B90/Bluz/blob/9da30d3fe7bc9583b86fb81afc4a7774c580c249/ui/src/components/base/CalendarFilterProvider.tsx#L84)

The opt-in; meaningful only in week edit mode, reset on leaving it.

***

### setShowUnavailabilities

> **setShowUnavailabilities**: `Dispatch`\<`SetStateAction`\<`boolean`\>\>

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:73](https://github.com/System-B90/Bluz/blob/9da30d3fe7bc9583b86fb81afc4a7774c580c249/ui/src/components/base/CalendarFilterProvider.tsx#L73)

***

### setShowUnstaffedOnly

> **setShowUnstaffedOnly**: `Dispatch`\<`SetStateAction`\<`boolean`\>\>

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:66](https://github.com/System-B90/Bluz/blob/9da30d3fe7bc9583b86fb81afc4a7774c580c249/ui/src/components/base/CalendarFilterProvider.tsx#L66)

***

### setWeekEditMode

> **setWeekEditMode**: (`on`) => `void`

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:80](https://github.com/System-B90/Bluz/blob/9da30d3fe7bc9583b86fb81afc4a7774c580c249/ui/src/components/base/CalendarFilterProvider.tsx#L80)

#### Parameters

##### on

`boolean`

#### Returns

`void`

***

### showHiveLessonIssues

> **showHiveLessonIssues**: `boolean`

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:59](https://github.com/System-B90/Bluz/blob/9da30d3fe7bc9583b86fb81afc4a7774c580c249/ui/src/components/base/CalendarFilterProvider.tsx#L59)

Mark events whose Hive lesson is missing or will not reach their
shuffles (#1025). Off by default: a schedule still being built would be
all markers.

***

### showInstructors

> **showInstructors**: `boolean`

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:86](https://github.com/System-B90/Bluz/blob/9da30d3fe7bc9583b86fb81afc4a7774c580c249/ui/src/components/base/CalendarFilterProvider.tsx#L86)

Draw instructor chips on tiles: always outside week edit mode, opt-in inside it.

***

### showMisconfigurations

> **showMisconfigurations**: `boolean`

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:52](https://github.com/System-B90/Bluz/blob/9da30d3fe7bc9583b86fb81afc4a7774c580c249/ui/src/components/base/CalendarFilterProvider.tsx#L52)

***

### showPAsFor

> **showPAsFor**: [`PaTarget`](PaTarget.md)

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:40](https://github.com/System-B90/Bluz/blob/9da30d3fe7bc9583b86fb81afc4a7774c580c249/ui/src/components/base/CalendarFilterProvider.tsx#L40)

The פ"א view: off (`null`), one instructor's windows (their Hive id),
dimming the slots they are busy in — the default, see
`usePaWindowsToggle` — or every PA window with no dimming (`"all"`).

***

### showPrayers

> **showPrayers**: `boolean`

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:50](https://github.com/System-B90/Bluz/blob/9da30d3fe7bc9583b86fb81afc4a7774c580c249/ui/src/components/base/CalendarFilterProvider.tsx#L50)

Tint the daily prayer windows and the Shabbat window (כניסת שבת → צאת
שבת, #996) light red, and show the hand-made prayer events. Off hides
all three.

***

### showReservations

> **showReservations**: `boolean`

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:82](https://github.com/System-B90/Bluz/blob/9da30d3fe7bc9583b86fb81afc4a7774c580c249/ui/src/components/base/CalendarFilterProvider.tsx#L82)

Draw room reservations: always outside week edit mode, opt-in inside it.

***

### showUnavailabilities

> **showUnavailabilities**: `boolean`

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:72](https://github.com/System-B90/Bluz/blob/9da30d3fe7bc9583b86fb81afc4a7774c580c249/ui/src/components/base/CalendarFilterProvider.tsx#L72)

Show staff unavailabilities (אי זמינות), in the day view's "אי
זמינויות" column. Off by default: they are planning context, not
schedule.

***

### showUnstaffedOnly

> **showUnstaffedOnly**: `boolean`

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:65](https://github.com/System-B90/Bluz/blob/9da30d3fe7bc9583b86fb81afc4a7774c580c249/ui/src/components/base/CalendarFilterProvider.tsx#L65)

Show only events still missing a מבזר (#1029). Prayers and breaks never
take one, so they leave the calendar too.

***

### weekEditMode

> **weekEditMode**: `boolean`

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:79](https://github.com/System-B90/Bluz/blob/9da30d3fe7bc9583b86fb81afc4a7774c580c249/ui/src/components/base/CalendarFilterProvider.tsx#L79)

Week edit mode: a working view for building the week. Room reservations
(שריון כיתה) become opt-in, instructor chips leave the tiles, and the
parked panel opens while it lasts.
