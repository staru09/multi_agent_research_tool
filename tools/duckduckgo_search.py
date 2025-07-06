from langchain_community.tools import DuckDuckGoSearchResults

class DuckDuckGoSearchWrapper:
    def __init__(self):
        self.search = DuckDuckGoSearchResults(output_format="list")
    
    def invoke(self, query):
        return self.search.invoke(query)