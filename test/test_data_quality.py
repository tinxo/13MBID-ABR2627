import pandas as pd
import pytest
from pandera.pandas import DataFrameSchema, Column, Check


GENEROS = ["Femenino", "Masculino", "Otro"]

@pytest.fixture
def datos_clientes():
    """ Función para cargar los datos de clientes a un dataframe

    Args:
        None

    Returns:
        pd.DataFrame: Dataframe con los datos de clientes
    """
    df = pd.read_csv("data/raw/datos_clientes.csv", sep=";")
    return df


@pytest.fixture
def datos_resenas():
    """ Función para cargar los datos de reseñas a un dataframe

    Args:
        None

    Returns:
        pd.DataFrame: Dataframe con los datos de reseñas
    """
    df = pd.read_csv("data/raw/datos_resenas.csv", sep=";")
    return df


def test_schema_datos_clientes(datos_clientes):
    """ Función para validar el esquema de los datos de clientes

    Args:
        datos_clientes (pd.DataFrame): Dataframe con los datos de clientes

    Returns:
        None
    """
    schema = DataFrameSchema(
        {
            "id_cliente": Column(int, nullable=False),
            "edad": Column(float, nullable=True, checks=Check.in_range(18, 90)),
            "genero": Column(str, nullable=False, checks=Check.isin(GENEROS)),
            "ciudad": Column(str, nullable=False),
            "antiguedad_cliente_meses": Column(int, nullable=True, checks=Check.ge(0)),
            "canal_registro": Column(str, nullable=False),
        }
    )
    schema.validate(datos_clientes)