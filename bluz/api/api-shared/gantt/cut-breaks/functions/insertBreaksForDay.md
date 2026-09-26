[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/cut-breaks](../index.md) / insertBreaksForDay

# Function: insertBreaksForDay()

> **insertBreaksForDay**(`input`): [`BreakPassResult`](../type-aliases/BreakPassResult.md)

Defined in: [ui/src/api-shared/gantt/cut-breaks.ts:207](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/cut-breaks.ts#L207)

Insert breaks into a single day's slack.

Guarantees:
- The day never grows: inserted minutes never exceed the slack of the
  segment they sit in (the gap up to the next pinned meal, or to
  `dayEndMinutes` for the last segment), so no item is shifted into a
  pinned meal and the last item still ends at or before `dayEndMinutes`.
- Higher-priority break kinds are satisfied first; when slack runs out the
  remaining candidates are dropped rather than shortened below their
  `minimumMinutes`.
- Leftover slack is grown into the breaks that already exist (largest
  priority first, capped by `maximumMinutes`) instead of being left as one
  long empty tail — and never grown past `implicitBreakCeilingMinutes`.

## Parameters

### input

[`BreakPassInput`](../type-aliases/BreakPassInput.md)

## Returns

[`BreakPassResult`](../type-aliases/BreakPassResult.md)
