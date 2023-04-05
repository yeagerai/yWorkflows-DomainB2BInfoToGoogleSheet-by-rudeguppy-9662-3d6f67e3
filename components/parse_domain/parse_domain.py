
import os
import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI
from typing import List, Dict
from pydantic import BaseModel
import yaml

from core.abstract_component import AbstractComponent


class ParseDomainInputDict(BaseModel):
    domain: str


class ParseDomainOutputDict(BaseModel):
    extracted_data: List[Dict[str, str]]


class ParseDomain(AbstractComponent):
    def __init__(self) -> None:
        super().__init__()
        with open(self.component_configuration_path(), "r", encoding="utf-8") as file:
            yaml_data = yaml.safe_load(file)
        self.timeout: int = int(yaml_data["parameters"]["timeout"])

    def transform(self, args: ParseDomainInputDict) -> ParseDomainOutputDict:
        # 1. Validate the input domain URL
        domain = args.domain

        # 2. Send an HTTP GET request to the input domain URL with the specified timeout using the requests library
        response = requests.get(domain, timeout=self.timeout)

        # 3. Parse the received HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # 4. Identify HTML elements containing B2B businesses information like business name, contact information, and business description
        # (replace 'your_selector' with the actual CSS selector)
        b2b_elements = soup.select('your_selector')

        extracted_data = []

        # 5. Extract the information from the identified HTML elements
        for element in b2b_elements:
            business_name = ''  # Extract business_name from element
            contact_info = ''   # Extract contact_info from element
            description = ''    # Extract description from element

            # 6. Perform post-processing on the extracted information to present it in structured format
            extracted_data.append({
                'business_name': business_name,
                'contact_info': contact_info,
                'description': description
            })

        # 7. Return the structured B2B information as output
        return ParseDomainOutputDict(extracted_data=extracted_data)


parse_domain_app = FastAPI()


@parse_domain_app.post("/transform/")
async def transform(args: ParseDomainInputDict) -> ParseDomainOutputDict:
    parse_domain = ParseDomain()
    return parse_domain.transform(args)

