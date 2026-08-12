# Snake Trio Log
F                                                                                                                                                                                         [100%]
=========================================================================================== FAILURES ===========================================================================================
____________________________________________________________________________ test_next_head_moves_exactly_one_cell _____________________________________________________________________________

    def test_next_head_moves_exactly_one_cell() -> None:
>       assert next_head((40, 60), (1, 0), 20) == (60, 60)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

tests_public\test_snake_contract.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

head = (40, 60), direction = (1, 0), cell_size = 20

    def next_head(head: Cell, direction: Direction, cell_size: int) -> Cell:
        """Return the next head cell.
    
        Interface:
            head: current ``(x, y)`` grid position.
            direction: one of ``(-1, 0)``, ``(1, 0)``, ``(0, -1)``, ``(0, 1)``.
            cell_size: positive number of pixels moved in one step.
            return: a new ``(x, y)`` tuple.
    
        Hint: calculate x and y separately.  Do not mutate any input.
        """
        # TODO 1: replace this line with one return statement.
>       raise NotImplementedError("TODO 1: compute the next head")
E       NotImplementedError: TODO 1: compute the next head

src\snake_trio\logic.py:26: NotImplementedError
=================================================================================== short test summary info ====================================================================================
FAILED tests_public/test_snake_contract.py::test_next_head_moves_exactly_one_cell - NotImplementedError: TODO 1: compute the next head


## Members and first roles

- Driver:
- Navigator:
- Tester / Recorder:

Rotate roles after each completed TODO.

## Gate record

| Gate | Driver | Navigator | Tester / Recorder | Observed result | Next action |
|---|---|---|---|---|---|
| Baseline | | | | | |
| TODO 1 - next head | | | | | |
| TODO 2 - food | | | | | |
| TODO 3 - wall | | | | | |
| TODO 4 - body | | | | | |
| Playable run | | | | | |

## Explain-back

1. Which function was easiest to test, and why?
2. Which failing test gave the clearest clue?
3. What did your trio ask AI at L1, and what decision remained human-owned?
