[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/base/IterationProvider](../index.md) / IterationProvider

# Function: IterationProvider()

> **IterationProvider**(`__namedParameters`): `Element`

Defined in: [ui/src/components/base/IterationProvider.tsx:55](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/base/IterationProvider.tsx#L55)

Owns the iteration the whole app is scoped to. This state used to live in
`CalendarProvider`, but everything backed by the iteration's database —
settings included — has to read it, and those providers mount above the
calendar. It therefore sits at the top of the post-auth tree instead.

Mirrored to a `?it=` URL param (`ITERATION_QUERY_PARAM`) so a refresh or a
shared link keeps the selected iteration instead of silently falling back
to "current" (#456). Backfilled with the current iteration's id once known
if the param is missing, so the param is always present.

## Parameters

### \_\_namedParameters

#### children

`ReactNode`

## Returns

`Element`
