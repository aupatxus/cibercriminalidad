
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import textwrap
import seaborn as sns

import variables 

def h5():

    df_vic = pd.read_csv(variables.csv_5, sep=";", thousands=".")
    print("\nProcesando el csv:", variables.csv_5 )


    # Filtrados
    df_filtrado = df_vic[
        (df_vic["Comunidades autónomas"] != "TOTAL NACIONAL") & 
        (df_vic["Grupo penal"] != "TOTAL tipo hecho") &
        (df_vic["Grupo penal"] != "TOTAL grupo penal") &
        (df_vic["Sexo"] != "Total sexos" ) &
        (df_vic["Grupo edad"] != "TOTAL edad" ) 
    ]

    # Guardar el CSV 
    df_filtrado.to_csv(variables.csv_h5, sep=";")
    print("\nSe ha generado el dataset 5:", variables.csv_h5 )


    # Víctimas agrupadas por "Sexo" 
    vic_sexo = df_filtrado.groupby("Sexo")["Total"].sum().sort_values(ascending=False)

    vic_sexo_porcentaje = (vic_sexo / vic_sexo.sum() * 100).round()

    print("\nVíctimas agrupadas por Sexo")
    print(vic_sexo)
    print("\nVíctimas agrupadas por pocentajes según Sexo ")
    print(vic_sexo_porcentaje) 


    # Víctimas agrupadas por "Grupo edad"

    vic_edad = df_filtrado.groupby("Grupo edad")["Total"].sum()

    vic_edad_porcentaje = (vic_edad / vic_edad.sum() * 100).round()

    print("\nVíctimas agrupadas por Grupos de edad")
    print(vic_edad)
    print("\nVíctimas agrupadas por pocentajes según Grupos de edad ")
    print(vic_edad_porcentaje)



    # gráfico 5_1


    # Gráfico de Víctimas agrupadas por "Sexo" y Víctimas agrupadas por "Grupo edad" )
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5.5), gridspec_kw={"width_ratios": [1, 1.5]})

    # Sexo
    colores_sexo = ["#1f4e78", "#d95f02", "#7f7f7f"][:len(vic_sexo)]
    bars1 = ax1.bar(vic_sexo.index, vic_sexo.values, color=colores_sexo, width=0.5)
    ax1.set_title("Víctimas agrupadas por Sexo (2011–2025)", fontsize=13, fontweight="bold", pad=12)
    ax1.set_ylabel("Número de víctimas", fontsize=10.5)
    ax1.spines["top"].set_visible(False)
    ax1.spines["right"].set_visible(False)
    ax1.grid(axis="y", linestyle="--", alpha=0.4)

    for bar, pct in zip(bars1, vic_sexo_porcentaje.values):
        val = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2, val + (val*0.02),
                f"{val:,.0f}\n({pct}%)".replace(",", "."), ha="center", va="bottom", fontsize=9.5, fontweight="bold")
    ax1.set_ylim(0, vic_sexo.max() * 1.18)

    # Grupo Edad
    bars2 = ax2.bar(vic_edad.index, vic_edad.values, color="#4a7bb0", width=0.6)
    ax2.set_title("Víctimas agrupadas por Grupo de Edad (2011–2025)", fontsize=13, fontweight="bold", pad=12)
    ax2.spines["top"].set_visible(False)
    ax2.spines["right"].set_visible(False)
    ax2.grid(axis="y", linestyle="--", alpha=0.4)
    ax2.tick_params(axis="x", rotation=25)

    for bar, pct in zip(bars2, vic_edad_porcentaje.values):
        val = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2, val + (val*0.02),
                f"{pct}%", ha="center", va="bottom", fontsize=9.5, fontweight="bold")
    ax2.set_ylim(0, vic_edad.max() * 1.15)

    plt.tight_layout()

    plt.savefig(variables.h5_1png, dpi=300)

    print("\nSe ha generado los gráficos:", variables.h5_1png )
    print("Gráficos de Víctimas agrupadas por Sexo y Víctimas agrupadas por Grupo edad \n")


    # gráfico 5_2
    # Comparando Tipología Delictiva con el Sexo de las víctimas 

    # Tabla comparativa de Grupo Penal vs Sexo (% por fila)
    tabla_grupo_sexo = pd.pivot_table(
        df_filtrado, values="Total", index="Grupo penal", columns="Sexo", aggfunc="sum", fill_value=0
    )
    tabla_grupo_sexo_porcentaje = tabla_grupo_sexo.div(tabla_grupo_sexo.sum(axis=1), axis=0) * 100

    # Ordenar por porcentaje de mujeres (si existe la columna 'Mujeres')
    col_mujeres = [c for c in tabla_grupo_sexo_porcentaje.columns if "Femenino" in c][0]
    tabla_plot = tabla_grupo_sexo_porcentaje.sort_values(by=col_mujeres, ascending=True)

    etiquetas = [textwrap.fill(str(nombre), width=32) for nombre in tabla_plot.index]

    fig, ax = plt.subplots(figsize=(11, 6.5))
    left_acum = np.zeros(len(tabla_plot))
    paleta = {"Mujeres": "#d95f02", "Hombres": "#1f4e78"}

    for col in tabla_plot.columns:
        color = paleta.get(col)
        bars = ax.barh(etiquetas, tabla_plot[col], left=left_acum, label=col, color=color, height=0.65)
        
        # Etiquetar porcentajes mayores al 8% dentro de cada segmento
        for i, val in enumerate(tabla_plot[col]):
            if val >= 8:
                ax.text(left_acum[i] + val/2, i, f"{val:.0f}%", va="center", ha="center",
                        color="white", fontweight="bold", fontsize=9.5)
        left_acum += tabla_plot[col].values

    ax.axvline(50, color="#333333", linestyle="--", linewidth=1, alpha=0.7)
    ax.set_title("Tipología Delictiva comparada por Sexo de las víctimas según el Grupo Penal (2011–2025)", fontsize=14, fontweight="bold", pad=15)
    ax.set_xlabel("Proporción según el Sexo de las víctimas (%)", fontsize=11)
    ax.set_xlim(0, 100)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.legend(loc="center right", frameon=True)

    plt.tight_layout()

    plt.savefig(variables.h5_2png, dpi=300)

    print("\nSe ha generado el gráfico:", variables.h5_2png )
    print("Tipología Delictiva comparada por Sexo de las víctimas según el Grupo Penal (2011–2025) \n")

    return True


