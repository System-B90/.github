[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/base/DocumentPip](../index.md) / useDocumentPip

# Function: useDocumentPip()

> **useDocumentPip**(`__namedParameters`): `object`

Defined in: [ui/src/components/base/DocumentPip.tsx:104](https://github.com/System-B90/Bluz/blob/04ebae9cb334a01c6e7a55f885993f021e83cd92/ui/src/components/base/DocumentPip.tsx#L104)

Opens and tracks one Document PiP window. `open` must run inside a user
gesture (a click); the window closes on `close`, on unmount, or by the user.

## Parameters

### \_\_namedParameters

#### height

`number`

#### title

`string`

#### width

`number`

## Returns

`object`

### close

> **close**: () => `void` \| `undefined`

#### Returns

`void` \| `undefined`

### open

> **open**: () => `Promise`\<`void`\>

#### Returns

`Promise`\<`void`\>

### pipWindow

> **pipWindow**: `Window` \| `null`
