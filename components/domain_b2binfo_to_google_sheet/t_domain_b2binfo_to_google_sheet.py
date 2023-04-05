
import pytest
from fastapi.testclient import TestClient
from pydantic import ValidationError
from core.workflows.example_workflow import DomainNameInputModel, GoogleSheetOutputModel, domain_b2b_info_to_google_sheet_app

# Import DomainB2BInfoToGoogleSheet component once it is available
# from core.workflows.example_workflow import DomainB2BInfoToGoogleSheet

client = TestClient(domain_b2b_info_to_google_sheet_app)

test_cases = [
    ("example.com", "https://sheets.google.com/spreadsheet/example"),
    ("testdomain.org", "https://sheets.google.com/spreadsheet/test"),
]

@pytest.mark.parametrize("domain_name,expected_sheet_url", test_cases)
async def test_transform(domain_name, expected_sheet_url):
    input_model = DomainNameInputModel(domain=domain_name)
    # Instantiate the component if it is already available
    # domain_b2b_info_to_google_sheet = DomainB2BInfoToGoogleSheet()
    
    # Use FastAPI test client to simulate call to the API
    response = client.post("/transform/", json=input_model.dict())

    assert response.status_code == 200

    output_model = GoogleSheetOutputModel(**response.json())

    # Call component's transform method if it is available
    # output_model = await domain_b2b_info_to_google_sheet.transform(input_model, callbacks=None)

    assert output_model.sheet_url == expected_sheet_url

def test_invalid_domain_name():
    with pytest.raises(ValidationError):
        DomainNameInputModel(domain="invalid")

@pytest.mark.parametrize("invalid_model_data", [{}, {"domain": None}])
def test_required_fields(invalid_model_data):
    with pytest.raises(ValidationError):
        DomainNameInputModel(**invalid_model_data)
