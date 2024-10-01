import pandas as pd
from db_class import AircraftModels, Manufacturer
from db_manager import Session


def fill_table(document):
    with Session() as session:
        for index, row in document.iterrows():
            try:
                manufacturer_code = row['manufacturercode'].strip()
                manufacturer = session.query(Manufacturer).filter_by(name=manufacturer_code).first()
                if manufacturer is None:
                    manufacturer = Manufacturer(name=manufacturer_code)
                    session.add(manufacturer)
                    session.commit()
                    print(f"Добавлен производитель: {manufacturer_code}")
                else:
                    print(f"Производитель уже существует: {manufacturer_code}")

                existing_model = session.query(AircraftModels).filter_by(
                    model_code=row['designator'].strip(),
                    model_description=row['modelfullname'].strip(),
                    manufacturer_id=manufacturer.id
                ).first()

                if existing_model is None:
                    model = AircraftModels(
                        model_code=row['designator'].strip(),
                        model_description=row['modelfullname'].strip(),
                        manufacturer_id=manufacturer.id
                    )
                    session.add(model)
                    print(f"Добавлена модель: {model.model_code} - {model.model_description}")
                else:
                    print(f"Модель уже существует: {existing_model.model_code} - {existing_model.model_description}")

            except Exception as e:
                print(f"Ошибка при добавлении данных для строки {index}: {e}")

    session.commit()

print("Данные успешно загружены в базу данных")


if __name__ == "__main__":
    document = pd.read_csv('https://opensky-network.org/datasets/metadata/doc8643AircraftTypes.csv')
    document.columns = document.columns.str.strip().str.lower()
    fill_table(document)
