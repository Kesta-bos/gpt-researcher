# Configuration Guide

## Environment Variables

Required environment variables for different LLM providers:

```bash
# OpenAI (for embeddings)
export OPENAI_API_KEY="your-openai-key"

# OpenRouter (for LLMs)
export OPENROUTER_API_KEY="your-openrouter-key"

# Optional: Tavily (for web search)
export TAVILY_API_KEY="your-tavily-key"
```

## Configuration File

The configuration file can be in JSON format. Here's an example using LiteLLM:

```json
{
    "RETRIEVER": "tavily",
    "EMBEDDING": "openai:text-embedding-3-small",
    "FAST_LLM": "litellm:openrouter/openai/gpt-4o-mini",
    "SMART_LLM": "litellm:openrouter/openai/gpt-4o-2024-08-06",
    "STRATEGIC_LLM": "litellm:openrouter/openai/gpt-4o-2024-08-06",
    "TEMPERATURE": 0.4,
    "MAX_SEARCH_RESULTS_PER_QUERY": 5
}
```

### LLM Configuration Format

When using LiteLLM, the LLM configuration follows this format:
- OpenRouter models: `litellm:openrouter/provider/model-name`
- Direct provider models: `litellm:provider/model-name`

Examples:
```json
{
    "FAST_LLM": "litellm:openrouter/openai/gpt-4o-mini",
    "SMART_LLM": "litellm:openrouter/anthropic/claude-3-opus",
    "STRATEGIC_LLM": "litellm:openai/gpt-4"
}
```

### Embedding Configuration

The embedding configuration follows this format:
`provider:model-name`

Example:
```json
{
    "EMBEDDING": "openai:text-embedding-3-small"
}
```

For more detailed LiteLLM configuration options, see [Using LiteLLM with GPT Researcher](llms/using-litellm.md).
