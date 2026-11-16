[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/pa-coverage](../index.md) / paCoverage

# Function: paCoverage()

> **paCoverage**\<`E`\>(`instructorId`): [`PaCoverage`](../type-aliases/PaCoverage.md) \| `null`

Defined in: [ui/src/api-shared/pa-coverage.ts:74](https://github.com/System-B90/Bluz/blob/182d51c797407c7b0ea37986b1a45ab0e64c4df0/ui/src/api-shared/pa-coverage.ts#L74)

## Type Parameters

### E

`E` *extends* [`PaCoverageEvent`](../type-aliases/PaCoverageEvent.md)

## Parameters

### instructorId

The instructor.

#### attendees

(`event`) => `number`[]

#### events

readonly `E`[]

#### from

`number`

#### instructorId

`number`

#### studentIds

`ReadonlySet`\<`number`\>

#### talkMs

`number`

#### to

`number`

## Returns

[`PaCoverage`](../type-aliases/PaCoverage.md) \| `null`

The coverage, or null when the instructor has no students.
