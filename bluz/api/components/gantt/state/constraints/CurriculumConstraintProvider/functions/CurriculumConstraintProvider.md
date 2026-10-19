[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/gantt/state/constraints/CurriculumConstraintProvider](../index.md) / CurriculumConstraintProvider

# Function: CurriculumConstraintProvider()

> **CurriculumConstraintProvider**(`__namedParameters`): `Element`

Defined in: [ui/src/components/gantt/state/constraints/CurriculumConstraintProvider.tsx:40](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/components/gantt/state/constraints/CurriculumConstraintProvider.tsx#L40)

Loads every constraint of a curriculum once and resolves them per event,
for anything that reasons about weekdays: recurrence echoes, student load,
occurrence counts, violations. Mount once per open curriculum.

## Parameters

### \_\_namedParameters

#### children

`ReactNode`

#### curriculumId

`string`

## Returns

`Element`
