from back.models.base_model import BaseModel
from back.dao.session import Session


class BaseDao:
    def __init__(self, model_type: BaseModel):
        self.__model_type = model_type

    def save(self, model: BaseModel) -> BaseModel:
        if isinstance(model, BaseModel):
            with Session() as session:
                session.add(model)
                session.commit()
                session.refresh(model)
                return model
        else:
            raise TypeError('Model must be a BaseModel type.')
    
    def read_all(self) -> list[BaseModel]:
        with Session() as session:
            result = session.query(self.__model_type).order_by('id').all()
        return result

    def read_by_id(self, id_: int) -> BaseModel:
        if isinstance(id_, int):
            with Session() as session:
                result = session.query(self.__model_type).filter_by(id_=id_).first()
            return result
        else:
            raise TypeError('ID must be a integer.')

    def delete(self, model: BaseModel) -> None:
        if isinstance(model, BaseModel):
            with Session() as session:
                result = session.delete(model)
                session.commit()
        else:
            raise TypeError('Model must be a BaseModel type.')
