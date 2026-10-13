[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/student-pink-mode](../index.md) / isPinkModeAllowed

# Function: isPinkModeAllowed()

> **isPinkModeAllowed**(`clearance`, `studentPinkMode?`): `boolean`

Defined in: [ui/src/api-server/student-pink-mode.ts:10](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-server/student-pink-mode.ts#L10)

Whether a session gets the pink-mode toggle (#765). Staff always do;
students only when the deployment sets `BLUZ_STUDENT_PINK_MODE=true`.

Not a security boundary: it only hides a button. A student can still reach
pink through a theme already stored in their browser.

## Parameters

### clearance

`Clearance`

### studentPinkMode?

`string` \| `undefined`

## Returns

`boolean`
