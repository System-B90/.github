[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/student-pink-mode](../index.md) / isPinkModeAllowed

# Function: isPinkModeAllowed()

> **isPinkModeAllowed**(`clearance`, `studentPinkMode?`): `boolean`

Defined in: [ui/src/api-server/student-pink-mode.ts:10](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-server/student-pink-mode.ts#L10)

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
