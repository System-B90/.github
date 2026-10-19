[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/week-template](../index.md) / WeekTemplate

# Type Alias: WeekTemplate

> **WeekTemplate** = [`WeekTemplateTimes`](WeekTemplateTimes.md) & `object`

Defined in: [ui/src/api-shared/types/week-template.ts:59](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/api-shared/types/week-template.ts#L59)

A template's metadata. Its events live in their own collection.

## Type Declaration

### createdAt

> **createdAt**: `string`

### eventCount

> **eventCount**: `number`

### id

> **id**: [`WeekTemplateId`](WeekTemplateId.md)

### isDefault

> **isDefault**: `boolean`

Used when a week is cut without picking a template. At most one.

### name

> **name**: `string`

### updatedAt

> **updatedAt**: `string`

### updatedBy?

> `optional` **updatedBy?**: `string`
