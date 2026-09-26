[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [components/gantt/curriculum-view/tabs/cut-preview-tab/PreviewShell](../index.md) / renderPreviewBlockers

# Function: renderPreviewBlockers()

> **renderPreviewBlockers**(`preview`): `ReactNode`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/cut-preview-tab/PreviewShell.tsx:93](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/gantt/curriculum-view/tabs/cut-preview-tab/PreviewShell.tsx#L93)

Renders the non-ready states of a cut preview (loading, request error,
validation failure). Returns null when the preview holds usable data, so a
tab can `if (blocked) return blocked;` before rendering its own body.

## Parameters

### preview

[`CutPreviewState`](../../UseCutPreview/type-aliases/CutPreviewState.md)

## Returns

`ReactNode`
