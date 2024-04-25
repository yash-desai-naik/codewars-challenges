from typing import List

from packages.api import get_facts
from packages.modules.cats.cats_module import CatFact


def main() -> None:
    facts: List[CatFact] = get_facts()
    for fact in facts:
        print(f"- {fact.text}")
        print(f"- {fact.status.verified}")


if __name__ == '__main__':
    main()
