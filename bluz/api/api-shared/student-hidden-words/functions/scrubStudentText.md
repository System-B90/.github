[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/student-hidden-words](../index.md) / scrubStudentText

# Function: scrubStudentText()

> **scrubStudentText**(`text`): `string`

Defined in: [ui/src/api-shared/student-hidden-words.ts:52](https://github.com/System-B90/Bluz/blob/90114c31e10132d84c8c3bab079c25588fbe0459/ui/src/api-shared/student-hidden-words.ts#L52)

`text` with every hidden word removed, plus the brackets, separators and
spaces that removal leaves behind: `מתמטיקה (מתקדמים)` → `מתמטיקה`.
May return "" when the text was nothing but hidden words.

## Parameters

### text

`string`

## Returns

`string`
