from typing import Any, Dict, List, Optional, Tuple
from litellm import completion
from langchain.callbacks.manager import CallbackManagerForLLMRun
from langchain.chat_models.base import BaseChatModel
from langchain.schema.messages import BaseMessage, HumanMessage, AIMessage, SystemMessage
from langchain.schema.output import ChatGeneration, ChatResult
import os

class LiteLLMProvider(BaseChatModel):
    model: str
    temperature: float = 0.7
    max_tokens: Optional[int] = None
    api_key: Optional[str] = None
    api_base: Optional[str] = None
    kwargs: Dict[str, Any] = {}

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Set OpenRouter configuration if using OpenRouter model
        if self.model.startswith("openrouter/"):
            self.api_base = "https://openrouter.ai/api/v1"
            self.api_key = os.getenv("OPENROUTER_API_KEY")

    def _convert_message_to_dict(self, message: BaseMessage) -> Dict[str, str]:
        if isinstance(message, SystemMessage):
            return {"role": "system", "content": message.content}
        elif isinstance(message, AIMessage):
            return {"role": "assistant", "content": message.content}
        elif isinstance(message, HumanMessage):
            return {"role": "user", "content": message.content}
        else:
            return {"role": "user", "content": str(message.content)}

    def _generate(
        self,
        messages: List[BaseMessage],
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> ChatResult:
        message_dicts = [self._convert_message_to_dict(m) for m in messages]
        
        response = completion(
            model=self.model,
            messages=message_dicts,
            temperature=self.temperature,
            max_tokens=self.max_tokens,
            api_key=self.api_key,
            api_base=self.api_base,
            **self.kwargs,
            **kwargs
        )
        
        message = response.choices[0].message
        generation = ChatGeneration(
            message=AIMessage(content=message.content),
            generation_info=dict(finish_reason=response.choices[0].finish_reason),
        )
        return ChatResult(generations=[generation])

    @property
    def _llm_type(self) -> str:
        return "litellm"

    @property
    def _identifying_params(self) -> Dict[str, Any]:
        return {
            "model": self.model,
            "temperature": self.temperature,
            "max_tokens": self.max_tokens,
        }

