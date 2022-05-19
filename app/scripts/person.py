from typing import Any, List

from app.scripts.dna_handler_definition import DNAHandler
from app.scripts.dna_matrix import DNAMatrix


class Person:
    """Class to describe a person who will be analyzed"""

    def __init__(self, dna_sequences: List[Any]) -> None:
        """For this case, person only needs the dna sequences.

        Args:
            dna_sequences (List[Any]): matrix with dna data.
        """
        self.dna_matrix = DNAMatrix(dna_sequences)

    async def is_mutant(self, dna_handler: DNAHandler) -> bool:
        """This method is the beginning of the responsability chain, calling
        the first handler (Row Handler).

        Args:
            dna_handler (DNAHandler): The first handler on the chain.

        Returns:
            bool: The output of the responsability chain.
        """
        result = await dna_handler.handle(self.dna_matrix)
        return result
