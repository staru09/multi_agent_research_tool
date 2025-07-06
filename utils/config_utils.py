def setup_environment():
    import getpass
    import os
    
    def _set_if_undefined(var: str):
        if not os.environ.get(var):
            os.environ[var] = getpass.getpass(f"Please provide your {var}")
    
    _set_if_undefined("OPENAI_API_KEY")