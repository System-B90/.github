[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/app-onboarding/schedule/use-schedule-tours](../index.md) / useScheduleTours

# Function: useScheduleTours()

> **useScheduleTours**(`__namedParameters`): `void`

Defined in: [ui/src/components/app-onboarding/schedule/use-schedule-tours.tsx:22](https://github.com/System-B90/Bluz/blob/9da30d3fe7bc9583b86fb81afc4a7774c580c249/ui/src/components/app-onboarding/schedule/use-schedule-tours.tsx#L22)

Registers every schedule tutorial (#986) for as long as the screen is
mounted: the intro, which runs by itself on the first visit, and one tour
per task, run from the help panel or the palette.

Built in one `useMemo`, since `useTour` needs referentially stable tours, and
registered in `SCHEDULE_TUTORIAL_LIST` order, which is the order the help
panel lists them in.

## Parameters

### \_\_namedParameters

[`ScheduleTourDeps`](../../tours/types/type-aliases/ScheduleTourDeps.md)

## Returns

`void`
