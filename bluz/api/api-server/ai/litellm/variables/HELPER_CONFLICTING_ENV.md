[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/ai/litellm](../index.md) / HELPER\_CONFLICTING\_ENV

# Variable: HELPER\_CONFLICTING\_ENV

> `const` **HELPER\_CONFLICTING\_ENV**: readonly \[`"ANTHROPIC_AUTH_TOKEN"`, `"ANTHROPIC_API_KEY"`\]

Defined in: [ui/src/api-server/ai/litellm.ts:80](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-server/ai/litellm.ts#L80)

Claude Code credentials that outrank an `apiKeyHelper`. Set alongside
cc-sso-helper they make it hand LiteLLM an SSO JWT instead of the `sk-`
virtual key ("LiteLLM Virtual Key expected"), so the helper never sees them.
