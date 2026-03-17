"""Lecture 01 practice problems.

Implement each function below so tests pass.
Rules:
- Do not change function names/signatures.
- Keep implementations pure unless the function explicitly needs I/O.
- Use only the Python standard library.
"""

from __future__ import annotations


def normalize_username(name: str) -> str:
    """Return a normalized username.

    Rules:
    - Trim outer whitespace
    - Lowercase everything
    - Replace internal whitespace runs with a single underscore
    """

    name = name.strip()
    name = name.lower()
    name = name.replace(" ", "_")
    return(name)

    raise NotImplementedError


def is_valid_age(age: int) -> bool:
    """Return True if age is in [18, 120], otherwise False."""

    if age >= 18 and age <= 120:
        return True
    else:
        return False
    
    raise NotImplementedError


def truthy_values(values: list[object]) -> list[object]:
    """Return a new list containing only truthy values from input."""

    truevalues = []
    for i in values:
        if i:
            truevalues.append(i)
    return (truevalues)

    raise NotImplementedError


def sum_until_negative(numbers: list[int]) -> int:
    """Return sum of numbers until the first negative value (exclusive)."""
    positives = []
    for i in numbers:
        if i >= 0:
            positives.append(i)
        else:
            return sum(positives)
    raise NotImplementedError


def skip_multiples_of_three(numbers: list[int]) -> list[int]:
    """Return numbers excluding values divisible by 3."""
    
    notdivisible = []
    for i in numbers:
        if i % 3 != 0:
            notdivisible.append(i)
    return notdivisible
    raise NotImplementedError


def first_even_or_none(numbers: list[int]) -> int | None:
    """Return the first even number, or None if no even number exists."""
    
    for i in numbers:
        if i % 2 == 0:
            return i
    return "None"
    raise NotImplementedError


def squares_of_even(numbers: list[int]) -> list[int]:
    """Return squares of all even numbers in input order."""
    
    even = []
    for i in number:
        if i % 2 == 0:
            even.append(i**2)
    return even
    raise NotImplementedError


def word_lengths(words: list[str]) -> dict[str, int]:
    """Return dict mapping each word to its length."""
    
    wordlengths = []
    for i in words:
        wordlengths.append(len(i))
        wordlengths.append(i)
    return wordlengths
    raise NotImplementedError


def zip_to_pairs(keys: list[str], values: list[int]) -> list[tuple[str, int]]:
    """Zip keys and values into list of pairs. Ignore extras in longer list."""
    raise NotImplementedError


def build_user(name: str, role: str = "student", active: bool = True) -> dict[str, object]:
    """Build and return {'name': name, 'role': role, 'active': active}."""
    raise NotImplementedError


def append_tag_safe(tag: str, tags: list[str] | None = None) -> list[str]:
    """Append tag to tags safely (no shared mutable default across calls)."""
    raise NotImplementedError


def invert_dict(mapping: dict[str, int]) -> dict[int, str]:
    """Invert mapping. Assume values are unique."""
    raise NotImplementedError


def unique_sorted_tags(tags: list[str]) -> list[str]:
    """Return unique tags sorted ascending."""
    raise NotImplementedError


def count_words(words: list[str]) -> dict[str, int]:
    """Count occurrences of each word using collections.Counter."""
    raise NotImplementedError


def group_scores(records: list[tuple[str, int]]) -> dict[str, list[int]]:
    """Group scores by student name using collections.defaultdict(list)."""
    raise NotImplementedError


def rotate_queue(items: list[str], steps: int) -> list[str]:
    """Rotate queue to the right by `steps` using collections.deque and return as list."""
    raise NotImplementedError


def safe_int(value: str) -> int | None:
    """Convert string to int, returning None if conversion fails."""
    if value.isdigit():
        return int(value)
    else:
        return None
    raise NotImplementedError


def read_lines(path: str) -> list[str]:
    """Read a text file with a context manager and return non-empty stripped lines."""
    raise NotImplementedError


def top_n_scores(scores: list[int], n: int = 3) -> list[int]:
    """Return top `n` scores in descending order."""
    sortedscore = sorted(scores, reverse=True)[:n]
    return sortedscore
    raise NotImplementedError


def all_passed(scores: list[int], threshold: int = 50) -> bool:
    """Return True if every score is >= threshold."""
    for i in scores:
        if i < threshold:
            return False
    return True
    raise NotImplementedError
