[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/cut-rules](../index.md) / CUT\_PRIORITY\_LADDER

# Variable: CUT\_PRIORITY\_LADDER

> `const` **CUT\_PRIORITY\_LADDER**: `ReadonlyArray`\<\{ `description`: `string`; `rule`: `string`; \}\>

Defined in: [ui/src/api-shared/gantt/cut-rules.ts:424](https://github.com/System-B90/Bluz/blob/d77dcf130db661461363a52910f62a34b3514ebd/ui/src/api-shared/gantt/cut-rules.ts#L424)

When two rules disagree, the earlier entry wins. This is the tie-breaker of
record for the whole cut — the balancer, the break pass and the constraint
solver all resolve conflicts by consulting this order.
