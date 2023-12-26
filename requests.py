# Файл запросами к БД

from typing import Optional
from sqlmodel import SQLModel, create_engine, Session, Field, select
from datetime import *
from sqlalchemy import Column, Integer, String, DateTime, Float
from models import Клиент, Сотрудник, Товары, Чек, ТоварыВЧеке


# Создание подключения к базе данных
sqlite_url = "sqlite:///МузыкальныйМагазин.db"
engine = create_engine(sqlite_url)


# Вычисление скидки клиента        
def calculate_discount(CardNumber: str, PurchaseDate: datetime) -> float:
    discount = 0.03
    TotalPurchases = 0

    # Вычисление общей суммы покупок за последние 365 дней
    with Session(engine) as session:
        statement = select(Чек.ОбщаяСтоимостьБезСкидки).where(Чек.НомерКарты == CardNumber and Чек.ДатаИВремя >= PurchaseDate - timedelta(days=365))
        results = session.exec(statement)
        for i in results:
            TotalPurchases+=i

    # Скидка равна:
    if TotalPurchases >= 80000:
        discount = 0.1
    elif TotalPurchases >= 30000:
        discount = 0.05

    return discount * 100

#print(calculate_discount("К001","01-01-2019"))
#----------------------------------------------
def add_product(CodeProduct: str, NameProduct: str, Price: float, Mark: str,
                QuantityProduct: int, Category: str, State: str):
    with Session(engine) as session:
        statement = select(Товары).filter(Товары.КодТовара == CodeProduct)
        existing_product = session.exec(statement).first()
        if not existing_product:
            new_product = Товары(КодТовара=CodeProduct, НазваниеТовара=NameProduct, Цена=Price, Марка=Mark, 
                                 КоличествоТовара=QuantityProduct, Категория=Category, Состояние=State)
            session.add(new_product)
            session.commit()

#add_product('Т008','Синтезатор CASIO', 15000, 'CASIO', 50, 'Синтезаторы', 'новый')
