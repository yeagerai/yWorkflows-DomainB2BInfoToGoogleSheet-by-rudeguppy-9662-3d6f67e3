
import typing
from typing import Optional
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
from core.workflows.abstract_workflow import AbstractWorkflow

class DomainNameInputModel(BaseModel):
    domain: str

class GoogleSheetOutputModel(BaseModel):
    sheet_url: str

class DomainB2BInfoToGoogleSheet(AbstractWorkflow):
    def __init__(self) -> None:
        super().__init__()

    async def transform(self, args: DomainNameInputModel, callbacks: typing.Any) -> GoogleSheetOutputModel:
        results_dict = await super().transform(args=args, callbacks=callbacks)
        sheet_url = results_dict[-1].sheet_url
        return GoogleSheetOutputModel(sheet_url=sheet_url)

load_dotenv()
domain_b2b_info_to_google_sheet_app = FastAPI()

@domain_b2b_info_to_google_sheet_app.post("/transform/")
async def transform(args: DomainNameInputModel) -> GoogleSheetOutputModel:
    domain_b2b_info_to_google_sheet = DomainB2BInfoToGoogleSheet()
    return await domain_b2b_info_to_google_sheet.transform(args, callbacks=None)
