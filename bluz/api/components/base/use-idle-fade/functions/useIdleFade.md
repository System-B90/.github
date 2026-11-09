[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/base/use-idle-fade](../index.md) / useIdleFade

# Function: useIdleFade()

> **useIdleFade**(`active`): `object`

Defined in: [ui/src/components/base/use-idle-fade.ts:21](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/components/base/use-idle-fade.ts#L21)

Fades floating chrome (the fullscreen exit button) once the user stops
moving, so it does not sit over the grid on a wall display. Any activity
brings it back; hovering or focusing it keeps it shown. Stays opaque while
`active` is false.

Opacity only, never `visibility`/`display`: the button stays clickable and
reachable by Tab, and Escape keeps working throughout.

Kept free of providers so the student bundle can import it (#656).

## Parameters

### active

`boolean`

## Returns

`object`

### @media (prefers-reduced-motion: reduce)

> `readonly` **@media (prefers-reduced-motion: reduce)**: `object`

#### @media (prefers-reduced-motion: reduce).transition

> `readonly` **transition**: `"none"` = `"none"`

### &:hover, &:focus-within

> `readonly` **&:hover, &:focus-within**: `object`

#### &:hover, &:focus-within.opacity

> `readonly` **opacity**: `1` = `1`

### opacity

> `readonly` **opacity**: `0` \| `1`

### transition

> `readonly` **transition**: `"opacity 0.4s ease"` = `"opacity 0.4s ease"`
