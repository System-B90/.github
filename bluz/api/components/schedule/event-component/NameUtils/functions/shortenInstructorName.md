[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/schedule/event-component/NameUtils](../index.md) / shortenInstructorName

# Function: shortenInstructorName()

> **shortenInstructorName**(`fullName`, `allInstructors`): `string`

Defined in: [ui/src/components/schedule/event-component/NameUtils.ts:16](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/components/schedule/event-component/NameUtils.ts#L16)

Shortens an instructor display name to their first name.
Differentiates instructors with the same first name by appending the minimum
necessary letters from their last name.

## Parameters

### fullName

`string`

The target instructor's full name.

### allInstructors

readonly `string`[]

Array of all instructor names to resolve collisions.

## Returns

`string`

The uniquely shortened name.

## Example

```ts
shortenInstructorName("אבי כהן", allNames) // "אבי כ"
shortenInstructorName("אבי כץ", allNames)  // "אבי כץ"
shortenInstructorName("איש חוץ", allNames) // "איש חוץ"
```
