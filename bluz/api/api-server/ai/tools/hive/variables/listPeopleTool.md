[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/ai/tools/hive](../index.md) / listPeopleTool

# Variable: listPeopleTool

> `const` **listPeopleTool**: [`AiTool`](../../types/type-aliases/AiTool.md)\<`ListPeopleArgs`\>

Defined in: [ui/src/api-server/ai/tools/hive.ts:102](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-server/ai/tools/hive.ts#L102)

Hive users by id or name. Events, gantt rows and syllabuses store people as
bare Hive user ids; without this the model can only answer "instructor 32".
