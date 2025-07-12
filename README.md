# LangGraph ReAct Agent for Viral Content Creation

[![CI](https://github.com/langchain-ai/react-agent/actions/workflows/unit-tests.yml/badge.svg)](https://github.com/langchain-ai/react-agent/actions/workflows/unit-tests.yml)
[![Integration Tests](https://github.com/langchain-ai/react-agent/actions/workflows/integration-tests.yml/badge.svg)](https://github.com/langchain-ai/react-agent/actions/workflows/integration-tests.yml)
[![Open in - LangGraph Studio](https://img.shields.io/badge/Open_in-LangGraph_Studio-00324d.svg?logo=data:image/svg%2bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI4NS4zMzMiIGhlaWdodD0iODUuMzMzIiB2ZXJzaW9uPSIxLjAiIHZpZXdCb3g9IjAgMCA2NCA2NCI+PHBhdGggZD0iTTEzIDcuOGMtNi4zIDMuMS03LjEgNi4zLTYuOCAyNS43LjQgMjQuNi4zIDI0LjUgMjUuOSAyNC41QzU3LjUgNTggNTggNTcuNSA1OCAzMi4zIDU4IDcuMyA1Ni43IDYgMzIgNmMtMTIuOCAwLTE2LjEuMy0xOSAxLjhtMzcuNiAxNi42YzIuOCAyLjggMy40IDQuMiAzLjQgNy42cy0uNiA0LjgtMy40IDcuNkw0Ny4yIDQzSDE2LjhsLTMuNC0zLjRjLTQuOC00LjgtNC44LTEwLjQgMC0xNS4ybDMuNC0zLjRoMzAuNHoiLz48cGF0aCBkPSJNMTguOSAyNS42Yy0xLjEgMS4zLTEgMS43LjQgMi41LjkuNiAxLjcgMS44IDEuNyAyLjcgMCAxIC43IDIuOCAxLjYgNC4xIDEuNCAxLjkgMS40IDIuNS4zIDMuMi0xIC42LS42LjkgMS44LjkgMS41IDAgMi43LS41IDIuNy0xIDAtLjYgMS4xLS44IDIuNi0uNGwyLjYuNy0xLjgtMi45Yy01LjktOS4zLTkuNC0xMi4zLTExLjUtOS44TTM5IDI2YzAgMS4xLS45IDIuNS0yIDMuMi0yLjQgMS41LTIuNiAzLjQtLjUgNC4yLjguMyAyIDEuNyAyLjUgMy4xLjYgMS41IDEuNCAyLjMgMiAyIDEuNS0uOSAxLjItMy41LS40LTMuNS0yLjEgMC0yLjgtMi44LS44LTMuMyAxLjYtLjQgMS42LS45IDAtLjYtMS4xLS4xLTEuNS0uNi0xLjItMS41LjctMS43IDMuMy0yLjEgMy41LS41LjEuNS4yIDEuNi4zIDIuMiAwIC43LjkgMS40IDEuOSAxLjYgMi4xLjQgMi4zLTIuMy4yLTMuMi0uOC0uMy0yLTEuNy0yLjUmMy4xLTEuMS0zLTMtMy4zLTMtLjUiLz48L3N2Zz4=)](https://langgraph-studio.vercel.app/templates/open?githubUrl=https://github.com/langchain-ai/react-agent)

This template provides a powerful and flexible ReAct agent built with [LangGraph](https://github.com/langchain-ai/langgraph) and designed for seamless integration with [LangGraph Studio](https://github.com/langchain-ai/langgraph-studio). This agent is specialized in creating viral short-form video content, acting as a master AI strategist and storyteller. The ReAct (Reasoning and Acting) agent paradigm allows the agent to iteratively reason about a user's query, select appropriate tools, and execute actions to arrive at a final answer. This makes it well-suited for complex creative tasks that require interaction with external tools and data sources.

![Graph view in LangGraph studio UI](./static/studio_ui.png)

The core logic is defined in `src/react_agent/graph.py`, which implements a ReAct agent that can be easily customized and extended.

## Features

- **Iterative Reasoning and Action:** The agent can reason about a problem, choose a tool, execute it, and repeat the process until it finds a solution.
- **Specialized Content Creation Tools:**
    - `viral_hook_generator`: Creates compelling hooks for video scripts.
    - `create_visuals_sfx`: Enhances scripts with visual and sound effect suggestions.
    - `critic_content_tool`: Provides critiques and feedback on content.
    - `search`: A general-purpose web search tool using Tavily.
- **Model Flexibility:** The agent can be configured to use different language models from providers like OpenAI, Anthropic, and others.
- **Customizable Prompts:** The agent's behavior can be customized by modifying the system prompt to change its persona, instructions, or constraints.
- **LangGraph Studio Integration:** The agent is designed to be used with LangGraph Studio, providing a visual interface for debugging and interacting with the agent.

## Prerequisites

- Python 3.11+
- A package manager (like `pip`)

## Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/langchain-ai/react-agent.git
    cd react-agent
    ```

2.  **Create a virtual environment:**

    ```bash
    python -m venv .venv
    source .venv/bin/activate
    ```

3.  **Install the dependencies:**

    ```bash
    pip install -e ".[dev]"
    ```

## Configuration

1.  **Create a `.env` file:**

    ```bash
    cp .env.example .env
    ```

2.  **Add your API keys to the `.env` file:**

    -   **Tavily:** The primary search tool is [Tavily](https://tavily.com/). You can get an API key [here](https://app.tavily.com/sign-in).

        ```
        TAVILY_API_KEY=your-tavily-api-key
        ```

    -   **OpenAI (Recommended):** The default model is `openai/gpt-4.1`. You'll need an API key from the [OpenAI Platform](https://platform.openai.com/signup).

        ```
        OPENAI_API_KEY=your-openai-api-key
        ```

    -   **Anthropic (Optional):** To use Anthropic's models, you'll need an API key from the [Anthropic Console](https://console.anthropic.com/).

        ```
        ANTHROPIC_API_KEY=your-anthropic-api-key
        ```

## Usage

To run the agent, open the project folder in LangGraph Studio. The studio will automatically detect the agent and provide an interface for interacting with it.

## Customization

### Adding New Tools

You can extend the agent's capabilities by adding new tools in `src/react_agent/tools.py`. A tool can be any Python function that takes a set of arguments and returns a string.

### Changing the Model

The agent defaults to `openai/gpt-4.1`. You can change the model by updating the `model` field in the agent's configuration. For example, to use Anthropic's Claude 3.5 Sonnet, you would set the model to `anthropic/claude-3-5-sonnet-20240620`.

### Customizing the Prompt

The agent's behavior is guided by a system prompt defined in `src/react_agent/prompts.py`. You can modify this prompt to change the agent's persona, instructions, or constraints.

## Codebase Overview

The `src/react_agent` directory contains the core logic of the agent. Here's a breakdown of the files and the agent's workflow:

The agent operates in a ReAct (Reasoning and Action) loop:

1.  **`graph.py`**: This is the heart of the agent. It defines the LangGraph state machine that orchestrates the agent's behavior. It starts with the `call_model` node.
2.  **`call_model` node**: This node prepares the prompt using `prompts.py` and the conversation history from `state.py`, then calls the LLM.
3.  **LLM (Reasoning)**: The LLM decides whether to respond to the user directly or use a tool.
4.  **`route_model_output` function**: This function in `graph.py` directs the flow. If a tool is called, it goes to the `tools` node; otherwise, it ends the loop.
5.  **`tools` node (Action)**: This node, defined in `graph.py`, executes the appropriate tool from `tools.py`. The available tools are:
    -   **`tools.py`**: This file defines the tools that the agent can use, such as a Tavily search tool, a tool to create audio narration, a viral hook generator, and a content critic.
    -   **`hook_generator.py`**: This file contains a tool that generates a viral video hook for a given script using an LLM and a set of predefined hook ideas.
    -   **`critic_tool.py`**: This file contains a tool that uses an LLM to critique a given piece of content, such as a video script, and provide feedback.
6.  **Loop**: The output of the tool is added to the agent's state, and the process repeats from step 2.

Other important files include:

-   **`prompts.py`**: This file contains the default system prompts used by the agent. There are different prompts for different use cases, such as generating a script or critiquing content.
-   **`state.py`**: This file defines the state objects for the agent, which are used to track the conversation history and other relevant information.
-   **`configuration.py`**: This file defines the configurable parameters for the agent, such as the system prompt, the language model to use, and the maximum number of search results.
-   **`utils.py`**: This file contains utility functions, such as a function to load a chat model from a fully specified name.

## Development

### Running Tests

The project includes a suite of unit and integration tests. To run the tests, use the following `make` commands:

-   `make test`: Run all unit tests.
-   `make test_watch`: Run unit tests in watch mode.
-   `make integration_tests`: Run integration tests.

### Linting and Formatting

The project uses `ruff` for linting and formatting. The following `make` commands are available:

-   `make lint`: Run the linter.
-   `make format`: Format the code.

### Available Commands

The `Makefile` includes the following commands:

| Command             | Description                               |
| ------------------- | ----------------------------------------- |
| `make all`          | Display the help message.                 |
| `make format`       | Run code formatters.                      |
| `make lint`         | Run linters.                              |
| `make test`         | Run unit tests.                           |
| `make test_watch`   | Run unit tests in watch mode.             |
| `make integration_tests` | Run integration tests.               |
| `make help`         | Display the help message.                 |

## Contributing

Contributions are welcome! Please feel free to submit a pull request with any improvements or new features.

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for more details.
