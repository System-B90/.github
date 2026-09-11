[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/cut-breaks](../index.md) / insertBreaksForDay

# Function: insertBreaksForDay()

> **insertBreaksForDay**(`input`): [`BreakPassResult`](../type-aliases/BreakPassResult.md)

Defined in: [ui/src/api-shared/gantt/cut-breaks.ts:181](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/gantt/cut-breaks.ts#L181)

Insert breaks into a single day's slack.

Guarantees:
- The day never grows: total inserted minutes never exceed the trailing
  slack, so the last item still ends at or before `dayEndMinutes`.
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
