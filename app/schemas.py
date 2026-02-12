from pydantic import BaseModel

class ReadmeStructure(BaseModel):
    overview: str
    architecture: str
    installation: str
    usage: str
    structure: str
    assumptions: str
    limitations: str
