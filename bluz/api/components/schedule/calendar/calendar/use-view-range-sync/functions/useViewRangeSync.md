[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/calendar/use-view-range-sync](../index.md) / useViewRangeSync

# Function: useViewRangeSync()

> **useViewRangeSync**(`__namedParameters`): \[`Date`, `Dispatch`\<`SetStateAction`\<`Date`\>\>\]

Defined in: [ui/src/components/schedule/calendar/calendar/use-view-range-sync.ts:20](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/components/schedule/calendar/calendar/use-view-range-sync.ts#L20)

Two-way sync between the calendar view's date and the provider's range.

The view owns `currentDate` and pushes its range into the context; a range
set from outside (a snapshot restore, #653) must move the view. Telling the
two apart by "is the context range inside the view's range" alone made a
loop: on remount (back from the gantt) the view started at today while the
provider still held the last viewed week, so each effect undid the other
every render and the grid flickered between the two weeks until a reload.

Now the view starts from the provider's range when it has one, and an echo
of the range the view pushed itself is never treated as an outside change.

## Parameters

### \_\_namedParameters

#### setEndDate

`Dispatch`\<`SetStateAction`\<`Date` \| `undefined`\>\>

#### setStartDate

`Dispatch`\<`SetStateAction`\<`Date` \| `undefined`\>\>

#### startDate

`Date` \| `undefined`

#### view

`View`

## Returns

\[`Date`, `Dispatch`\<`SetStateAction`\<`Date`\>\>\]
