[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/gantt/curriculum-view/search/fuzzy](../index.md) / normalizeSearchText

# Function: normalizeSearchText()

> **normalizeSearchText**(`text`): `string`

Defined in: [ui/src/components/gantt/curriculum-view/search/fuzzy.ts:10](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/components/gantt/curriculum-view/search/fuzzy.ts#L10)

Normalize text for fuzzy matching: lowercase, strip quotation marks and
collapse whitespace. Quote stripping is what lets the search shrug off the
Hebrew gershayim/geresh that pepper module and event names.

## Parameters

### text

`string`

## Returns

`string`
