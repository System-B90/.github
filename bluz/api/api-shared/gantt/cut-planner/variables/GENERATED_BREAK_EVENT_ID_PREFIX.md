[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/cut-planner](../index.md) / GENERATED\_BREAK\_EVENT\_ID\_PREFIX

# Variable: GENERATED\_BREAK\_EVENT\_ID\_PREFIX

> `const` **GENERATED\_BREAK\_EVENT\_ID\_PREFIX**: `"cut-break:"` = `"cut-break:"`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:166](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-shared/gantt/cut-planner.ts#L166)

Synthetic `ganttEventId` prefix for breaks the post-pass generated. They are
real schedule events with no gantt event behind them; the prefix marks their
provenance so a pull-back archives them with the rest of the cut and a
re-cut never duplicates them.
