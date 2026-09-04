from typing import Dict


class ProcessingStrategy:

    STRATEGIES = {
        "resume_parsing": "async",
        "ats_scoring": "async",
        "screening": "async",
        "interview": "sync",
        "decision": "sync",
    }

    @classmethod
    def get_strategy(cls, api_name: str) -> str:

        if api_name not in cls.STRATEGIES:
            raise KeyError(f"Unknown API: {api_name}")

        return cls.STRATEGIES[api_name]

    @classmethod
    def is_async(cls, api_name: str) -> bool:
        return cls.get_strategy(api_name) == "async"

    @classmethod
    def is_sync(cls, api_name: str) -> bool:
        return cls.get_strategy(api_name) == "sync"

    @classmethod
    def get_all_strategies(cls) -> Dict[str, str]:
        return cls.STRATEGIES.copy()