[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/ai/litellm](../index.md) / HELPER\_CONFLICTING\_ENV

# Variable: HELPER\_CONFLICTING\_ENV

> `const` **HELPER\_CONFLICTING\_ENV**: readonly \[`"ANTHROPIC_AUTH_TOKEN"`, `"ANTHROPIC_API_KEY"`\]

Defined in: [ui/src/api-server/ai/litellm.ts:80](https://github.com/System-B90/Bluz/blob/1b02178048002eee34d502b2e3e2a402e1b9c9c0/ui/src/api-server/ai/litellm.ts#L80)

Claude Code credentials that outrank an `apiKeyHelper`. Set alongside
cc-sso-helper they make it hand LiteLLM an SSO JWT instead of the `sk-`
virtual key ("LiteLLM Virtual Key expected"), so the helper never sees them.
