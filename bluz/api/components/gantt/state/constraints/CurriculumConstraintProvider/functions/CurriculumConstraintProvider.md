[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/gantt/state/constraints/CurriculumConstraintProvider](../index.md) / CurriculumConstraintProvider

# Function: CurriculumConstraintProvider()

> **CurriculumConstraintProvider**(`__namedParameters`): `Element`

Defined in: [ui/src/components/gantt/state/constraints/CurriculumConstraintProvider.tsx:41](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/components/gantt/state/constraints/CurriculumConstraintProvider.tsx#L41)

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
