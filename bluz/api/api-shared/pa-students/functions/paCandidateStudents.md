[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/pa-students](../index.md) / paCandidateStudents

# Function: paCandidateStudents()

> **paCandidateStudents**(`instructorId`, `users`, `eventGroups`): `CourseUser`[]

Defined in: [ui/src/api-shared/pa-students.ts:17](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/api-shared/pa-students.ts#L17)

An instructor's students (Hive mentees) who attend an event, i.e. whom they
could take out of it for a personal talk (פ"א).

A mentee is listed on either side in Hive (`mentees` on the instructor,
`mentor` on the student), so both count. A student attends when they are in
one of the event's Hive student groups, by the group's `users` or their own
`classes`.

## Parameters

### instructorId

`number`

The instructor whose students are wanted.

### users

`Record`\<`number`, `CourseUser`\>

Every Hive user, by id.

### eventGroups

`Pick`\<`Class`, `"id"` \| `"users"`\>[]

The Hive groups the event reaches (`resolveEventHiveGroups`).

## Returns

`CourseUser`[]

Those students, in no particular order.
