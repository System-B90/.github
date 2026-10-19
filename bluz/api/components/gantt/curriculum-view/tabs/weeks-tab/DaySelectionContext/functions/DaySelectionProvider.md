[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [components/gantt/curriculum-view/tabs/weeks-tab/DaySelectionContext](../index.md) / DaySelectionProvider

# Function: DaySelectionProvider()

> **DaySelectionProvider**(`orderedDayIds`): `Element`

Defined in: [ui/src/components/gantt/curriculum-view/tabs/weeks-tab/DaySelectionContext.tsx:47](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/components/gantt/curriculum-view/tabs/weeks-tab/DaySelectionContext.tsx#L47)

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
