# Using LiteLLM with GPT Researcher

This guide explains how to use LiteLLM to integrate various LLM providers with GPT Researcher.

## Configuration

### Setting up API Keys

First, set up your environment variables for the APIs you want to use:

```bash
# OpenAI API (for embeddings)
export OPENAI_API_KEY="your-openai-key"

# OpenRouter API (for LLMs)
export OPENROUTER_API_KEY="your-openrouter-key"
```

### Configuration File

Create a configuration file (e.g., `config/variables/litellm.json`):

```json
{
    "RETRIEVER": "tavily",
    "EMBEDDING": "openai:text-embedding-3-small",
    "SIMILARITY_THRESHOLD": 0.6,
    "FAST_LLM": "litellm:openrouter/openai/gpt-4o-mini",
    "SMART_LLM": "litellm:openrouter/openai/gpt-4o-2024-08-06",
    "STRATEGIC_LLM": "litellm:openrouter/openai/gpt-4o-2024-08-06",
    "FAST_TOKEN_LIMIT": 2000,
    "SMART_TOKEN_LIMIT": 4000,
    "BROWSE_CHUNK_MAX_LENGTH": 8192,
    "SUMMARY_TOKEN_LIMIT": 700,
    "TEMPERATURE": 0.4,
    "LLM_TEMPERATURE": 0.55,
    "MAX_SEARCH_RESULTS_PER_QUERY": 5,
    "MEMORY_BACKEND": "local",
    "TOTAL_WORDS": 1000,
    "REPORT_FORMAT": "APA",
    "MAX_ITERATIONS": 4,
    "AGENT_ROLE": null,
    "SCRAPER": "bs",
    "MAX_SUBTOPICS": 3,
    "REPORT_SOURCE": null,
    "DOC_PATH": "./my-docs"
}
```

## Supported LLM Providers

LiteLLM supports various LLM providers. Here's how to configure them:

### OpenRouter Format
```
litellm:openrouter/provider/model-name
```

Examples:
- `litellm:openrouter/openai/gpt-4o-2024-08-06`
- `litellm:openrouter/anthropic/claude-3-opus`
- `litellm:openrouter/google/gemini-pro`

### Direct Provider Format
```
litellm:provider/model-name
```

Examples:
- `litellm:openai/gpt-4`
- `litellm:anthropic/claude-3-opus`
- `litellm:google/gemini-pro`

## Usage Example

```python
from gpt_researcher.config import Config
from gpt_researcher.agent import GPTResearcher

async def run_research():
    # Initialize with LiteLLM config
    researcher = GPTResearcher(
        query="Your research query",
        report_type="research_report",
        config_path="/path/to/your/litellm_config.json"
    )
    
    # Conduct research
    await researcher.conduct_research()
    
    # Generate report
    report = await researcher.write_report()
    return report
```

## Provider-Specific Setup

### OpenRouter
```bash
export OPENROUTER_API_KEY="your-key"
```

### OpenAI
```bash
export OPENAI_API_KEY="your-key"
```

### Anthropic
```bash
export ANTHROPIC_API_KEY="your-key"
```

### Google
```bash
export GOOGLE_API_KEY="your-key"
```

## Best Practices

1. **API Key Management**: Store API keys securely in environment variables or a secure configuration management system.

2. **Model Selection**: 
   - Use `FAST_LLM` for quick, simple tasks
   - Use `SMART_LLM` for complex reasoning
   - Use `STRATEGIC_LLM` for high-level planning

3. **Error Handling**: LiteLLM provides standardized error handling across providers. Monitor the application logs for any API-related issues.

4. **Cost Management**: Different providers have different pricing models. Monitor usage through LiteLLM's built-in cost tracking features.

## Troubleshooting

Common issues and solutions:

1. **API Key Errors**:
   ```
   Error: The api_key client option must be set
   Solution: Ensure environment variables are properly set
   ```

2. **Model Not Found**:
   ```
   Error: Model not found
   Solution: Verify the model name and provider syntax
   ```

3. **Rate Limiting**:
   ```
   Error: Rate limit exceeded
   Solution: Implement backoff strategy or switch providers
   ```

## Additional Resources

- [LiteLLM Documentation](https://docs.litellm.ai/)
- [OpenRouter Documentation](https://openrouter.ai/docs)
- [GPT Researcher Documentation](https://docs.gptr.dev/)
