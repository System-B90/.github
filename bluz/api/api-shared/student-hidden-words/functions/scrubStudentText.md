[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/student-hidden-words](../index.md) / scrubStudentText

# Function: scrubStudentText()

> **scrubStudentText**(`text`): `string`

Defined in: [ui/src/api-shared/student-hidden-words.ts:52](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-shared/student-hidden-words.ts#L52)

`text` with every hidden word removed, plus the brackets, separators and
spaces that removal leaves behind: `מתמטיקה (מתקדמים)` → `מתמטיקה`.
May return "" when the text was nothing but hidden words.

## Parameters

### text

`string`

## Returns

`string`
