[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [components/gantt/curriculum-view/tabs/cut-preview-tab/UseCutPreview](../index.md) / useCutPreview

# Function: useCutPreview()

> **useCutPreview**(`curriculumId`): [`CutPreviewState`](../type-aliases/CutPreviewState.md)

Defined in: [ui/src/components/gantt/curriculum-view/tabs/cut-preview-tab/UseCutPreview.ts:17](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/gantt/curriculum-view/tabs/cut-preview-tab/UseCutPreview.ts#L17)

Fetches the dry-run cut preview for a curriculum. Refetches whenever the
curriculum id changes; both preview tabs share this hook so each mount gets
fresh occurrences after gantt edits.

## Parameters

### curriculumId

`string`

## Returns

[`CutPreviewState`](../type-aliases/CutPreviewState.md)
