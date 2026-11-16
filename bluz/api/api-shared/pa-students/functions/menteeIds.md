[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/pa-students](../index.md) / menteeIds

# Function: menteeIds()

> **menteeIds**(`instructorId`, `users`): `Set`\<`number`\>

Defined in: [ui/src/api-shared/pa-students.ts:12](https://github.com/System-B90/Bluz/blob/182d51c797407c7b0ea37986b1a45ab0e64c4df0/ui/src/api-shared/pa-students.ts#L12)

An instructor's students (Hive mentees). A mentee is listed on either side
in Hive (`mentees` on the instructor, `mentor` on the student), so both
count.

## Parameters

### instructorId

`number`

The instructor whose students are wanted.

### users

`Record`\<`number`, `CourseUser`\>

Every Hive user, by id.

## Returns

`Set`\<`number`\>

Those students' ids, in no particular order.
