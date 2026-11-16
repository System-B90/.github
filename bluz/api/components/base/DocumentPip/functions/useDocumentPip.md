[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/base/DocumentPip](../index.md) / useDocumentPip

# Function: useDocumentPip()

> **useDocumentPip**(`__namedParameters`): `object`

Defined in: [ui/src/components/base/DocumentPip.tsx:104](https://github.com/System-B90/Bluz/blob/182d51c797407c7b0ea37986b1a45ab0e64c4df0/ui/src/components/base/DocumentPip.tsx#L104)

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
