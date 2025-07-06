# Multi-Agent Research Tool

## Overview
The Multi-Agent Research Tool is designed to facilitate the interaction and collaboration of multiple agents to perform research-related tasks. Each agent is specialized in a specific function, allowing for efficient data retrieval, processing, and task management.

## Project Structure
The project is organized into several key directories:

- **agents/**: Contains the implementations of various agents that perform specific tasks.
  - `web_search_agent.py`: Interacts with web search APIs to retrieve information.
  - `arxiv_agent.py`: Fetches research papers and related data from the Arxiv repository.
  - `writer_agent.py`: Generates or formats text based on inputs.
  - `supervisor_agent.py`: Coordinates tasks among other agents.

- **tools/**: Includes utility tools that assist the agents in their operations.
  - `duckduckgo_search.py`: Performs searches using the DuckDuckGo search engine.
  - `arxiv_tools.py`: Provides utility functions for interacting with the Arxiv API.
  - `handoff_tool.py`: Facilitates the handoff of tasks or data between agents.

- **graph/**: Contains modules related to the multi-agent graph structure.
  - `multi_agent_graph.py`: Represents the relationships and interactions between different agents.

- **utils/**: Provides utility functions and configuration management.
  - `message_utils.py`: Handles messages between agents.
  - `config_utils.py`: Manages configuration settings for the project.

## Installation
To set up the project, clone the repository and install the required dependencies:

```bash
git clone https://github.com/staru09/multi_agent_research_tool
cd multi_agent_research_tool
pip install -r requirements.txt
```

## Usage
To run the application, execute the following command:

```bash
python app.py
```
You can also run the jupyter notebook in kaggle/google colab pre-configured environments to avoid all the setup locally.

This will start the multi-agent system, allowing the agents to begin their tasks.

## Todo

- [ ] Add more specialized agents (e.g., code analysis, data visualization, etc.)
- [ ] Create a user interface (UI) for better interaction and usability
- [ ] Integrate support for multiple language models (e.g., OpenAI, Anthropic, etc.)

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.