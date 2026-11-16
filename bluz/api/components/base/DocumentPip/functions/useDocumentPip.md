[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/base/DocumentPip](../index.md) / useDocumentPip

# Function: useDocumentPip()

> **useDocumentPip**(`__namedParameters`): `object`

Defined in: [ui/src/components/base/DocumentPip.tsx:104](https://github.com/System-B90/Bluz/blob/9da30d3fe7bc9583b86fb81afc4a7774c580c249/ui/src/components/base/DocumentPip.tsx#L104)

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
