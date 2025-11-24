"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel

import os

import matplotlib.pyplot as plt
import pandas as pd


def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """
  # leo el archivo y dejo el año como índice para manejar mejor el eje X
    noticias_df = pd.read_csv("files/input/news.csv", index_col=0)

    # creo la figura base donde se van a pintar las líneas
    plt.figure()

    # colores que le doy a cada tipo de medio
    paleta_colores = {
        "Newspaper": "grey",
        "Television": "dimgray",
        "Radio": "lightgrey",
        "Internet": "tab:blue",
    }

    # nivel de dibujo para controlar qué línea queda encima
    orden_dibujo = {
        "Television": 1,
        "Newspaper": 1,
        "Internet": 2,
        "Radio": 1,
    }

    # grosor asignado a cada serie
    grosor_linea = {
        "Internet": 4,
        "Television": 2,
        "Newspaper": 2,
        "Radio": 2,
    }

    # recorro cada columna (medio) y la grafico
    for canal in noticias_df.columns:
        plt.plot(
            noticias_df[canal],
            color=paleta_colores[canal],
            linewidth=grosor_linea[canal],
            zorder=orden_dibujo[canal],
            label=canal,
        )

    # ajustes visuales generales del grafico
    plt.title("How people get their news", fontsize=16)
    eje_actual = plt.gca()
    eje_actual.spines["top"].set_visible(False)
    eje_actual.spines["left"].set_visible(False)
    eje_actual.spines["right"].set_visible(False)
    eje_actual.get_yaxis().set_visible(False)

    # anoto los valores iniciales y finales de cada medio
    for canal in noticias_df.columns:
        anio_inicial = noticias_df.index[0]
        valor_inicial = noticias_df[canal][anio_inicial]

        plt.scatter(
            anio_inicial,
            valor_inicial,
            color=paleta_colores[canal],
            zorder=orden_dibujo[canal],
        )
        plt.text(
            anio_inicial - 0.2,
            valor_inicial,
            f"{canal} {valor_inicial}%",
            fontsize=8,
            color=paleta_colores[canal],
            ha="right",
            va="center",
            zorder=orden_dibujo[canal],
        )

        anio_final = noticias_df.index[-1]
        valor_final = noticias_df[canal][anio_final]

        plt.scatter(
            anio_final,
            valor_final,
            color=paleta_colores[canal],
            zorder=orden_dibujo[canal],
        )
        plt.text(
            anio_final + 0.2,
            valor_final,
            f"{valor_final}%",
            fontsize=8,
            color=paleta_colores[canal],
            ha="left",
            va="center",
            zorder=orden_dibujo[canal],
        )

    # uso los años del índice como etiquetas en el eje X
    plt.xticks(noticias_df.index, noticias_df.index)
    plt.tight_layout()

    # me aseguro de que la carpeta de salida exista
    os.makedirs("files/plots", exist_ok=True)

    # guardo el grafico en el archivo indicado
    plt.savefig("files/plots/news.png")
    plt.close()

pregunta_01()