[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/student-hidden-words](../index.md) / scrubStudentText

# Function: scrubStudentText()

> **scrubStudentText**(`text`): `string`

Defined in: [ui/src/api-shared/student-hidden-words.ts:52](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/api-shared/student-hidden-words.ts#L52)

`text` with every hidden word removed, plus the brackets, separators and
spaces that removal leaves behind: `מתמטיקה (מתקדמים)` → `מתמטיקה`.
May return "" when the text was nothing but hidden words.

## Parameters

### text

`string`

## Returns

`string`
