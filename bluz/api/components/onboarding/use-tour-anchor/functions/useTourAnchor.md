[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/onboarding/use-tour-anchor](../index.md) / useTourAnchor

# Function: useTourAnchor()

> **useTourAnchor**\<`T`\>(`id`): (`element`) => (() => `void`) \| `undefined`

Defined in: [ui/src/components/onboarding/use-tour-anchor.ts:19](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/onboarding/use-tour-anchor.ts#L19)

Marks an element as a spotlight target.

```tsx
<Tabs ref={useTourAnchor("gantt.tabs")} />
```

The returned ref callback registers on mount and un-registers on unmount, so
a tour always spotlights whatever is on screen right now — and a component
that is never rendered simply has no anchor, which is what lets steps be
marked `optional` and skipped.

## Type Parameters

### T

`T` *extends* `HTMLElement` = `HTMLElement`

## Parameters

### id

`string`

## Returns

(`element`) => (() => `void`) \| `undefined`
