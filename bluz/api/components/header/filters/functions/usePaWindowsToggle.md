[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/header/filters](../index.md) / usePaWindowsToggle

# Function: usePaWindowsToggle()

> **usePaWindowsToggle**(): `object`

Defined in: [ui/src/components/header/filters.tsx:47](https://github.com/System-B90/Bluz/blob/182d51c797407c7b0ea37986b1a45ab0e64c4df0/ui/src/components/header/filters.tsx#L47)

The פ"א view toggle, in the main toolbar. A click shows one person's PA
windows, dimming the slots they are busy in: the single filtered
instructor, else the signed-in user. The button's right-click menu
(`PaWindowsButton`) picks another target, or every window ("all").

## Returns

### label

> **label**: `string`

### on

> **on**: `boolean`

### setTarget

> **setTarget**: (`target`) => `void`

#### Parameters

##### target

[`PaTarget`](../../../base/CalendarFilterProvider/type-aliases/PaTarget.md)

#### Returns

`void`

### target

> **target**: [`PaTarget`](../../../base/CalendarFilterProvider/type-aliases/PaTarget.md)

### toggle

> **toggle**: () => `void`

#### Returns

`void`

### userId

> **userId**: `number` \| `null`

The signed-in user's Hive id, when they have one.
