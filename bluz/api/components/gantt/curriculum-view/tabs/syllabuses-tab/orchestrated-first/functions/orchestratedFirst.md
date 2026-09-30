[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [components/gantt/curriculum-view/tabs/syllabuses-tab/orchestrated-first](../index.md) / orchestratedFirst

# Function: orchestratedFirst()

> **orchestratedFirst**\<`TId`\>(`syllabusIds`, `userId`, `state`): `TId`[]

Defined in: [ui/src/components/gantt/curriculum-view/tabs/syllabuses-tab/orchestrated-first.ts:27](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/components/gantt/curriculum-view/tabs/syllabuses-tab/orchestrated-first.ts#L27)

Stable partition: syllabuses the user orchestrates first, each group keeping
its existing order (#748). Returns the input array untouched when nothing moves.

## Type Parameters

### TId

`TId` *extends* `string`

## Parameters

### syllabusIds

`TId`[]

### userId

`number` \| `null` \| `undefined`

### state

`OrchestrationState`

## Returns

`TId`[]
