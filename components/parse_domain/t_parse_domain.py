
import pytest
from fastapi.testclient import TestClient
from typing import List, Dict

from your_component_path.parse_domain import (
    ParseDomainInputDict,
    ParseDomainOutputDict,
    ParseDomain,
    parse_domain_app,
)

client = TestClient(parse_domain_app)

@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        (
            ParseDomainInputDict(domain='https://mocked-domain.com'),
            ParseDomainOutputDict(
                extracted_data=[
                    {
                        'business_name': 'Mocked Business A',
                        'contact_info': '12345',
                        'description': 'A mocked test business',
                    },
                    {
                        'business_name': 'Mocked Business B',
                        'contact_info': '67890',
                        'description': 'Another mocked test business',
                    },
                ]
            ),
        ),
        (
            # Test case for an empty input domain
            ParseDomainInputDict(domain=''),
            ParseDomainOutputDict(extracted_data=[]),
        ),
        (
            # Test case for an invalid input domain
            ParseDomainInputDict(domain='not-a-valid-domain'),
            ParseDomainOutputDict(extracted_data=[]),
        ),
    ],
)
def test_parse_domain(input_data: ParseDomainInputDict, expected_output: ParseDomainOutputDict) -> None:
    response = client.post("/transform/", json=input_data.dict())
    output = ParseDomainOutputDict(**response.json())

    assert response.status_code == 200
    assert output == expected_output
