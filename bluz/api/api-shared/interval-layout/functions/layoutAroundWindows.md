[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/interval-layout](../index.md) / layoutAroundWindows

# Function: layoutAroundWindows()

> **layoutAroundWindows**(`start`, `workingMs`, `windows`, `options?`): [`Interval`](../type-aliases/Interval.md)[]

Defined in: [ui/src/api-shared/interval-layout.ts:72](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/interval-layout.ts#L72)

Lays `workingMs` of continuous work starting at `start`, stepping over every
window in its path.

Invariants callers rely on:
- the returned segments are non-empty, ordered and non-overlapping;
- their lengths sum to exactly `workingMs` — the amount of work is never
  changed by the windows, only redistributed;
- a start that lands inside a window is pushed to that window's end.

## Parameters

### start

`number`

Epoch ms the work begins at.

### workingMs

`number`

Net working length, excluding any window it steps over.

### windows

`Iterable`\<[`Interval`](../type-aliases/Interval.md)\>

Blocked windows (any order; overlaps are fine).

### options?

[`LayoutOptions`](../type-aliases/LayoutOptions.md) = `{}`

## Returns

[`Interval`](../type-aliases/Interval.md)[]

One segment per piece of the run — a single segment when nothing
         was in the way.

## Example

```typescript
// 4h of work from 09:00 over a 12:00-12:30 break → 09:00-12:00, 12:30-13:30
layoutAroundWindows(t("09:00"), 4 * 60 * 60_000, [breakWindow]);
```
