[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/db-week-templates](../../../index.md) / [DbWeekTemplates](../index.md) / resolve

# Variable: resolve

> `const` **resolve**: (`id?`) => `Promise`\<[`WeekTemplate`](../../../../../api-shared/types/week-template/type-aliases/WeekTemplate.md) \| `null`\> = `resolveTemplate`

Defined in: [ui/src/api-server/db-week-templates.ts:309](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-server/db-week-templates.ts#L309)

The template a cut uses: the one asked for, else the default. Null only
when no template exists at all, which the seed makes unreachable in
practice.

## Parameters

### id?

`string`

## Returns

`Promise`\<[`WeekTemplate`](../../../../../api-shared/types/week-template/type-aliases/WeekTemplate.md) \| `null`\>
