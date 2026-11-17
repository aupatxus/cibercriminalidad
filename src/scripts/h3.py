

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import textwrap
import seaborn as sns

import variables 

def h3():

    df = pd.read_csv(variables.csv_3, sep=";", thousands=".")
    print("\nProcesando el csv:", variables.csv_3 )

    # Tipología penal

    # condición de filtrado
    df_dataset3 = df[
        (df["Comunidades autónomas"] == "TOTAL NACIONAL") & 
        (df["Tipología penal"] != "TOTAL tipo hecho")
    ]


    # Guardado en csv del Dataset 3 
    df_dataset3.sort_values(by=["periodo", "Total"], ascending=[False, False]).to_csv(
        variables.cvs_h3, index=False, sep=";"
    )


    print("\nSe ha generado el dataset 3:", variables.cvs_h3 )

    # Agrupar por tipología acumulada
    ranking_tipos = df_dataset3.groupby("Tipología penal")["Total"].sum().sort_values(ascending=False)
    print("\nRanking acumulado de hechos conocidos por tipología penal", ranking_tipos)



    # gráfico h3_1

    total_global = ranking_tipos.sum()

    top10_plot = ranking_tipos.head(10).sort_values(ascending=True)
    porcentajes = (top10_plot / total_global) * 100

    # Acortar o dividir etiquetas muy largas en 2 líneas (máx. 42 caracteres por línea) 
    etiquetas_limpias = [textwrap.fill(str(nombre), width=42) for nombre in top10_plot.index]

    # Creación de la figura
    fig, ax = plt.subplots(figsize=(12, 7.5))

    # Destacar la tipología líder en un azul más oscuro
    colores = ["#8ab4d8"] * (len(top10_plot) - 1) + ["#1f4e78"]
    bars = ax.barh(etiquetas_limpias, top10_plot.values, color=colores, height=0.68)

    # Títulos y ejes
    ax.set_title("Top 10 tipologías de ciberdelincuencia (Acumulado histórico desde 2011 hasta 2025)", fontsize=14, fontweight="bold", pad=15)
    ax.set_xlabel("Total de hechos conocidos", fontsize=11, labelpad=10)

    # Formatear el eje X con separador de miles (punto)
    ax.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: f"{int(x):,}".replace(",", ".")))

    # Limpiar bordes superiores y derechos
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(axis="x", linestyle="--", alpha=0.4)

    # Añadir etiquetas con el número exacto y el porcentaje sobre el total nacional
    margen = top10_plot.max() * 0.015
    for bar, pct in zip(bars, porcentajes):
        valor = int(bar.get_width())
        valor_fmt = f"{valor:,}".replace(",", ".")
        ax.text(
            bar.get_width() + margen,
            bar.get_y() + bar.get_height() / 2,
            f"{valor_fmt} ({pct:.2f}%)",
            va="center",
            ha="left",
            fontsize=9.5,
            color="#333333"
        )

    # Ampliar margen derecho para que la etiqueta de la barra superior no se corte
    ax.set_xlim(0, top10_plot.max() * 1.24)

    plt.tight_layout()

    plt.savefig(variables.h3_1png, dpi=300)

    print("\nSe ha generado el gráfico:", variables.h3_1png )
    print("Top 10 tipologías de ciberdelincuencia (Acumulado histórico desde 2011 hasta 2025) \n")



    # gráfico 3_2

    # Agrupación para identificar las más frecuentes
    # datos por Tipo de Hecho sumando todo el histórico
    top_delitos = df_dataset3.groupby("Tipología penal")["Total"].sum().sort_values(ascending=False)
    #print("\nRanking acumulado de la tipología penal más frecuente", top_delitos)



    # Análisis de tendencias por año
    # Agrupamos por Año y Tipo de Hecho a nivel nacional
    df_tendencia = df_dataset3.groupby(["periodo", "Tipología penal"])["Total"].sum().unstack(fill_value=0)

    # print(df_tendencia)

    # tendencia 
    primer_anio = df_tendencia.index.min()
    #print(primer_anio)
    ultimo_anio = df_tendencia.index.max()
    #print(ultimo_anio)


    diferencia_absoluta = df_tendencia.loc[ultimo_anio] - df_tendencia.loc[primer_anio]

    # Clasificamos las tipologías según su evolución ascendente y descendente
    tipologias_crecientes = diferencia_absoluta[diferencia_absoluta > 0].sort_values(ascending=False).index.tolist()
    tipologias_decrecientes = diferencia_absoluta[diferencia_absoluta < 0].sort_values(ascending=True).index.tolist()

    print("\nNúmero de tipologías de ciberdelitos en aumento:", len(tipologias_crecientes))
    print("\nNúmero de tipologías de ciberdelitos que disminuyen:", len(tipologias_decrecientes))

    print("\nTipologías de ciberdelitos en aumento", tipologias_crecientes)
    print("\nTipologías de ciberdelitos que disminuyen:", tipologias_decrecientes)




    # Configuración visual
    sns.set_theme(style="whitegrid")
    plt.rcParams["figure.figsize"] = (14, 7)
    plt.figure(figsize=(14, 7))
    # Mostramos las 10 que más crecen 
    top_crecientes = tipologias_crecientes[:10]

    for delito in top_crecientes:
        plt.plot(df_tendencia.index, df_tendencia[delito], marker="o", linewidth=2.5, label=delito)

    # plt.title("Evolución de las tipologías de Ciberdelitos con mayor crecimiento (", + str(primer_anio), "-", + str(ultimo_anio), ")", fontsize=14, fontweight='bold')

    plt.title(f"Evolución de las tipologías de Ciberdelitos con mayor crecimiento ({primer_anio}-{ultimo_anio})", fontsize=14, fontweight="bold")
    plt.xlabel("Año", fontsize=12)
    plt.ylabel("Casos Conocidos Anuales", fontsize=12)
    plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title="Tipologías")
    plt.tight_layout()
    plt.savefig(variables.h3_2png, dpi=300)

    print("\nSe ha generado el gráfico:", variables.h3_2png )
    print("Evolución de las tipologías de Ciberdelitos con mayor crecimiento \n")


    #gráfico 3_3

    plt.figure(figsize=(14, 7))

    if len(tipologias_decrecientes) == 0:
        print("No se encontraron tipologías con descenso neto entre el año inicial y final global.")
        
        diferencia_ultimo_anio = df_tendencia.iloc[-1] - df_tendencia.iloc[-2]
        tipologias_decrecientes_ultimo = diferencia_ultimo_anio[diferencia_ultimo_anio < 0].sort_values().index.tolist()
        
        if tipologias_decrecientes_ultimo:
            for delito in tipologias_decrecientes_ultimo[:10]:
                plt.plot(df_tendencia.index, df_tendencia[delito], marker="o", linewidth=2.5, label=delito)
            plt.title(f"Tipologías de Ciberdelitos que más disminuyeron en el último año ({df_tendencia.index[-2]}-{df_tendencia.index[-1]})", fontsize=14, fontweight="bold")
    else:
        for delito in tipologias_decrecientes[:10]:
            plt.plot(df_tendencia.index, df_tendencia[delito], marker="o", linewidth=2.5, label=delito)
        plt.title(f"Evolución de las Tipologías de Ciberdelitos que más disminuyeron ({primer_anio}-{ultimo_anio})", fontsize=14, fontweight="bold")

    plt.xlabel("Año", fontsize=12)
    plt.ylabel("Casos Conocidos Anuales", fontsize=12)
    plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
    plt.legend(bbox_to_anchor=(1.05, 1), loc="upper left", title="Tipologías")
    plt.tight_layout()
    plt.savefig(variables.h3_3png, dpi=300)

    print("\nSe ha generado el gráfico:", variables.h3_3png )
    print("Evolución de las Tipologías de Ciberdelitos que más disminuyeron \n")

    return True