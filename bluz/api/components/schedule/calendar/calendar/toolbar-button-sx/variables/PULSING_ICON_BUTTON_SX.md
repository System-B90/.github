[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/calendar/toolbar-button-sx](../index.md) / PULSING\_ICON\_BUTTON\_SX

# Variable: PULSING\_ICON\_BUTTON\_SX

> `const` **PULSING\_ICON\_BUTTON\_SX**: `object`

Defined in: [ui/src/components/schedule/calendar/calendar/toolbar-button-sx.ts:11](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/schedule/calendar/calendar/toolbar-button-sx.ts#L11)

[CONTROL\_BUTTON\_SX](CONTROL_BUTTON_SX.md) plus the pulsing icon used by the fullscreen toggles.

## Type Declaration

### @keyframes pulse-expand

> `readonly` **@keyframes pulse-expand**: `object`

#### @keyframes pulse-expand.0%, 100%

> `readonly` **0%, 100%**: `object`

#### @keyframes pulse-expand.0%, 100%.transform

> `readonly` **transform**: `"scale(1)"` = `"scale(1)"`

#### @keyframes pulse-expand.50%

> `readonly` **50%**: `object`

#### @keyframes pulse-expand.50%.transform

> `readonly` **transform**: `"scale(1.25)"` = `"scale(1.25)"`

### &:active

> `readonly` **&:active**: `object`

#### &:active.transform

> `readonly` **transform**: `"scale(0.95)"` = `"scale(0.95)"`

### &:hover

> `readonly` **&:hover**: `object`

#### &:hover.color

> `readonly` **color**: `"primary.main"` = `"primary.main"`

#### &:hover .MuiSvgIcon-root

> `readonly` **&:hover .MuiSvgIcon-root**: `object`

#### &:hover .MuiSvgIcon-root.animation

> `readonly` **animation**: `"pulse-expand 1.2s infinite ease-in-out"` = `"pulse-expand 1.2s infinite ease-in-out"`

### transition

> `readonly` **transition**: `"all 0.2s ease-in-out"` = `"all 0.2s ease-in-out"`
