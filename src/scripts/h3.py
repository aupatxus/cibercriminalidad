

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



    print("\n\nDebido a reformas legales, en el registro estadístico en 2022–2023 se realizó una reclasificación de los nombres de tipologías:")
    print('- ACCESO ILEGAL INFORMÁTICO" registra datos de 2011 a 2022 y a partir de 2023 pasa a 0. En 2023 aparece "ACCESO ILEGAL A SISTEMAS INFORMÁTICOS" (que estaba a 0 hasta 2022). Es el mismo delito renombrado en el sistema estadístico.')
    print('- ATAQUES INFORMÁTICOS", "ATAQUES A DATOS O PROGRAMAS INFORMÁTICOS" y "ATAQUES A SISTEMAS INFORMÁTICOS" a partir de 2023 pasa a llamarse "ATAQUES A DATOS Y SISTEMAS INFORMÁTICOS".')
    print('-"ABUSO SEXUAL" pasa a 0 en 2023, "AGRESIÓN SEXUAL", "ABUSO SEXUAL CON PENETRACIÓN" y "AGRESIÓN SEXUAL CON PENETRACIÓN" tras la reforma del Código Penal (Ley del "solo sí es sí") se integran en "AGRESIÓN Y ABUSO SEXUAL".')
    print('-"ESTAFA BANCARIA" y "ESTAFAS CON TARJETAS DE CRÉDITO, DÉBITO Y CHEQUES DE VIAJE" se renombran a "ESTAFAS BANCARIAS Y CON TARJETAS/MEDIOS DE PAGO"\n')




    # Partimos del dataframe filtrado a nivel nacional (excluyendo el total general)
    df_limpio = df[
        (df["Comunidades autónomas"] == "TOTAL NACIONAL") & 
        (df["Tipología penal"] != "TOTAL tipo hecho")
    ].copy()

    # Diccionario de mapeo para unificar tipologías equivalentes o reclasificadas
    mapeo_tipologias = {
        # Accesos ilegales (renombrado en 2023)
        "ACCESO ILEGAL INFORMÁTICO": "ACCESO ILEGAL A SISTEMAS INFORMÁTICOS",
        
        # Ataques informáticos (desglosados/renombrados en 2023)
        "ATAQUES INFORMÁTICOS": "ATAQUES A DATOS Y SISTEMAS INFORMÁTICOS",
        "ATAQUES A DATOS O PROGRAMAS INFORMÁTICOS": "ATAQUES A DATOS Y SISTEMAS INFORMÁTICOS",
        "ATAQUES A SISTEMAS INFORMÁTICOS": "ATAQUES A DATOS Y SISTEMAS INFORMÁTICOS",
        
        # Reforma del Código Penal (unificación de abuso y agresión sexual en 2023)
        "ABUSO SEXUAL": "AGRESIÓN Y ABUSO SEXUAL",
        "AGRESIÓN SEXUAL": "AGRESIÓN Y ABUSO SEXUAL",
        "ABUSO SEXUAL CON PENETRACIÓN": "AGRESIÓN Y ABUSO SEXUAL CON PENETRACIÓN",
        "AGRESIÓN SEXUAL CON PENETRACIÓN": "AGRESIÓN Y ABUSO SEXUAL CON PENETRACIÓN",
        
        # Reclasificación de estafas bancarias y medios de pago en 2025
        "ESTAFA BANCARIA": "ESTAFAS BANCARIAS Y CON TARJETAS/MEDIOS DE PAGO",
        "ESTAFAS CON TARJETAS DE CRÉDITO, DÉBITO Y CHEQUES DE VIAJE": "ESTAFAS BANCARIAS Y CON TARJETAS/MEDIOS DE PAGO"
    }

    # Aplicamos el reemplazo de tipologías con .replace()
    df_limpio["Tipología penal"] = df_limpio["Tipología penal"].replace(mapeo_tipologias)



    # gráfico h3_1
    ranking_unificado = df_limpio.groupby("Tipología penal")["Total"].sum().sort_values(ascending=False)
    total_global = ranking_unificado.sum()

    top10_plot = ranking_unificado.head(10).sort_values(ascending=True)
    porcentajes = (top10_plot / total_global) * 100
    etiquetas_limpias = [textwrap.fill(str(nombre), width=42) for nombre in top10_plot.index]

    fig, ax = plt.subplots(figsize=(12, 7.5))
    colores = ["#8ab4d8"] * (len(top10_plot) - 1) + ["#1f4e78"]
    bars = ax.barh(etiquetas_limpias, top10_plot.values, color=colores, height=0.68)

    ax.set_title("Top 10 tipologías de ciberdelincuencia (Acumulado histórico 2011-2025)", fontsize=14, fontweight="bold", pad=15)
    ax.set_xlabel("Total de hechos conocidos", fontsize=11, labelpad=10)
    ax.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: f"{int(x):,}".replace(",", ".")))
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(axis="x", linestyle="--", alpha=0.4)

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

    ax.set_xlim(0, top10_plot.max() * 1.24)
    plt.tight_layout()


    plt.savefig(variables.h3_1png, dpi=300)

    print("\nSe ha generado el gráfico:", variables.h3_1png )
    print("Top 10 tipologías de ciberdelincuencia (Acumulado histórico desde 2011 hasta 2025) \n")



    # gráfico 3_2

    # Agrupación para identificar las más frecuentes
    # datos por Tipo de Hecho sumando todo el histórico
    
    df_tendencia_unificada = df_limpio.groupby(["periodo", "Tipología penal"])["Total"].sum().unstack(fill_value=0)

    primer_anio = df_tendencia_unificada.index.min()
    ultimo_anio = df_tendencia_unificada.index.max()
    diferencia_absoluta = df_tendencia_unificada.loc[ultimo_anio] - df_tendencia_unificada.loc[primer_anio]

    tipologias_crecientes = diferencia_absoluta[diferencia_absoluta > 0].sort_values(ascending=False).index.tolist()
    tipologias_decrecientes = diferencia_absoluta[diferencia_absoluta < 0].sort_values(ascending=True).index.tolist()

    print("\nNúmero de tipologías de ciberdelitos en aumento:", len(tipologias_crecientes))
    print("\nNúmero de tipologías de ciberdelitos que disminuyen:", len(tipologias_decrecientes))

    print("\nTipologías de ciberdelitos en aumento", tipologias_crecientes)
    print("\nTipologías de ciberdelitos que disminuyen:", tipologias_decrecientes)

  


    # Gráfica de mayor crecimiento

    sns.set_theme(style="whitegrid")

    plt.figure(figsize=(14, 7))
    for delito in tipologias_crecientes[:10]:
        plt.plot(df_tendencia_unificada.index, df_tendencia_unificada[delito], marker="o", linewidth=2.5, label=delito)

    plt.title(f"Evolución de las tipologías de los ciberdelitos con mayor crecimiento ({primer_anio}-{ultimo_anio})", fontsize=14, fontweight="bold")
    plt.xlabel("Año", fontsize=12)
    plt.ylabel("Casos Conocidos Anuales", fontsize=12)
    plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: f"{int(x):,}".replace(",", ".")))
    plt.legend(bbox_to_anchor=(1.05, 1), loc="upper left", title="Tipologías unificadas")
    plt.tight_layout()


    plt.savefig(variables.h3_2png, dpi=300)

    print("\nSe ha generado el gráfico:", variables.h3_2png )
    print("Evolución de las tipologías de Ciberdelitos con mayor crecimiento \n")




    #gráfico 3_3

    plt.figure(figsize=(14, 7))
    for delito in tipologias_decrecientes[:10]:
        plt.plot(df_tendencia_unificada.index, df_tendencia_unificada[delito], marker="o", linewidth=2.5, label=delito)

    plt.title(f"Evolución de las tipologías de los ciberdelitos que disminuyeron ({primer_anio}-{ultimo_anio})", fontsize=14, fontweight="bold")
    plt.xlabel("Año", fontsize=12)
    plt.ylabel("Casos Conocidos Anuales", fontsize=12)
    plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: f"{int(x):,}".replace(",", ".")))
    plt.legend(bbox_to_anchor=(1.05, 1), loc="upper left", title="Tipologías unificadas")
    plt.tight_layout()


    plt.savefig(variables.h3_3png, dpi=300)

    print("\nSe ha generado el gráfico:", variables.h3_3png )
    print("Evolución de las Tipologías de Ciberdelitos que más disminuyeron \n")

    return True