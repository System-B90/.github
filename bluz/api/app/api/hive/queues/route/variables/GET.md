[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [app/api/hive/queues/route](../index.md) / GET

# Variable: GET

> `const` **GET**: `ServerApiHiveQueuesGet`

Defined in: [ui/src/app/api/hive/queues/route.ts:23](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/app/api/hive/queues/route.ts#L23)

GET /api/hive/queues?module=<id> — the queues of one Hive module, for the
event dialog's per-shuffle queue picker. Module-scoped by design: Hive
rejects user queues on a lesson rule, so an unscoped list would offer
choices that cannot be saved.
