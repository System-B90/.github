[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/hive/lesson-sync](../index.md) / planLessonRules

# Function: planLessonRules()

> **planLessonRules**(`desired`, `existing`): [`LessonRulePlan`](../type-aliases/LessonRulePlan.md)

Defined in: [ui/src/api-server/hive/lesson-sync.ts:57](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/hive/lesson-sync.ts#L57)

Diffs the shuffle→queue mapping an event wants against the rules a Hive
lesson already has.

Bluz owns every rule on a lesson it manages, so anything it does not
recognise is removed: a rule for a group that is no longer on the event, a
nested rule (Bluz never builds hierarchies), and any duplicate rule for a
group. Kept pure so the reconciliation is testable without a Hive.

## Parameters

### desired

`Map`\<`number`, `number`\>

Hive student-group id → Hive queue id.

### existing

`LessonRule`[]

The lesson's current rules, as Hive returns them.

## Returns

[`LessonRulePlan`](../type-aliases/LessonRulePlan.md)

The rules to create, re-point, and delete.
