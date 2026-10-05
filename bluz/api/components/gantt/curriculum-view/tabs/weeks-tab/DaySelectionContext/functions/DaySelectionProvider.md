[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [components/gantt/curriculum-view/tabs/weeks-tab/DaySelectionContext](../index.md) / DaySelectionProvider

# Function: DaySelectionProvider()

> **DaySelectionProvider**(`orderedDayIds`): `Element`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/weeks-tab/DaySelectionContext.tsx:40](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/components/gantt/curriculum-view/tabs/weeks-tab/DaySelectionContext.tsx#L40)

Selection state for the weeks grid's day cells. Lives above the rows so a
range can span weeks, and holds nothing but ids — the cells stay the owners
of their own values.

## Parameters

### orderedDayIds

Every day in the grid, in calendar order. Range
  selection is defined over this order, so it must match what is rendered.

#### children

`ReactNode`

#### orderedDayIds

`string`[]

## Returns

`Element`
