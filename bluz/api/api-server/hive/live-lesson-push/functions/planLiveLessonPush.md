[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/hive/live-lesson-push](../index.md) / planLiveLessonPush

# Function: planLiveLessonPush()

> **planLiveLessonPush**(`change`, `opened`, `heldElsewhere`): [`LiveLessonPlan`](../type-aliases/LiveLessonPlan.md)

Defined in: [ui/src/api-server/hive/live-lesson-push.ts:94](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/api-server/hive/live-lesson-push.ts#L94)

Decides which groups an edit touches. Kept pure so it is testable without
a Hive.

Re-assigning resets every student of the group to where the lesson's
rules (in Hive) send them, so it is done only where something changed: a
group new to the event, or a new lesson. Renaming a running event moves
nobody. Only groups Bluz actually assigned (the ledger) are cleared, and
never one another running event holds.

## Parameters

### change

[`LiveLessonChange`](../type-aliases/LiveLessonChange.md)

The edit.

### opened

`Pick`\<[`HiveLessonActivation`](../../../../api-shared/types/hive-activation/type-aliases/HiveLessonActivation.md), `"hiveClassId"` \| `"lessonId"`\>[]

The ledger rows of the occurrence(s) being edited.

### heldElsewhere

`Set`\<`number`\>

Groups another live event has opened.

## Returns

[`LiveLessonPlan`](../type-aliases/LiveLessonPlan.md)

The groups to assign and to close.
