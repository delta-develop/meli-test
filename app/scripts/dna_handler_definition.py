from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional


class DNAHandler(ABC):
    @abstractmethod
    async def set_next(self, dna_handler: DNAHandler) -> DNAHandler:
        ...

    @abstractmethod
    async def handle(self, request) -> Any:
        ...


class AbstractDNAHandler(DNAHandler):

    _next_handler: Optional[DNAHandler] = None

    def set_next(self, dna_handler: DNAHandler) -> DNAHandler:
        self._next_handler = dna_handler
        return dna_handler

    @abstractmethod
    async def handle(self, request: Any) -> Any:
        if self._next_handler:
            return await self._next_handler.handle(request)
