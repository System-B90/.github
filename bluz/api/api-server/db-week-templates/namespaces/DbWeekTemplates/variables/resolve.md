[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/db-week-templates](../../../index.md) / [DbWeekTemplates](../index.md) / resolve

# Variable: resolve

> `const` **resolve**: (`id?`) => `Promise`\<[`WeekTemplate`](../../../../../api-shared/types/week-template/type-aliases/WeekTemplate.md) \| `null`\> = `resolveTemplate`

Defined in: [ui/src/api-server/db-week-templates.ts:332](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-server/db-week-templates.ts#L332)

The template a cut uses: the one asked for, else the default. Null only
when no template exists at all, which the seed makes unreachable in
practice.

## Parameters

### id?

`string`

## Returns

`Promise`\<[`WeekTemplate`](../../../../../api-shared/types/week-template/type-aliases/WeekTemplate.md) \| `null`\>
