[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/cut-rules](../index.md) / CUT\_PRIORITY\_LADDER

# Variable: CUT\_PRIORITY\_LADDER

> `const` **CUT\_PRIORITY\_LADDER**: `ReadonlyArray`\<\{ `description`: `string`; `rule`: `string`; \}\>

Defined in: [ui/src/api-shared/gantt/cut-rules.ts:420](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/gantt/cut-rules.ts#L420)

When two rules disagree, the earlier entry wins. This is the tie-breaker of
record for the whole cut — the balancer, the break pass and the constraint
solver all resolve conflicts by consulting this order.
