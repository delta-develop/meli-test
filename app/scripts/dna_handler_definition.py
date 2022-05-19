from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Optional


class DNAHandler(ABC):
    """Generalization of the DNA handler to build a chain of
    responsability.
    """

    @abstractmethod
    async def set_next(self, dna_handler: DNAHandler):
        """Define the next handler on the chain.

        Args:
            dna_handler (DNAHandler): Next handler to associate.
        """
        ...

    @abstractmethod
    async def handle(self, request):
        """Define the method to handle with the request.

        Args:
            request (Any): request to handle with.
        """
        ...


class AbstractDNAHandler(DNAHandler):
    """Abstraction of the DNA handler."""

    _next_handler: Optional[DNAHandler] = None

    def set_next(self, dna_handler):
        """Ensure how all the AbstractDNAHandlers will
        be linked to the next one.

        Args:
            dna_handler (Any): Handler to put in chain.

        Returns:
            Any: Same handler form the input.
        """
        self._next_handler = dna_handler
        return dna_handler

    @abstractmethod
    async def handle(self, request: Any) -> Any:
        """Link the handler by it behaviour, in this case
        if there's another handler in the chain, actual
        will send the request to the next.

        Args:
            request (Any): Request to process.

        Returns:
            Any: The result of the next handler if it can
            solve the request.
        """
        if self._next_handler:
            return await self._next_handler.handle(request)
