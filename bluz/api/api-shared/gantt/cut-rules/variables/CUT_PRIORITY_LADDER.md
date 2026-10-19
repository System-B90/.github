[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/cut-rules](../index.md) / CUT\_PRIORITY\_LADDER

# Variable: CUT\_PRIORITY\_LADDER

> `const` **CUT\_PRIORITY\_LADDER**: `ReadonlyArray`\<\{ `description`: `string`; `rule`: `string`; \}\>

Defined in: [ui/src/api-shared/gantt/cut-rules.ts:422](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/api-shared/gantt/cut-rules.ts#L422)

When two rules disagree, the earlier entry wins. This is the tie-breaker of
record for the whole cut — the balancer, the break pass and the constraint
solver all resolve conflicts by consulting this order.
