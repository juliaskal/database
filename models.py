# Файл с моделями

from typing import Optional
from sqlmodel import SQLModel, create_engine, Session, Field, select
from datetime import *

# Определение модели для таблицы "Клиент"
class Клиент(SQLModel, table=True):
    НомерКарты: str = Field(primary_key=True)
    ФИО: str
    ДатаРождения: str
    Телефон: str
    e_mail: str

# Определение модели для таблицы "Сотрудник"
class Сотрудник(SQLModel, table=True):
    ТабельныйНомер: str = Field(primary_key=True)
    ФИО: str
    ДатаРождения: Optional[str]
    Телефон: str
    e_mail: Optional[str]

# Определение модели для таблицы "Товары"
class Товары(SQLModel, table=True):
    КодТовара: str = Field(primary_key=True)
    НазваниеТовара: Optional[str]
    Цена: float
    Марка: Optional[str]
    КоличествоТовара: Optional[int]
    Категория: str
    Состояние: str

# Определение модели для таблицы "Чек"
class Чек(SQLModel, table=True):
    НомерЧека: str = Field(primary_key=True)
    ДатаИВремя: str
    НомерКарты: Optional[str]
    ПроцентСкидки: Optional[float]
    ОбщаяСтоимостьБезСкидки: Optional[float]
    ОбщаяСтоимостьСоСкидкой: Optional[float]
    ТабельныйНомер: str

# Определение модели для таблицы "ТоварыВЧеке"
class ТоварыВЧеке(SQLModel, table=True):
    НомерЧека: str = Field(primary_key=True)
    КодТовара: Optional[str] = Field(primary_key=True)
    КоличествоТовараВЧеке: Optional[int]
    СтоимостьТовара: Optional[float]

#------------------------------
# Создание базы данных и таблиц
sqlite_url = "sqlite:///МузыкальныйМагазин.db"
engine = create_engine(sqlite_url, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

#-------------------------------
# Заполнение таблицы с клиентами
def create_client():
    client1 = Клиент(НомерКарты="К001", ФИО="Кошкин Тартар Викторович", ДатаРождения="07-06-1990",Телефон="+79211119900",e_mail="dgdr@mail.ru")
    client2 = Клиент(НомерКарты="К002", ФИО="Петрова Марина Алексеевна", ДатаРождения="06-06-1990",Телефон="+79211119901",e_mail="dgdra@mail.ru")
    client3 = Клиент(НомерКарты="К003", ФИО="Мухина Лариса Петровна", ДатаРождения="04-01-1998",Телефон="+79609991142",e_mail="xcbdgh@mail.ru")
    with Session(engine) as session:
        session.add(client1)
        session.add(client2)
        session.add(client3)
        session.commit()

# Заполнение таблицы с сотрудниками
def create_employee():
    employee1 = Сотрудник(ТабельныйНомер="С001", ФИО="Агафонов Павел Андреевич", ДатаРождения="02-05-1989",Телефон="+79151237010",e_mail="cvghjk@mail.ru")
    employee2 = Сотрудник(ТабельныйНомер="С002", ФИО="Трофимова Ева Львовна", ДатаРождения="01-06-1990",Телефон="+79151237490",e_mail="cvgfhttfdjk@mail.ru")
    employee3 = Сотрудник(ТабельныйНомер="С003", ФИО="Русаков Леонид Алексеевич", ДатаРождения="03-07-1988",Телефон="+72751237010",e_mail="sefghjk@mail.ru")
    with Session(engine) as session:
        session.add(employee1)
        session.add(employee2)
        session.add(employee3)
        session.commit()

# Заполнение таблицы с товарами
def create_products():
    product1 = Товары(КодТовара="Т001", НазваниеТовара="Акустическая система BEHRINGER B112D", Цена=30030, Марка="BEHRINGER",КоличествоТовара=100, Категория="Акустические системы", Состояние="новый")
    product2 = Товары(КодТовара="Т002", НазваниеТовара="Аудиоинтерфейс FOCUSRITE", Цена=20768, Марка="FOCUSRITE",КоличествоТовара=150, Категория="Аудиоинтерфейсы", Состояние="новый")
    product3 = Товары(КодТовара="Т003", НазваниеТовара="Аудиоинтерфейс BEHRINGER UMC204HD", Цена=11080, Марка="BEHRINGER",КоличествоТовара=2, Категория="Аудиоинтерфейсы", Состояние="уценка")
    with Session(engine) as session:
        session.add(product1)
        session.add(product2)
        session.add(product3)
        session.commit()

# Заполнение таблицы с чеками
def create_checks():
    check1 = Чек(НомерЧека="Ч001", ДатаИВремя="07-06-2018", НомерКарты="К001", ПроцентСкидки=5.0,
                 ОбщаяСтоимостьБезСкидки=70250.0, ОбщаяСтоимостьСоСкидкой=66737.5, ТабельныйНомер="С002")
    check2 = Чек(НомерЧека="Ч002", ДатаИВремя="05-10-2022", НомерКарты="К002", ПроцентСкидки=3.0,
                 ОбщаяСтоимостьБезСкидки=11080.0, ОбщаяСтоимостьСоСкидкой=10747.6, ТабельныйНомер="С003")
    check3 = Чек(НомерЧека="Ч003", ДатаИВремя="07-10-2022", НомерКарты="К005", ПроцентСкидки=3.0,
                 ОбщаяСтоимостьБезСкидки=17190.0, ОбщаяСтоимостьСоСкидкой=16674.3, ТабельныйНомер="С005")
    with Session(engine) as session:
        session.add(check1)
        session.add(check2)
        session.add(check3)
        session.commit()

# Заполнение таблицы с товарами в чеке
def create_products_in_check():
    products_in_check1 = ТоварыВЧеке(НомерЧека="Ч001", КодТовара="Т001", КоличествоТовараВЧеке=2, СтоимостьТовара=60060.0)
    products_in_check2 = ТоварыВЧеке(НомерЧека="Ч001", КодТовара="Т005", КоличествоТовараВЧеке=1, СтоимостьТовара=10190.0)
    products_in_check3 = ТоварыВЧеке(НомерЧека="Ч002", КодТовара="Т003", КоличествоТовараВЧеке=1, СтоимостьТовара=11080.0)
    products_in_check4 = ТоварыВЧеке(НомерЧека="Ч003", КодТовара="Т005", КоличествоТовараВЧеке=1, СтоимостьТовара=10190.0)
    products_in_check5 = ТоварыВЧеке(НомерЧека="Ч003", КодТовара="Т006", КоличествоТовараВЧеке=1, СтоимостьТовара=7000.0)
    with Session(engine) as session:
        session.add(products_in_check1)
        session.add(products_in_check2)
        session.add(products_in_check3)
        session.add(products_in_check4)
        session.add(products_in_check5)
        session.commit()
#-----------------------
        
def main():
    create_db_and_tables()
    create_client()
    create_employee()
    create_products()
    create_checks()
    create_products_in_check()

if __name__ == "__main__": 
    main()
