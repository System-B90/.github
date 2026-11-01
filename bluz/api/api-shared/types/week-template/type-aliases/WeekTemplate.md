[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/week-template](../index.md) / WeekTemplate

# Type Alias: WeekTemplate

> **WeekTemplate** = [`WeekTemplateTimes`](WeekTemplateTimes.md) & `object`

Defined in: [ui/src/api-shared/types/week-template.ts:59](https://github.com/System-B90/Bluz/blob/2fa23325da73d58527b069b0943f3bd1e838efee/ui/src/api-shared/types/week-template.ts#L59)

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
