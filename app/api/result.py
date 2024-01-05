from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.domain.result import Result
from app.application.result_service import ResultService
from app.infra.mysql_result_repository import MySQLResultRepository
from app.infra.db import get_db


result_router = APIRouter(
    prefix="/results"
)


def get_result_service(db: Session = Depends(get_db)) -> ResultService:
    return ResultService(MySQLResultRepository(db))


@result_router.post("/")
def create_result(
    result: Result, 
    service: ResultService = Depends(get_result_service)
):
    return service.create_result(result)


@result_router.get("/")
def get_all_results(service: ResultService = Depends(get_result_service)):
    return service.get_all_results()
