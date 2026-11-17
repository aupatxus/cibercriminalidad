
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import variables 

def h1():
        
    df = pd.read_csv(variables.csv_1, sep=";", thousands=".")

    print("\nProcesando el csv:", variables.csv_1 )

    # Filtrado para obtener la evolución nacional por tipo de delito
    # Seleccionamos únicamente el TOTAL NACIONAL para ver la tendencia
    # Excluimos la fila que agrupa la suma de todos los delitos ("TOTAL grupo penal") para no duplicar datos
    df_dataset1 = df[
        (df["Comunidades autónomas"] == "TOTAL NACIONAL") & 
        (df["Grupo penal"] != "TOTAL grupo penal")
    ]

    df_dataset1 = df_dataset1[["periodo", "Grupo penal", "Total"]].sort_values(by=["periodo", "Total"], ascending=[False, False])

    df_dataset1.to_csv(variables.cvs_h1, index=False, sep=";")

    df_dataset1.groupby("Grupo penal")["Total"].sum().sort_values(ascending=False)

    print("\nSe ha generado el dataset 1:", variables.cvs_h1 )
    print(df_dataset1.groupby("Grupo penal")["Total"].sum().sort_values(ascending=False) )



    # gráfico 1_1: Evolución de la cibercriminalidad por grupo penal
    df_pivot = df_dataset1.pivot(index="periodo", columns="Grupo penal", values="Total").sort_index()
    # Ordenar columnas de mayor a menor volumen 
    orden_cols = df_pivot.sum().sort_values(ascending=False).index
    df_pivot = df_pivot[orden_cols]
    ax = df_pivot.plot(kind="bar", stacked=True, figsize=(12, 6), colormap="tab10", width=0.75)
    ax.set_title("Evolución de la cibercriminalidad por grupo penal", fontsize=14, pad=15)
    ax.set_xlabel("Año", fontsize=11)
    ax.set_ylabel("Hechos conocidos", fontsize=11)
    ax.legend(title="Grupo penal", bbox_to_anchor=(1.02, 1), loc="upper left")
    plt.xticks(rotation=45)
    plt.grid(axis="y", linestyle="--", alpha=0.4)
    plt.tight_layout()
    plt.savefig(variables.h1_1png, dpi=300)

    print("\nSe ha generado el gráfico:", variables.h1_1png )
    print("Evolución de la cibercriminalidad por grupo penal \n")



    # gráfico 1_2: Incremento absoluto anual y porcentual de nuevos casos de la Cibercriminalidad (2011-2025)

    df_anual = df.groupby("periodo")["Total"].sum().reset_index()
    # Calcular métricas de incremento anual y porcentual
    df_anual["Incremento_Absoluto"] = df_anual["Total"].diff()
    df_anual["Incremento_Porcentual"] = (df_anual["Total"].pct_change() * 100).round()

    # ¿Cuál ha sido el año con más ciberdelitos?
    anio_max = df_anual.loc[df_anual["Total"].idxmax()]
    print("El período con más ciberdelitos fue el año:", int(anio_max["periodo"]), "con:", int(anio_max["Total"]), "casos.")


    # ¿Cuándo se produjo el mayor incremento?

    # Mayor incremento absoluto
    max_inc_absoluto = df_anual.loc[df_anual["Incremento_Absoluto"].idxmax()]

    # Mayor incremento porcentual
    max_inc_porcentual = df_anual.loc[df_anual["Incremento_Porcentual"].idxmax()]

    print("Mayor incremento absoluto: El año", int(max_inc_absoluto["periodo"]), "con", + int(max_inc_absoluto["Incremento_Absoluto"]), "casos" )
    print("Mayor incremento porcentual: El año", int(max_inc_porcentual["periodo"]), "con el", + int(max_inc_porcentual["Incremento_Porcentual"]), "%")


    # ¿Existe algún año en el que hayan disminuido?
    disminuciones = df_anual[df_anual["Incremento_Absoluto"] < 0]
    if disminuciones.empty:
        print("No existe ningún año en el que los ciberdelitos hayan disminuido. El crecimiento de los ciberdelitos ha sido constante.")
    else:
        print("Años con disminución de ciberdelitos:")
        for _, row in disminuciones.iterrows():
            print("Año", int(row["periodo"]), ": Bajó en", + int(abs(row["Incremento_Absoluto"])), "casos.")


    # Gráfico de Incremento Año a Año 
    fig, ax1 = plt.subplots(figsize=(12, 6))
    plt.title("Incremento absoluto anual y porcentual de nuevos casos de la Cibercriminalidad (2011-2025)", fontsize=14, fontweight="bold")

    color = "teal"
    ax1.set_xlabel("Año", fontsize=12)
    ax1.set_ylabel("Incremento Absoluto (Casos nuevos)", color="black", fontsize=12)
    sns.barplot(data=df_anual.dropna(), x="periodo", y="Incremento_Absoluto", color=color, alpha=0.6, ax=ax1)
    ax1.tick_params(axis="y", labelcolor=color)
    # ax1.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
    ax1.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))

    # Línea para el incremento porcentual en el eje secundario
    ax2 = ax1.twinx()
    color = "darkorange"
    ax2.set_ylabel("Incremento Porcentual (%)", color="black", fontsize=12)
    sns.lineplot(data=df_anual.dropna(), x=df_anual.dropna().index - 1, y="Incremento_Porcentual", color=color, marker="s", linewidth=2, ax=ax2)
    ax2.tick_params(axis="y", labelcolor=color)
    plt.tight_layout()

    plt.savefig(variables.h1_2png, dpi=300)

    print("\nSe ha generado el gráfico:", variables.h1_2png )
    print("Incremento absoluto anual y porcentual de nuevos casos de la Cibercriminalidad (2011-2025) \n")


    return True