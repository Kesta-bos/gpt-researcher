# Quick Start Guide: Using LiteLLM with GPT Researcher

This guide provides a quick setup for using GPT Researcher with LiteLLM, focusing on OpenRouter for LLMs and OpenAI for embeddings.

## 1. Install Requirements

```bash
pip install gpt-researcher litellm
```

## 2. Set API Keys

```bash
# For LLMs (using OpenRouter)
export OPENROUTER_API_KEY="your-openrouter-key"

# For embeddings (using OpenAI)
export OPENAI_API_KEY="your-openai-key"
```

## 3. Create Configuration

Create a file `config.json`:

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

## 4. Run Research

```python
import asyncio
from gpt_researcher.config import Config
from gpt_researcher.agent import GPTResearcher

async def main():
    researcher = GPTResearcher(
        query="Your research topic",
        report_type="research_report",
        config_path="config.json"
    )
    
    await researcher.conduct_research()
    report = await researcher.write_report()
    print(report)

if __name__ == "__main__":
    asyncio.run(main())
```

## Common Issues

1. **Missing API Keys**: Ensure both OPENROUTER_API_KEY and OPENAI_API_KEY are set
2. **Model Not Found**: Verify model names in config.json match available models
3. **Rate Limits**: Consider using different models or implementing delays

For more detailed configuration and advanced usage, see [Using LiteLLM with GPT Researcher](using-litellm.md).
