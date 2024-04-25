import os
from typing import List

import requests
from dotenv import load_dotenv

from packages.modules.cats.cats_module import CatFact, Status

load_dotenv()  # Load environment variables from .env file


def get_facts() -> List[CatFact]:
    # fetch random facts from an API
    url: str | None = os.getenv('CAT_FACTS_API_URL')
    if url is None:
        raise ValueError("CAT_FACTS_API_URL environment variable is not set")
    response = requests.get(url)
    data_ = response.json()
    cat_facts: List[CatFact] = []
    for fact in data_:
        status_data = fact['status']
        status = Status(
            verified=status_data['verified'],
            sentCount=status_data['sentCount'],
            feedback=status_data['feedback'] if 'feedback' in status_data else None
        )
        cat_fact = CatFact(
            _id=fact['_id'],
            text=fact['text'],
            status=status,
            user=fact['user'],
            source=fact['source'],
            updatedAt=fact['updatedAt'],
            type=fact['type'],
            createdAt=fact['createdAt'],
            deleted=fact['deleted'],
            used=fact['used']
        )

        cat_fact.status.verified = False
        cat_facts.append(cat_fact)
    return cat_facts
