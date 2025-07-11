"""This module provides example tools for web scraping and search functionality.

It includes a basic Tavily search function (as an example)

These tools are intended as free examples to get started. For production use,
consider implementing more robust and specialized tools tailored to your needs.
"""

from typing import Any, Callable, List, Optional, cast

from langchain_tavily import TavilySearch  # type: ignore[import-not-found]
from langchain.tools import tool

from .configuration import Configuration
from src.logging_config import log
from .hook_generator import generate_hook_with_word_count
from .critic_tool import critic_content


@tool
async def search(query: str) -> Optional[dict[str, Any]]:
    """Search for general web results.

    This function performs a search using the Tavily search engine, which is designed
    to provide comprehensive, accurate, and trusted results. It's particularly useful
    for answering questions about current events.
    """
    log.info(f"[TOOL CALL] search called with query: {query}")
    log.info(f"Searching for: {query}")
    configuration = Configuration.from_context()
    wrapped = TavilySearch(max_results=configuration.max_search_results)
    result = cast(dict[str, Any], await wrapped.ainvoke({"query": query}))
    log.info(f"Search results: {result}")
    return result


from .audio_script import generate_audio_script


@tool
async def create_audio_narration(script: str) -> str:
    """
    Generate a clean, engaging voiceover script from a raw video script.
    Removes non-verbal cues, on-screen text, and pauses.
    """
    log.info(f"[TOOL CALL] create_audio_narration called with script: {script[:200]}")
    log.info(f"Creating audio narration for script: {script}")
    return await generate_audio_script(script)


@tool
async def viral_hook_generator(script: str) -> str:
    """
    Generates a compelling and viral hook for a given script by leveraging an LLM and predefined hook ideas.
    """
    log.info(f"[TOOL CALL] viral_hook_generator called with script: {script[:200]}")
    log.info(f"Generating viral hook for script: {script}")
    return await generate_hook_with_word_count(script)


@tool
async def critic_content_tool(content: str) -> str:
    """
    Critique and provide feedback on the given content.
    """
    log.info(f"[TOOL CALL] critic_content_tool called with content: {content[:200]}")  # log first 200 chars
    return await critic_content(content)


TOOLS: List[Callable[..., Any]] = [search, create_audio_narration, viral_hook_generator, critic_content]
