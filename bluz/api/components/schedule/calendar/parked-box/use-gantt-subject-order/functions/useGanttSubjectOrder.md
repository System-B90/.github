[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/parked-box/use-gantt-subject-order](../index.md) / useGanttSubjectOrder

# Function: useGanttSubjectOrder()

> **useGanttSubjectOrder**(`enabled`): `ReadonlyMap`\<`number`, `number`\>

Defined in: [ui/src/components/schedule/calendar/parked-box/use-gantt-subject-order.ts:13](https://github.com/System-B90/Bluz/blob/2fa23325da73d58527b069b0943f3bd1e838efee/ui/src/components/schedule/calendar/parked-box/use-gantt-subject-order.ts#L13)

Hive subject id → its position in the gantt linked to the viewed
iteration: the order of the syllabuses that carry it (#981). Fetched only
while `enabled`, so an empty box costs nothing. Without a gantt, groups fall
back to by-name.

## Parameters

### enabled

`boolean`

## Returns

`ReadonlyMap`\<`number`, `number`\>
