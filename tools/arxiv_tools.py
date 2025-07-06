from langchain.tools import Tool
from langchain_community.utilities.arxiv import ArxivAPIWrapper

class ArxivTools:
    def search_arxiv_summaries(self, query: str) -> str:
        """
        Use this tool to find summaries of Arxiv papers on a specific topic.
        It returns a formatted string of the top results' titles, authors, and abstracts.
        This is best for getting a quick overview of research on a topic.
        """
        print(f"\nEXECUTING TOOL: Searching Arxiv for summaries of '{query}'...")
        arxiv_wrapper = ArxivAPIWrapper()
        return arxiv_wrapper.run(query)

    def read_arxiv_paper_content(self, query: str) -> str:
        """
        Use this tool when you need to read the full content of a specific Arxiv paper to answer a question.
        You can use a keyword search or a specific Arxiv ID.
        It downloads the paper's PDF, extracts the full text, and returns it.
        Use this when summaries are not enough to answer the user's question.
        """
        print(f"\nEXECUTING TOOL: Reading full Arxiv paper for '{query}'...")
        single_paper_wrapper = ArxivAPIWrapper(top_k_results=1, doc_content_chars_max=15000)
        docs = single_paper_wrapper.load(query)
        if docs:
            return docs[0].page_content
        return "Could not find a paper for that query."
        
    def get_tools(self):
        return [
            Tool(
                name="search_arxiv_summaries",  # No spaces, all lowercase, underscores
                func=self.search_arxiv_summaries,
                description="Useful for when you need to find and summarize academic papers on a specific topic from Arxiv. The input should be a search query."
            ),
            Tool(
                name="read_arxiv_paper_content",  # No spaces, all lowercase, underscores
                func=self.read_arxiv_paper_content,
                description="Useful for when you need to read the full text of a specific paper to find details not in the summary. The input can be a specific Arxiv ID or a search query."
            )
        ]