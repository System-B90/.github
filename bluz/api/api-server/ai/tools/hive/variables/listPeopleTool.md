[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/ai/tools/hive](../index.md) / listPeopleTool

# Variable: listPeopleTool

> `const` **listPeopleTool**: [`AiTool`](../../types/type-aliases/AiTool.md)\<`ListPeopleArgs`\>

Defined in: [ui/src/api-server/ai/tools/hive.ts:102](https://github.com/System-B90/Bluz/blob/9da30d3fe7bc9583b86fb81afc4a7774c580c249/ui/src/api-server/ai/tools/hive.ts#L102)

Hive users by id or name. Events, gantt rows and syllabuses store people as
bare Hive user ids; without this the model can only answer "instructor 32".
