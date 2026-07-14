from abc import ABC, abstractmethod


class BaseCollector(ABC):
    """
    Base class for every Legion Labs data collector.
    """

    @abstractmethod
    def collect(self):
        """Collect data."""
        raise NotImplementedError

    @abstractmethod
    def source_name(self) -> str:
        """Return collector name."""
        raise NotImplementedError