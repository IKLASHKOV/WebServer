import pandas as pd
from db_manager import Session, AircraftModels, Manufacturer


def fill_table(document):
    with Session() as session:
        for _, row in document.iterrows():
            manufacturer_code = row['manufacturercode'].strip()
            try:
                manufacturer = Manufacturer(name=manufacturer_code)
                session.add(manufacturer)
                session.commit()
                print(f"Добавлен производитель: {manufacturer_code}")
            except:
                session.rollback()
                print(f"Производитель уже существует: {manufacturer_code}")

            manufacturer_id = session.query(Manufacturer.id).filter_by(name=manufacturer_code).scalar()
            try:
                model = AircraftModels(
                    model_description=row['modelfullname'].strip(),
                    manufacturer_id=manufacturer_id
                )
                session.add(model)
                session.commit()
                print(f"Добавлена модель: {model.model_description}")
            except:
                session.rollback()
                print(f"Модель уже существует: {model.model_description}")
    print("Данные успешно загружены в базу данных")


if __name__ == "__main__":
    document = pd.read_csv('https://opensky-network.org/datasets/metadata/doc8643AircraftTypes.csv')
    document.columns = document.columns.str.strip().str.lower()
    fill_table(document)
