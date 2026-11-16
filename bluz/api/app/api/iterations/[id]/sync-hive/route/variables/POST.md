[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [app/api/iterations/\[id\]/sync-hive/route](../index.md) / POST

# Variable: POST

> `const` **POST**: `ServerApiIterationSyncHive`

Defined in: [ui/src/app/api/iterations/\[id\]/sync-hive/route.ts:27](https://github.com/System-B90/Bluz/blob/182d51c797407c7b0ea37986b1a45ab0e64c4df0/ui/src/app/api/iterations/[id]/sync-hive/route.ts#L27)

Manually re-snapshot the Hive module/subject/room names for an iteration
(#379), rather than relying only on the snapshot taken at creation time.

Past iterations are rejected by the same read-only guard as every other
write: their snapshot is what keeps them readable once their Hive instance
is gone, and Hive ids are reused across runs, so re-syncing one would
overwrite history with a different Hive's names.
