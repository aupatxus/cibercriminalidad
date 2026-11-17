
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import variables 

def h2():

    df = pd.read_csv(variables.csv_2, sep=";", thousands=".")
    print("\nProcesando el csv:", variables.csv_2 )


    # Filtrado para excluir Comunidades autónomas: TOTAL NACIONAL y Grupo penal: TOTAL grupo penal
    df_dataset2 = df[
        (df["Comunidades autónomas"] != "TOTAL NACIONAL") & 
        (df["Grupo penal"] != "TOTAL grupo penal")
    ]

    # Guardar el Dataset 2 en archivo csv
    df_dataset2.sort_values(by=["periodo", "Total"], ascending=[False, False]).to_csv(
        variables.csv_h2, sep=";"
    )

    print("\nSe ha generado el dataset 2:", variables.csv_h2 )

    # Ranking acumulado de hechos conocidos por Comunidad Autónoma
    ranking_ccaa = df_dataset2.groupby("Comunidades autónomas")["Total"].sum().sort_values(ascending=False)
    print("\nRanking acumulado de hechos conocidos por Comunidad Autónoma", ranking_ccaa)


    # gráfico 2_1:


    # Invertimos el orden para que la comunidad con más delitos aparezca arriba
    ranking_plot = ranking_ccaa.sort_values(ascending=True)

    # Calcular el porcentaje sobre el total para enriquecer las etiquetas
    total_general = ranking_plot.sum()
    porcentajes = (ranking_plot / total_general) * 100

    # Crear la figura
    fig, ax = plt.subplots(figsize=(11, 7))

    # Dibujar barras horizontales (destacando el Top 3 en un tono más oscuro)
    colores = ["#8ab4d8"] * (len(ranking_plot) - 3) + ["#1f4e78"] * 3
    bars = ax.barh(ranking_plot.index, ranking_plot.values, color=colores, height=0.7)

    # Títulos y etiquetas limpios
    ax.set_title("Ciberdelitos de hechos conocidos por Comunidad Autónoma (Acumulado histórico desde 2011 hasta 2025)", fontsize=14, fontweight="bold", pad=15)
    ax.set_xlabel("Total de hechos conocidos", fontsize=11, labelpad=10)

    # Formatear el eje X con separador de miles (punto)
    ax.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: f"{int(x):,}".replace(",", ".")))

    # Eliminar bordes innecesarios
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(axis="x", linestyle="--", alpha=0.4)

    # Añadir el valor y el porcentaje al final de cada barra
    margen = ranking_plot.max() * 0.012
    for bar, pct in zip(bars, porcentajes):
        valor = int(bar.get_width())
        valor_fmt = f"{valor:,}".replace(",", ".")
        ax.text(
            bar.get_width() + margen,
            bar.get_y() + bar.get_height() / 2,
            f"{valor_fmt} ({pct:.1f}%)",
            va="center",
            ha="left",
            fontsize=9.5,
            color="#333333"
        )

    # Ampliar el límite derecho para que no se corte el texto de la barra superior
    ax.set_xlim(0, ranking_plot.max() * 1.18)

    plt.tight_layout()

    plt.savefig(variables.h2_1png, dpi=300)
    print("\nSe ha generado el gráfico:", variables.h2_1png )
    print("Ciberdelitos de hechos conocidos por Comunidad Autónoma (Acumulado histórico desde 2011 hasta 2025)\n")

    return True