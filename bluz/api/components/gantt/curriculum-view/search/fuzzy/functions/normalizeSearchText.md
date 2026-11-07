[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/gantt/curriculum-view/search/fuzzy](../index.md) / normalizeSearchText

# Function: normalizeSearchText()

> **normalizeSearchText**(`text`): `string`

Defined in: [ui/src/components/gantt/curriculum-view/search/fuzzy.ts:10](https://github.com/System-B90/Bluz/blob/1b02178048002eee34d502b2e3e2a402e1b9c9c0/ui/src/components/gantt/curriculum-view/search/fuzzy.ts#L10)

Normalize text for fuzzy matching: lowercase, strip quotation marks and
collapse whitespace. Quote stripping is what lets the search shrug off the
Hebrew gershayim/geresh that pepper module and event names.

## Parameters

### text

`string`

## Returns

`string`
