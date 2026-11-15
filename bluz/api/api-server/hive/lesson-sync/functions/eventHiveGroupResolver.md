[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/hive/lesson-sync](../index.md) / eventHiveGroupResolver

# Function: eventHiveGroupResolver()

> **eventHiveGroupResolver**(`courses`, `hiveClasses`): (`event`) => `Set`\<`number`\>

Defined in: [ui/src/api-server/hive/lesson-sync.ts:30](https://github.com/System-B90/Bluz/blob/d77dcf130db661461363a52910f62a34b3514ebd/ui/src/api-server/hive/lesson-sync.ts#L30)

Resolves events' Hive groups against one course list and group list.

## Parameters

### courses

`Pick`\<[`Course`](../../../../api-shared/types/course/type-aliases/Course.md), `"id"` \| `"name"` \| `"parentId"` \| `"hiveClassId"`\>[]

### hiveClasses

`Class`[]

## Returns

(`event`) => `Set`\<`number`\>
