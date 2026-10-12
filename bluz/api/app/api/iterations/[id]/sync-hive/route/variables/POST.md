[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [app/api/iterations/\[id\]/sync-hive/route](../index.md) / POST

# Variable: POST

> `const` **POST**: `ServerApiIterationSyncHive`

Defined in: [ui/src/app/api/iterations/\[id\]/sync-hive/route.ts:25](https://github.com/System-B90/Bluz/blob/4bd90f164a3cfe171409116b1f28d79f80797dcd/ui/src/app/api/iterations/[id]/sync-hive/route.ts#L25)

Manually re-snapshot the Hive module/subject/room names for an iteration
(#379), rather than relying only on the snapshot taken at creation time.

Past iterations are rejected by the same read-only guard as every other
write: their snapshot is what keeps them readable once their Hive instance
is gone, and Hive ids are reused across runs, so re-syncing one would
overwrite history with a different Hive's names.
