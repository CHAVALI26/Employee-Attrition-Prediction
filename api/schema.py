from pydantic import BaseModel

class EmployeeInput(BaseModel):
    Age: int
    MonthlyIncome: int
    YearsAtCompany: int
    JobSatisfaction: int
    JobRole: str
    OverTime: str
    EnvironmentSatisfaction: int | None = None
    WorkLifeBalance: int | None = None
    YearsSinceLastPromotion: int | None = None

class PredictionResponse(BaseModel):
    attrition_probability: float