from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends, status, HTTPException
from typing import Optional
import db.database as database
import model.schema as schema
import logging

router = APIRouter(tags=['crud'])
get_db = database.get_db

@router.delete('/delete-id', status_code=status.HTTP_200_OK)
async def del_by_id(id: int, db: Session = Depends(get_db)):

    whole_search = db.query(schema.Cat_schema)
    if id:
        whole_search = whole_search.filter(schema.Cat_schema.id == id)

    if not whole_search.first():
        logging.info('Requisition not found!')   
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST) 
    whole_search.delete(synchronize_session=False)
    db.commit()
    logging.info('Deleted item!')
    return "Deleted item!"


@router.delete('/delete', status_code=status.HTTP_200_OK)
async def del_by_par(db: Session = Depends(get_db), breed : Optional[str] = None, 
        location_of_origin : Optional[str] = None, coat_length : Optional[float] = None,
        body_type : Optional[str] = None, pattern : Optional[str] = None):

    values = {'breed':breed,'location_of_origin':location_of_origin,'coat_length':coat_length,
            'body_type':body_type, 'pattern':pattern}
    whole_search = db.query(schema.Cat_schema)
    for attr,value in values.items():
        if value == None:
            pass
        else:
            whole_search = whole_search.filter(getattr(schema.Cat_schema,attr)==value)
    if not whole_search.first():
        logging.info('Requisition not found!')   
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

    whole_search.delete(synchronize_session=False)
    db.commit()
    logging.info('Deleted item!')
    return "Deleted item!"
