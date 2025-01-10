import marimo

__generated_with = "0.10.9"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md(
        r"""
        # Algoritmo Clonal con memoria inmunológica

        El algoritmo clonal con memoria inmunológica es un método de optimización que combina el algoritmo clonal propuesto por Castro con el mecanismo de memoria inmunológica. Esta memoria es capaz de recordar los antígenos previamente encontrados o, dicho de otro modo, las mejores soluciones obtenidas en ejecuciones anteriores.
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        ## Pseudocódigo

        El algoritmo clonal con memoria inmunológica se describe mediante el siguiente pseudocódigo:

        ```
        FUNCTION clonal_selection_with_memory(
            lymphocytes_count,
            antigenic_features,
            recognition_function,
            mutation_cycles,
            memory_rate
        ):

            // Initialize lymphocyte population
            lymphocytes = create_initial_lymphocytes(lymphocytes_count)

            // Retrieve immune memory if exists
            IF exists_in_memory(recognition_function):
                memory_lymphocytes = get_memory(recognition_function)
                memory_clones_count = lymphocytes_count * memory_rate
                clone_memory_lymphocytes(memory_lymphocytes, memory_clones_count)
                add_to_population(lymphocytes, memory_lymphocytes)

            best_lymphocyte = NULL
            best_affinity = INFINITY

            // Main maturation cycle
            FOR cycle IN mutation_cycles:
                affinities = calculate_affinity(lymphocytes, recognition_function)

                IF min(affinities) < best_affinity:
                    best_affinity = min(affinities)
                    best_lymphocyte = get_best_affinity_lymphocyte(lymphocytes, affinities)

                clones = clonal_expansion(lymphocytes, affinities)
                mutated = somatic_mutation(clones, affinities)
                lymphocytes = select_best(lymphocytes + mutated, lymphocytes_count)

            // Update immune memory
            save_to_memory(recognition_function, best_lymphocyte)

            RETURN best_lymphocyte, best_affinity
        ```
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        ## Análisis de Datos

        Se realizó una comparativa con el algoritmo clonal para evaluar las mejoras en la aproximación al valor óptimo y el tiempo de búsqueda.

        Para ello, se utilizaron las siguientes funciones _benchmark_:

        - Esfera
        - Ackley
        - Rastrigin
        - Griewank
        - Rosenbrock
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        ### Extracción de Datos

        Se inició con la extracción de los datos mediante la parametrización de ambos algoritmos. Esto implicó combinar los diferentes valores posibles para cada parámetro, con el objetivo de evaluar los algoritmos bajo diversas circunstancias.

        Los parámetros parametrizados son los siguientes:

        - antigenic_feature_count: Dimensionalidad del vector solución.
        - somatic_hypermutation_cycle: Número de generaciones a ejecutar.
        - clonal_expansion_factor: Factor de clonación de las mejores soluciones.
        - somatic_hypermutation_rate: Probabilidad de mutación en las soluciones clonadas.
        - antigenic_recognition_function: Función benchmark a evaluar.

        Cabe mencionar que existen otros parámetros también parametrizados, pero sus valores dependen de otros, como los siguientes:

        - _antigenic_feature_range_: Espacio de búsqueda dentro de la función _benchmark_. Está relacionado con el parámetro _**antigenic_recognition_function**_.
        - _lymphocytes_count_: Tamaño de la población, ligado al parámetro _**antigenic_feature_range**_ en una proporción 1 a 100.

        Por otro lado, el algoritmo clonal con memoria inmunológica requiere parámetros adicionales, que son los siguientes:

        immune_responses: Número de veces que se reejecutará el algoritmo.
        immune_memory_count: Proporción respecto al tamaño de la población de linfocitos inicial, de los que se introducirán en la primera generación de clones de la mejor solución obtenida en la ejecución anterior.

        Finalmente, se recopiló la parametrización de cada ejecución de los algoritmos, junto con la mejor solución obtenida, la evaluación más alta de la solución y el tiempo empleado en cada ejecución.
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        ### Análisis de Datos

        Una vez extraídos los datos, el análisis de los mismos resultó ser el paso más desafiante del proceso. Aunque los datos estaban disponibles en su forma cruda, resultaba complicado encontrar una manera justa de compararlos que permitiera obtener resultados confiables, justificables, y sin perder exactitud debido a la sobre agrupación.

        Por ello, se decidió realizar un análisis de las funciones benchmark que permitiera justificar la primera agrupación de los datos, la cual podría parecer obvia a simple vista. 

        Se comenzó con una comparativa visual de las funciones benchmark, observando tanto su espacio de búsqueda como su forma geométrica, acompañado con información teórica: su valor mínimo (optimo) y su espacio de busqueda.
        """
    )
    return


@app.cell
def _():
    FUNCTIONS = [
        "sphere",
        "ackley",
        "rastrigin",
        "griewank",
        "rosenbrock",
    ]

    FUNCTION_NAME = {
        "sphere": "Esfera",
        "ackley": "Ackley",
        "rastrigin": "Rastrigin",
        "griewank": "Griewank",
        "rosenbrock": "Rosenbrock",
    }

    FUNCTION_SEARCH_SPACE = {
        "sphere": (-100, 100),
        "ackley": (-32.768, 32.768),
        "rastrigin": (-5.12, 5.12),
        "griewank": (-100, 100),
        "rosenbrock": (-10, 10),
    }
    return FUNCTIONS, FUNCTION_NAME, FUNCTION_SEARCH_SPACE


@app.cell
def _(FUNCTIONS, mo):
    function_dropdown = mo.ui.dropdown(
        FUNCTIONS, value=FUNCTIONS[0], label="Escoge una función", full_width=True
    )
    function_dropdown.callout()
    return (function_dropdown,)


@app.cell
def _(function_dropdown):
    function = function_dropdown.value
    return (function,)


@app.cell
def _(FUNCTION_NAME, FUNCTION_SEARCH_SPACE, function, mo):
    None if function is None else mo.vstack(
        [
            mo.md(f"#### {FUNCTION_NAME[function]}").center(),
            mo.hstack(
                [
                    mo.image(f"./resources/images/{function}.png").center(),
                    mo.md(
                        f"""
                        ##### Caracteristicas:  

                        - Espacio de busqueda: {FUNCTION_SEARCH_SPACE[function]}
                        - Valor óptimo: 0
                        """
                    ),
                ],
                justify="center",
            ),
        ]
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        La comparativa revela diferencias geométricas significativas. Sin embargo, se decidió realizar un análisis visual de ambos conjuntos de datos (resultados del algoritmo clonal y del algoritmo clonal con memoria inmunológica) para respaldar estas inferencias.

        Antes de realizar este análisis, nos enfrentamos a un desafío importante: ¿cómo graficar los datos? Afortunadamente, dado que solo contamos con dos variables independientes—el mejor valor y el tiempo de búsqueda—podemos representar ambas en un gráfico de 'mejor valor' contra 'tiempo tomado'. Además, podremos colorear los puntos según la función benchmark utilizada, lo que nos permitirá visualizar de manera más clara las relaciones entre las variables.
        """
    )
    return


@app.cell
def _(altair, clonal_data, mo):
    mo.vstack(
        [
            mo.md(
                "#### Grafica de dispersión del la información del algoritmo clonal"
            ),
            mo.ui.altair_chart(
                altair.Chart(clonal_data)
                .encode(
                    x=altair.X(
                        "elapsed_time",
                        scale=altair.Scale(type="log", nice=True),
                    ),
                    y=altair.Y(
                        "best_fitness:Q", scale=altair.Scale(type="log", nice=True)
                    ),
                    color=altair.Color("antigen_recognition_function:N"),
                )
                .mark_point()
            ),
        ]
    )
    return


@app.cell
def _(altair, clonal_with_memory_raw_data, mo):
    mo.vstack(
        [
            mo.md(
                "#### Grafica de dispersión del la información del algoritmo clonal con memoria inmunológica"
            ),
            mo.ui.altair_chart(
                altair.Chart(clonal_with_memory_raw_data)
                .encode(
                    x=altair.X(
                        "elapsed_time", scale=altair.Scale(type="log", nice=True)
                    ),
                    y=altair.Y(
                        "best_fitness:Q", scale=altair.Scale(type="log", nice=True)
                    ),
                    color=altair.Color("antigen_recognition_function:N"),
                )
                .mark_point()
                .interactive()
            ),
        ]
    )
    return


@app.cell
def _(mo):
    mo.md(r"""A partir del análisis visual de los datos, se observa una diferencia entre las regiones correspondientes a los diferentes grupos creados por las funciones benchmark. Para completar la inferencia, se optó por aplicar un análisis de varianza (ANOVA) con el fin de determinar si las diferencias entre los grupos formados por las funciones benchmark son estadísticamente significativas, lo que significaria que no podriamos compararlos entre sí.""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        #### Análisis de Varianza sobre los grupos creados por antigen_recognition_function (funciones benchmark)

        Para llevar a cabo este análisis, se debe agrupar la información según la propiedad antigen_recognition_function, que codifica la función de referencia utilizada. A continuación, se extraen tanto las propiedades de mejor valor como los tiempos de búsqueda, y finalmente se aplica la prueba a estos grupos.
        """
    )
    return


@app.cell
def _(clonal_data, f_oneway, mo):
    _groups = clonal_data.groupby("antigen_recognition_function")
    _groups_bests_fitness = [
        _group["best_fitness"].values for _group_key, _group in _groups
    ]

    _groups_result = f_oneway(*_groups_bests_fitness)

    mo.vstack(
        [
            mo.md(
                "Al aplicar las prueba anova respecto al mejor valor en el conjunto de datos de algoritmo clonal obtuvimos los siguientes resultados:"
            ),
            mo.hstack(
                [
                    mo.stat(
                        value=str(_groups_result.statistic),
                        label="Valor estadistico",
                    ),
                    mo.stat(value=str(_groups_result.pvalue), label="Valor p"),
                ]
            ),
            mo.md(
                """
    ##### Interpretación.  
    Un valor estadístico alto y un valor p extremadamente bajo, menor a un alfa de 0.01, indican una diferencia significativa entre las varianzas de los grupos. Esto sugiere que la función benchmark tiene un impacto significativo en el elapsed_time y no es producto del azar.
                """
            ).callout(),
        ]
    )
    return


@app.cell
def _(clonal_data, f_oneway, mo):
    _groups = clonal_data.groupby("antigen_recognition_function")
    _groups_bests_fitness = [
        _group["elapsed_time"].values for _group_key, _group in _groups
    ]

    _groups_result = f_oneway(*_groups_bests_fitness)

    mo.vstack(
        [
            mo.md(
                "Ahora, aplicando el anova respecto al tiempo de busqueda en el conjunto de datos de algoritmo clonal obtuvimos los siguientes resultados:"
            ),
            mo.hstack(
                [
                    mo.stat(
                        value=str(_groups_result.statistic),
                        label="Valor estadistico",
                    ),
                    mo.stat(value=str(_groups_result.pvalue), label="Valor p"),
                ]
            ),
            mo.md(
                """
    ##### Interpretación.  
    Un valor estadístico alto y un valor p extremadamente bajo, menor a un alfa de 0.01, indican una diferencia significativa entre las varianzas de los grupos. Esto sugiere que la función benchmark tiene un impacto significativo en el best_fitness y no es producto del azar.
                """
            ).callout(),
        ]
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        Los resultados de estas pruebas revelan una diferencia significativa entre las varianzas de los grupos, lo que nos permite inferir que no es adecuado compararlos directamente. Sin embargo, agrupar la información según esta propiedad permitirá formar grupos que sí podrán ser comparados de manera válida.

        Ahora bien, es tiempo de aplicar las mismas pruebas sobre el conjunto de datos del algoritmo clonal con memoria inmmunológica.
        """
    )
    return


@app.cell
def _(clonal_with_memory_raw_data, f_oneway, mo):
    _groups = clonal_with_memory_raw_data.groupby("antigen_recognition_function")
    _groups_bests_fitness = [
        _group["best_fitness"].values for _group_key, _group in _groups
    ]

    _groups_result = f_oneway(*_groups_bests_fitness)

    mo.vstack(
        [
            mo.hstack(
                [
                    mo.stat(
                        value=str(_groups_result.statistic),
                        label="Valor estadistico",
                    ),
                    mo.stat(value=str(_groups_result.pvalue), label="Valor p"),
                ]
            ),
        ]
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        El resultado obtenido tras la prueba anterior fue sorprendente, ya que el valor P es 0, un valor extremadamente bajo, junto con un valor estadistico muy alto. Fue en ese momento cuando nos dimos cuenta de que los datos utilizados no habían sido limpiados y procedimos a hacerlo.

        El proceso consistió en eliminar columnas innecesarias y acumular las columnas relacionadas. Debido a que el algoritmo clonal con memoria inmunológica, requiere más iteraciones para mostrar mejoras, dado que su mecanismo depende de un aprendizaje acumulativo. Por lo tanto, se eliminaron las iteraciones intermedias en el conjunto de datos. Es decir, si una prueba constaba de 10 ejecuciones, solo se conservó el registro de la última iteración, acumulando los datos relevantes, como el tiempo total transcurrido.

        Visualizando nuevamente los datos podemos notar la diferencia:
        """
    )
    return


@app.cell
def _(altair, clonal_with_memory_data, mo):
    mo.vstack(
        [
            mo.md(
                "#### Grafica de dispersión del la información del algoritmo clonal con memoria inmunológica"
            ),
            mo.ui.altair_chart(
                altair.Chart(clonal_with_memory_data)
                .encode(
                    x=altair.X(
                        "elapsed_time", scale=altair.Scale(type="log", nice=True)
                    ),
                    y=altair.Y(
                        "best_fitness:Q", scale=altair.Scale(type="log", nice=True)
                    ),
                    color=altair.Color("antigen_recognition_function:N"),
                )
                .mark_point()
                .interactive()
            ),
        ]
    )
    return


@app.cell
def _(clonal_with_memory_data, f_oneway, mo):
    _groups = clonal_with_memory_data.groupby("antigen_recognition_function")
    _groups_bests_fitness = [
        _group["best_fitness"].values for _group_key, _group in _groups
    ]

    _groups_result = f_oneway(*_groups_bests_fitness)

    mo.vstack(
        [
            mo.md(
                "Ahora, ejecutando nuevamente la prueba anova sobre los datos limpios obtenemos los siguientes resultados:"
            ),
            mo.hstack(
                [
                    mo.stat(
                        value=str(_groups_result.statistic),
                        label="Valor estadistico",
                    ),
                    mo.stat(value=str(_groups_result.pvalue), label="Valor p"),
                ]
            ),
        ]
    )
    return


@app.cell
def _(mo):
    mo.md(r"""Observamos resultados más consistentes con las pruebas realizadas con anterioridad. Por lo que seguimos a realizar la siguiente prueba anova relacionada con el tiempo de busqueda.""")
    return


@app.cell
def _(clonal_with_memory_data, f_oneway, mo):
    _groups = clonal_with_memory_data.groupby("antigen_recognition_function")
    _groups_bests_fitness = [
        _group["elapsed_time"].values for _group_key, _group in _groups
    ]

    _groups_result = f_oneway(*_groups_bests_fitness)

    mo.vstack(
        [
            mo.hstack(
                [
                    mo.stat(
                        value=str(_groups_result.statistic),
                        label="Valor estadistico",
                    ),
                    mo.stat(value=str(_groups_result.pvalue), label="Valor p"),
                ]
            ),
        ]
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        Observamos que las funciones benchmark tienen una mayor influencia en el tiempo de búsqueda. A partir de esta prueba, concluimos que el campo _antigen_recognition_function_ puede utilizarse para agrupar los datos y posteriormente comparar los diferentes conjuntos.

        La siguiente pregunta es: ¿qué parámetros podemos utilizar para agrupar a partir de lo recién inferido? La respuesta corta radica en la relación intrínseca entre la función benchmark y la dimensionalidad, la cual está representada por el parámetro antigenic_feature_count. Este parámetro, como se mencionó anteriormente, define el tamaño del vector solución de la función benchmark y, a su vez, determina el tamaño de la población en una proporción de 1 a 100.

        Primero, y al igual que con la variable pasada, realizamos un análisi visual, agregando una agrupación extra a la visualización.
        """
    )
    return


@app.cell
def _(altair, clonal_data, mo):
    mo.vstack(
        [
            mo.md(
                "#### Grafica de dispersión del la información del algoritmo clonal"
            ),
            mo.ui.altair_chart(
                altair.Chart(clonal_data)
                .encode(
                    x=altair.X(
                        "elapsed_time",
                        scale=altair.Scale(type="log", nice=True),
                    ),
                    y=altair.Y(
                        "best_fitness:Q", scale=altair.Scale(type="log", nice=True)
                    ),
                    color=altair.Color("antigen_recognition_function:N"),
                    shape=altair.Shape("antigenic_feature_count:O"),
                )
                .mark_point()
            ),
        ]
    )
    return


@app.cell
def _(altair, clonal_with_memory_data, mo):
    mo.vstack(
        [
            mo.md(
                "#### Grafica de dispersión del la información del algoritmo clonal con memoria inmunológica"
            ),
            mo.ui.altair_chart(
                altair.Chart(clonal_with_memory_data)
                .encode(
                    x=altair.X(
                        "elapsed_time", scale=altair.Scale(type="log", nice=True)
                    ),
                    y=altair.Y(
                        "best_fitness:Q", scale=altair.Scale(type="log", nice=True)
                    ),
                    color=altair.Color("antigen_recognition_function:N"),
                    shape=altair.Shape("antigenic_feature_count:O"),
                )
                .mark_point()
                .interactive()
            ),
        ]
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        Análizando la comparativa y explorando las visualizaciónes podemos observar que los conjunto de datos agrupados tanto por antigen_recognition_function, como por antigenic_feature_count presentan cambios, tanto en el mejor valor, como en el tiempo de busqueda. Por lo cual procedemos a hacer las pruebas anovas sobre las nuevas agrupaciones para tener un sustento estadistico.

        #### Análisis de Varianza sobre los grupos creados por antigenic_feature_count (funciones benchmark)

        Es importante destacar que, a diferencia de pruebas anteriores, estos nuevos grupos solo pueden compararse entre datos que compartan la misma función benchmark. Como se concluyó anteriormente, la diferencia entre las varianzas es tan significativa que cualquier comparación sería injusta. Por esta razón, las pruebas ANOVA deben realizarse inter-grupales,. En otras palabras, es necesario separar los datos por funciones benchmark diferentes y luego agruparlos nuevamente según el parámetro antigenic_feature_count. Por lo que ahora tendremos una tabla con cinco pruebas, una por cada función.

        Empezando por el conjunto de datos del algoritmo clonal, obtuvimos los siguientes resultados:
        """
    )
    return


@app.cell
def _(FUNCTIONS, clonal_data, f_oneway, mo):
    _results = []

    for _function in FUNCTIONS:
        _groups = clonal_data.groupby("antigen_recognition_function")
        _group = _groups.get_group(_function)

        _inter_group = _group.groupby("antigenic_feature_count")

        _groups_bests_fitness = [
            _group["best_fitness"].values for _group_key, _group in _inter_group
        ]

        _groups_result = f_oneway(*_groups_bests_fitness)

        _results.append(
            {
                "antigen_recognition_function": _function,
                "statistic": _groups_result.statistic,
                "p": _groups_result.pvalue,
            }
        )

    mo.ui.table(_results)
    return


@app.cell
def _(mo):
    mo.md(r"""Siguiend, se realizaron las pruebas sobre el conjunto de datos del algoritmo clonal con memoria inmunológica, obteniendo lo siguiente:""")
    return


@app.cell
def _(FUNCTIONS, clonal_with_memory_data, f_oneway):
    _results = []

    for _function in FUNCTIONS:
        _groups = clonal_with_memory_data.groupby("antigen_recognition_function")
        _group = _groups.get_group(_function)

        _inter_group = _group.groupby("antigenic_feature_count")

        _groups_bests_fitness = [
            _group["best_fitness"].values for _group_key, _group in _inter_group
        ]

        _groups_result = f_oneway(*_groups_bests_fitness)

        _results.append(
            {
                "antigen_recognition_function": _function,
                "statistic": _groups_result.statistic,
                "p": _groups_result.pvalue,
            }
        )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        En ambas tablas se observan valores p notablemente bajos, lo que sugiere una marcada diferencia entre las varianza de los grupos inter-grupos. Esto implica que antigenic_feature_count puede servir como una subdivisión para hacer comparaciones.

        Ahora debemos analizar las variables restantes: somatic_hypermutation_cycles, somatic_hypermutation_rate y clonal_expansion_factor. Aunque es posible seguir realizando subagrupaciones, esto podría ocasionar una pérdida de precisión en las comparaciones. Actualmente, el dataset del algoritmo clonal cuenta con 540 registros, y al subdividirlo según las agrupaciones actuales (antigen_recognition_function y antigenic_feature_count), se obtienen grupos de 36 registros. Este nivel de subdivisión podría afectar negativamente la comparación final si seguimos agrupando. Por ello, es preferible evaluar cuidadosamente si las variables mencionadas deben incluirse como criterios adicionales de agrupación.
        """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""Comenzando con un análisis visual, se generaron gráficos de dispersión para las funciones benchmark de forma individual, lo que permitió una evaluación más clara y detallada.""")
    return


@app.cell
def _(FUNCTIONS, mo):
    plot_function_dropdown = mo.ui.dropdown(
        FUNCTIONS, full_width=True, label="Escoge una función", value=FUNCTIONS[0]
    )
    plot_function_dropdown.callout()
    return (plot_function_dropdown,)


@app.cell
def _(plot_function_dropdown):
    plot_function = plot_function_dropdown.value
    return (plot_function,)


@app.cell
def _(altair, clonal_data, mo, plot_function):
    _groups = clonal_data.groupby("antigen_recognition_function")
    _group = _groups.get_group(plot_function)

    mo.vstack(
        [
            mo.md(
                "#### Graficas de dispersión del la información del algoritmo clonal con memoria inmunológica"
            ),
            mo.ui.altair_chart(
                altair.Chart(_group)
                .encode(
                    x=altair.X(
                        "elapsed_time",
                        scale=altair.Scale(
                            type="log",
                            nice=True,
                        ),
                    ),
                    y=altair.Y(
                        "best_fitness:Q", scale=altair.Scale(type="log", nice=True)
                    ),
                    color=altair.Color("antigenic_feature_count:O"),
                    size=altair.Size("somatic_hypermutation_cycles:O"),
                    shape=altair.value("diamond"),
                )
                .mark_point()
                .interactive()
            ),
            mo.ui.altair_chart(
                altair.Chart(_group)
                .encode(
                    x=altair.X(
                        "elapsed_time", scale=altair.Scale(type="log", nice=True)
                    ),
                    y=altair.Y(
                        "best_fitness:Q", scale=altair.Scale(type="log", nice=True)
                    ),
                    color=altair.Color("antigenic_feature_count:O"),
                    size=altair.Size("somatic_hypermutation_rate:O"),
                    shape=altair.value("triangle"),
                )
                .mark_point()
                .interactive()
            ),
            mo.ui.altair_chart(
                altair.Chart(_group)
                .encode(
                    x=altair.X(
                        "elapsed_time", scale=altair.Scale(type="log", nice=True)
                    ),
                    y=altair.Y(
                        "best_fitness:Q", scale=altair.Scale(type="log", nice=True)
                    ),
                    color=altair.Color("antigenic_feature_count:O"),
                    size=altair.Size("clonal_expansion_factor:O"),
                    shape=altair.value("square"),
                )
                .mark_point()
                .interactive()
            ),
        ]
    )
    return


@app.cell
def _(mo):
    mo.md(r"""Así como para el conjunto de datos del algoritmo clonal con memoria inmunológica""")
    return


@app.cell
def _(altair, clonal_with_memory_data, mo, plot_function):
    _groups = clonal_with_memory_data.groupby("antigen_recognition_function")
    _group = _groups.get_group(plot_function)

    mo.vstack(
        [
            mo.md(
                "#### Graficas de dispersión del la información del algoritmo clonal con memoria inmunológica"
            ),
            mo.ui.altair_chart(
                altair.Chart(_group)
                .encode(
                    x=altair.X(
                        "elapsed_time",
                        scale=altair.Scale(
                            type="log",
                            nice=True,
                        ),
                    ),
                    y=altair.Y(
                        "best_fitness:Q", scale=altair.Scale(type="log", nice=True)
                    ),
                    color=altair.Color("antigenic_feature_count:O"),
                    size=altair.Size("somatic_hypermutation_rate:O"),
                    shape=altair.value("diamond"),
                )
                .mark_point()
                .interactive()
            ),
            mo.ui.altair_chart(
                altair.Chart(_group)
                .encode(
                    x=altair.X(
                        "elapsed_time", scale=altair.Scale(type="log", nice=True)
                    ),
                    y=altair.Y(
                        "best_fitness:Q", scale=altair.Scale(type="log", nice=True)
                    ),
                    color=altair.Color("antigenic_feature_count:O"),
                    size=altair.Size("somatic_hypermutation_rate:O"),
                    shape=altair.value("triangle"),
                )
                .mark_point()
                .interactive()
            ),
            mo.ui.altair_chart(
                altair.Chart(_group)
                .encode(
                    x=altair.X(
                        "elapsed_time", scale=altair.Scale(type="log", nice=True)
                    ),
                    y=altair.Y(
                        "best_fitness:Q", scale=altair.Scale(type="log", nice=True)
                    ),
                    color=altair.Color("antigenic_feature_count:O"),
                    size=altair.Size("clonal_expansion_factor:O"),
                    shape=altair.value("square"),
                )
                .mark_point()
                .interactive()
            ),
        ]
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        En las gráficas de dispersión, se observa que la varianza entre los grupos no presenta cambios significativos en comparación con otras variables. Esto sugiere que no es necesario realizar una agrupación más detallada.

        Aun así se hace las pruebas anovas correspondientes para dar fundamento a estas observaciones.
        """
    )
    return


@app.cell
def _(FUNCTIONS, clonal_data, f_oneway, mo):
    _results = []

    for _function in FUNCTIONS:
        _groups = clonal_data.groupby("antigen_recognition_function")
        _group = _groups.get_group(_function)

        _inter_groups = _group.groupby("antigenic_feature_count")

        for _inter_inter_group_key, _inter_inter_group in _inter_groups:
            _iii_groups = _inter_inter_group.groupby("somatic_hypermutation_rate")
            _groups_bests_fitness = [
                _iii_group["best_fitness"].values
                for _iii_group_key, _iii_group in _iii_groups
            ]

            _groups_result = f_oneway(*_groups_bests_fitness)

            _results.append(
                {
                    "antigenic_feature_count": _inter_inter_group_key,
                    "antigen_recognition_function": _function,
                    "statistic": _groups_result.statistic,
                    "p": _groups_result.pvalue,
                }
            )

    mo.vstack(
        [
            mo.md(
                "##### Tabla de resultados de ANOVAS de somatic_hypermutation_rate sobre best_fitness para algoritmo clonal"
            ),
            mo.ui.table(_results),
        ]
    )

    return


@app.cell
def _(FUNCTIONS, clonal_with_memory_data, f_oneway, mo):
    _results = []

    for _function in FUNCTIONS:
        _groups = clonal_with_memory_data.groupby("antigen_recognition_function")
        _group = _groups.get_group(_function)

        _inter_groups = _group.groupby("antigenic_feature_count")

        for _inter_inter_group_key, _inter_inter_group in _inter_groups:
            _iii_groups = _inter_inter_group.groupby("somatic_hypermutation_rate")
            _groups_bests_fitness = [
                _iii_group["best_fitness"].values
                for _iii_group_key, _iii_group in _iii_groups
            ]

            _groups_result = f_oneway(*_groups_bests_fitness)

            _results.append(
                {
                    "antigenic_feature_count": _inter_inter_group_key,
                    "antigen_recognition_function": _function,
                    "statistic": _groups_result.statistic,
                    "p": _groups_result.pvalue,
                }
            )

    mo.vstack(
        [
            mo.md(
                "##### Tabla de resultados de ANOVAS de somatic_hypermutation_rate sobre best_fitnesss para algoritmo clonal con memoria inmunológica"
            ),
            mo.ui.table(_results),
        ]
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        En comparación con los resultados obtenidos en otras pruebas ANOVA a lo largo del análisis, observamos valores estadísticos y valores p elevados, lo que respalda nuestras afirmaciones.

        Enseguida abordaremos las pruebas para las variables restantes.
        """
    )
    return


@app.cell
def _(FUNCTIONS, clonal_data, f_oneway, mo):
    _results = []

    for _function in FUNCTIONS:
        _groups = clonal_data.groupby("antigen_recognition_function")
        _group = _groups.get_group(_function)

        _inter_groups = _group.groupby("antigenic_feature_count")

        for _inter_inter_group_key, _inter_inter_group in _inter_groups:
            _iii_groups = _inter_inter_group.groupby(
                "somatic_hypermutation_cycles"
            )
            _groups_bests_fitness = [
                _iii_group["best_fitness"].values
                for _iii_group_key, _iii_group in _iii_groups
            ]

            _groups_result = f_oneway(*_groups_bests_fitness)

            _results.append(
                {
                    "antigenic_feature_count": _inter_inter_group_key,
                    "antigen_recognition_function": _function,
                    "statistic": _groups_result.statistic,
                    "p": _groups_result.pvalue,
                }
            )

    mo.vstack(
        [
            mo.md(
                "##### Tabla de resultados de ANOVAS de somatic_hypermutation_cycles sobre best_fitnesss para algoritmo clonal"
            ),
            mo.ui.table(_results),
        ]
    )
    return


@app.cell
def _(FUNCTIONS, clonal_with_memory_data, f_oneway, mo):
    _results = []

    for _function in FUNCTIONS:
        _groups = clonal_with_memory_data.groupby("antigen_recognition_function")
        _group = _groups.get_group(_function)

        _inter_groups = _group.groupby("antigenic_feature_count")

        for _inter_inter_group_key, _inter_inter_group in _inter_groups:
            _iii_groups = _inter_inter_group.groupby(
                "somatic_hypermutation_cycles"
            )
            _groups_bests_fitness = [
                _iii_group["best_fitness"].values
                for _iii_group_key, _iii_group in _iii_groups
            ]

            _groups_result = f_oneway(*_groups_bests_fitness)

            _results.append(
                {
                    "antigenic_feature_count": _inter_inter_group_key,
                    "antigen_recognition_function": _function,
                    "statistic": _groups_result.statistic,
                    "p": _groups_result.pvalue,
                }
            )

    mo.vstack(
        [
            mo.md(
                "##### Tabla de resultados de ANOVAS de somatic_hypermutation_cycles sobre best_fitnesss para algoritmo clonal con memoria inmunológica"
            ),
            mo.ui.table(_results),
        ]
    )
    return


@app.cell
def _(FUNCTIONS, clonal_data, f_oneway, mo):
    _results = []

    for _function in FUNCTIONS:
        _groups = clonal_data.groupby("antigen_recognition_function")
        _group = _groups.get_group(_function)

        _inter_groups = _group.groupby("antigenic_feature_count")

        for _inter_inter_group_key, _inter_inter_group in _inter_groups:
            _iii_groups = _inter_inter_group.groupby("clonal_expansion_factor")
            _groups_bests_fitness = [
                _iii_group["best_fitness"].values
                for _iii_group_key, _iii_group in _iii_groups
            ]

            _groups_result = f_oneway(*_groups_bests_fitness)

            _results.append(
                {
                    "antigenic_feature_count": _inter_inter_group_key,
                    "antigen_recognition_function": _function,
                    "statistic": _groups_result.statistic,
                    "p": _groups_result.pvalue,
                }
            )

    mo.vstack(
        [
            mo.md(
                "##### Tabla de resultados de ANOVAS de clonal_expansion_factor sobre best_fitnesss para algoritmo clonal"
            ),
            mo.ui.table(_results),
        ]
    )
    return


@app.cell
def _(FUNCTIONS, clonal_with_memory_data, f_oneway, mo):
    _results = []

    for _function in FUNCTIONS:
        _groups = clonal_with_memory_data.groupby("antigen_recognition_function")
        _group = _groups.get_group(_function)

        _inter_groups = _group.groupby("antigenic_feature_count")

        for _inter_inter_group_key, _inter_inter_group in _inter_groups:
            _iii_groups = _inter_inter_group.groupby("clonal_expansion_factor")
            _groups_bests_fitness = [
                _iii_group["best_fitness"].values
                for _iii_group_key, _iii_group in _iii_groups
            ]

            _groups_result = f_oneway(*_groups_bests_fitness)

            _results.append(
                {
                    "antigenic_feature_count": _inter_inter_group_key,
                    "antigen_recognition_function": _function,
                    "statistic": _groups_result.statistic,
                    "p": _groups_result.pvalue,
                }
            )

    mo.vstack(
        [
            mo.md(
                "##### Tabla de resultados de ANOVAS de clonal_expansion_factor sobre best_fitnesss para algoritmo clonal con memoria inmunológica"
            ),
            mo.ui.table(_results),
        ]
    )
    return


@app.cell
def _(mo):
    mo.md(r"""Tras comparar las diferentes tablas, podemos afirmar que las tres últimas variables no tienen un impacto tan significativo como las primeras variables analizadas. Por lo tanto, pueden ser omitidas en la agrupación para la comparación del best_fitness entre los conjuntos de datos. A continuación, se procederá a realizar el mismo análisis, pero sobre el elapsed_time, ya que es nuestra segunda variable independiente.""")
    return


@app.cell
def _(FUNCTIONS, clonal_data, f_oneway, mo):
    _results = []

    for _function in FUNCTIONS:
        _groups = clonal_data.groupby("antigen_recognition_function")
        _group = _groups.get_group(_function)

        _inter_groups = _group.groupby("antigenic_feature_count")

        for _inter_inter_group_key, _inter_inter_group in _inter_groups:
            _iii_groups = _inter_inter_group.groupby("somatic_hypermutation_rate")
            _groups_bests_fitness = [
                _iii_group["elapsed_time"].values
                for _iii_group_key, _iii_group in _iii_groups
            ]

            _groups_result = f_oneway(*_groups_bests_fitness)

            _results.append(
                {
                    "antigenic_feature_count": _inter_inter_group_key,
                    "antigen_recognition_function": _function,
                    "statistic": _groups_result.statistic,
                    "p": _groups_result.pvalue,
                }
            )

    mo.vstack(
        [
            mo.md(
                "##### Tabla de resultados de ANOVAS de somatic_hypermutation_rate sobre elapsed_time para algoritmo clonal"
            ),
            mo.ui.table(_results),
        ]
    )
    return


@app.cell
def _(FUNCTIONS, clonal_with_memory_data, f_oneway, mo):
    _results = []

    for _function in FUNCTIONS:
        _groups = clonal_with_memory_data.groupby("antigen_recognition_function")
        _group = _groups.get_group(_function)

        _inter_groups = _group.groupby("antigenic_feature_count")

        for _inter_inter_group_key, _inter_inter_group in _inter_groups:
            _iii_groups = _inter_inter_group.groupby("somatic_hypermutation_rate")
            _groups_bests_fitness = [
                _iii_group["elapsed_time"].values
                for _iii_group_key, _iii_group in _iii_groups
            ]

            _groups_result = f_oneway(*_groups_bests_fitness)

            _results.append(
                {
                    "antigenic_feature_count": _inter_inter_group_key,
                    "antigen_recognition_function": _function,
                    "statistic": _groups_result.statistic,
                    "p": _groups_result.pvalue,
                }
            )

    mo.vstack(
        [
            mo.md(
                "##### Tabla de resultados de ANOVAS de somatic_hypermutation_rate sobre elapsed_time para algoritmo clonal con memoria inmunológica"
            ),
            mo.ui.table(_results),
        ]
    )
    return


@app.cell
def _(FUNCTIONS, clonal_data, f_oneway, mo):
    _results = []

    for _function in FUNCTIONS:
        _groups = clonal_data.groupby("antigen_recognition_function")
        _group = _groups.get_group(_function)

        _inter_groups = _group.groupby("antigenic_feature_count")

        for _inter_inter_group_key, _inter_inter_group in _inter_groups:
            _iii_groups = _inter_inter_group.groupby(
                "somatic_hypermutation_cycles"
            )
            _groups_bests_fitness = [
                _iii_group["elapsed_time"].values
                for _iii_group_key, _iii_group in _iii_groups
            ]

            _groups_result = f_oneway(*_groups_bests_fitness)

            _results.append(
                {
                    "antigenic_feature_count": _inter_inter_group_key,
                    "antigen_recognition_function": _function,
                    "statistic": _groups_result.statistic,
                    "p": _groups_result.pvalue,
                }
            )

    mo.vstack(
        [
            mo.md(
                "##### Tabla de resultados de ANOVAS de somatic_hypermutation_cycles sobre elapsed_time para algoritmo clonal"
            ),
            mo.ui.table(_results),
        ]
    )
    return


@app.cell
def _(FUNCTIONS, clonal_with_memory_data, f_oneway, mo):
    _results = []

    for _function in FUNCTIONS:
        _groups = clonal_with_memory_data.groupby("antigen_recognition_function")
        _group = _groups.get_group(_function)

        _inter_groups = _group.groupby("antigenic_feature_count")

        for _inter_inter_group_key, _inter_inter_group in _inter_groups:
            _iii_groups = _inter_inter_group.groupby(
                "somatic_hypermutation_cycles"
            )
            _groups_bests_fitness = [
                _iii_group["elapsed_time"].values
                for _iii_group_key, _iii_group in _iii_groups
            ]

            _groups_result = f_oneway(*_groups_bests_fitness)

            _results.append(
                {
                    "antigenic_feature_count": _inter_inter_group_key,
                    "antigen_recognition_function": _function,
                    "statistic": _groups_result.statistic,
                    "p": _groups_result.pvalue,
                }
            )

    mo.vstack(
        [
            mo.md(
                "##### Tabla de resultados de ANOVAS de somatic_hypermutation_cycles sobre elapsed_time para algoritmo clonal con memoria inmunológica"
            ),
            mo.ui.table(_results),
        ]
    )
    return


@app.cell
def _(FUNCTIONS, clonal_data, f_oneway, mo):
    _results = []

    for _function in FUNCTIONS:
        _groups = clonal_data.groupby("antigen_recognition_function")
        _group = _groups.get_group(_function)

        _inter_groups = _group.groupby("antigenic_feature_count")

        for _inter_inter_group_key, _inter_inter_group in _inter_groups:
            _iii_groups = _inter_inter_group.groupby("clonal_expansion_factor")
            _groups_bests_fitness = [
                _iii_group["elapsed_time"].values
                for _iii_group_key, _iii_group in _iii_groups
            ]

            _groups_result = f_oneway(*_groups_bests_fitness)

            _results.append(
                {
                    "antigenic_feature_count": _inter_inter_group_key,
                    "antigen_recognition_function": _function,
                    "statistic": _groups_result.statistic,
                    "p": _groups_result.pvalue,
                }
            )

    mo.vstack(
        [
            mo.md(
                "##### Tabla de resultados de ANOVAS de clonal_expansion_factor sobre elapsed_time para algoritmo clonal"
            ),
            mo.ui.table(_results),
        ]
    )
    return


@app.cell
def _(FUNCTIONS, clonal_with_memory_data, f_oneway, mo):
    _results = []

    for _function in FUNCTIONS:
        _groups = clonal_with_memory_data.groupby("antigen_recognition_function")
        _group = _groups.get_group(_function)

        _inter_groups = _group.groupby("antigenic_feature_count")

        for _inter_inter_group_key, _inter_inter_group in _inter_groups:
            _iii_groups = _inter_inter_group.groupby("clonal_expansion_factor")
            _groups_bests_fitness = [
                _iii_group["elapsed_time"].values
                for _iii_group_key, _iii_group in _iii_groups
            ]

            _groups_result = f_oneway(*_groups_bests_fitness)

            _results.append(
                {
                    "antigenic_feature_count": _inter_inter_group_key,
                    "antigen_recognition_function": _function,
                    "statistic": _groups_result.statistic,
                    "p": _groups_result.pvalue,
                }
            )

    mo.vstack(
        [
            mo.md(
                "##### Tabla de resultados de ANOVAS de clonal_expansion_factor sobre elapsed_time para algoritmo clonal con memoria inmunológica"
            ),
            mo.ui.table(_results),
        ]
    )
    return


@app.cell
def _(mo):
    mo.md(r"""Los resultados nos enseñan que la variable somatic_hypermutation_cycles, es la única que tiene efecto sobre el tiempo de busqueda, un efecto previsto, dado que dicha variable controla cuantas iteraciones tiene el ciclo principal tiene el algoritmo. Por otro lado las variables restantes demostraron diferentes poco significativas, lo que significa que solo tendremos que crear un grupo más cuando comparemos el tiempo de busqueda.""")
    return


@app.cell
def _(mo):
    mo.md(r"""Con esto podemos ya, hacer una comparativa justa entre los dos conjuntos de datos, agrupando ambos conjuntos conforme los grupos que hemos descubierto.""")
    return


@app.cell
def _(mo):
    mo.md(r"""Para realizar la comparativa es necesario ocupar métodos análiticos que permitan trabajar con la sobreagrupación y la diferencia de tamaños de los conjuntos de información de ambos algoritmos, por ello se concluyo utilizar la prueba Whitney, la cual permite comparar medias para conjuntos de datos extremadamente pequeños sin estar seguros de que sean normales, aparte también se utilizara la prueba Bootstrap que permite un remuestreo de la información para inferir rangos estadisticos, para este caso, los rangos de mejora.""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        ## Resultados

        Con base en el análizis de datos explicado, nos fue posible llegar a la siguientes tablas de resultados.
        """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""### Tabla de resultados para la aproximación al valor optimo""")
    return


@app.cell
def _(FUNCTIONS, clonal_data, numpy):
    clonal_fitness = []

    for _function in FUNCTIONS:
        _a_groups = clonal_data.groupby("antigen_recognition_function")
        _a_group = _a_groups.get_group(_function)
        _a_inter_groups = _a_group.groupby("antigenic_feature_count")

        for _count, _a_ii_group in _a_inter_groups:
            clonal_fitness.append(
                {
                    "antigen_recognition_function": _function,
                    "antigenic_feature_count": _count,
                    "best_fitness": numpy.abs(
                        numpy.array(_a_ii_group["best_fitness"].values)
                    ),
                }
            )
    return (clonal_fitness,)


@app.cell
def _(FUNCTIONS, clonal_with_memory_data, numpy):
    clonal_with_memory_fitness = []

    for _function in FUNCTIONS:
        _a_groups = clonal_with_memory_data.groupby("antigen_recognition_function")
        _a_group = _a_groups.get_group(_function)
        _a_inter_groups = _a_group.groupby("antigenic_feature_count")

        for _count, _a_ii_group in _a_inter_groups:
            clonal_with_memory_fitness.append(
                {
                    "antigen_recognition_function": _function,
                    "antigenic_feature_count": _count,
                    "best_fitness": numpy.abs(
                        numpy.array(_a_ii_group["best_fitness"].values)
                    ),
                }
            )
    return (clonal_with_memory_fitness,)


@app.cell
def _(FUNCTIONS, clonal_data, numpy):
    clonal_elapsed_time = []

    for _function in FUNCTIONS:
        _a_groups = clonal_data.groupby("antigen_recognition_function")
        _a_group = _a_groups.get_group(_function)
        _a_inter_groups = _a_group.groupby("antigenic_feature_count")

        for _count, _iii_group in _a_inter_groups:
            _a_iiii_groups = _iii_group.groupby("somatic_hypermutation_cycles")

            for _cycles, _iiii_group in _a_iiii_groups:
                _elapsed_time = numpy.array(_iiii_group["elapsed_time"].values)

                clonal_elapsed_time.append(
                    {
                        "antigen_recognition_function": _function,
                        "antigenic_feature_count": _count,
                        "elapsed_time": _elapsed_time,
                    }
                )
    return (clonal_elapsed_time,)


@app.cell
def _(FUNCTIONS, clonal_with_memory_data, numpy):
    clonal_with_memory_elapsed_time = []

    for _function in FUNCTIONS:
        _a_groups = clonal_with_memory_data.groupby("antigen_recognition_function")
        _a_group = _a_groups.get_group(_function)
        _a_inter_groups = _a_group.groupby("antigenic_feature_count")

        for _count, _a_ii_group in _a_inter_groups:
            _a_iiii_groups = _a_ii_group.groupby("somatic_hypermutation_cycles")

            for _cycles, _iiii_group in _a_iiii_groups:
                _elapsed_time = numpy.array(_iiii_group["elapsed_time"].values)
                clonal_with_memory_elapsed_time.append(
                    {
                        "antigen_recognition_function": _function,
                        "antigenic_feature_count": _count,
                        "somatic_hypermutation_cycles": _cycles,
                        "elapsed_time": _elapsed_time,
                    }
                )
    return (clonal_with_memory_elapsed_time,)


@app.cell
def _(
    bootstrap,
    clonal_fitness,
    clonal_with_memory_fitness,
    mannwhitneyu,
    mean_difference,
    pandas,
):
    best_fitness_results = []


    for group_index in range(len(clonal_fitness)):
        _a_group = clonal_fitness[group_index]
        _b_group = clonal_with_memory_fitness[group_index]

        _a_group_values = _a_group["best_fitness"]
        _b_group_values = _b_group["best_fitness"]
        _b_group_values_mean = _b_group_values.mean()

        _mannwhitneyu_result = mannwhitneyu(
            _b_group_values,
            _a_group_values,
            alternative="less",
        )

        _bootstrap_result = bootstrap(
            (_a_group_values, _b_group_values),
            mean_difference,
            n_resamples=10000,
            confidence_level=0.95,
        )

        best_fitness_results.append(
            {
                "antigen_recognition_function": _a_group[
                    "antigen_recognition_function"
                ],
                "antigenic_feature_count": _a_group["antigenic_feature_count"],
                "mannwhitneyu_p_value": _mannwhitneyu_result.pvalue,
                "bootstrap_confidence_interval_low": _bootstrap_result.confidence_interval.low,
                "bootstrap_confidence_interval_high": _bootstrap_result.confidence_interval.high,
            }
        )

    best_fitness_results = pandas.DataFrame(best_fitness_results)
    return best_fitness_results, group_index


@app.cell
def _(mo):
    mo.md(r"""#### Medias comparativas del conjunto de datos de resultados del valor óptimo.""")
    return


@app.cell
def _(best_fitness_results, mo):
    mo.hstack(
        [
            mo.stat(
                value=f"{best_fitness_results["bootstrap_confidence_interval_low"].mean()}, {best_fitness_results["bootstrap_confidence_interval_high"].mean()}",
                label="Media",
            ),
            mo.stat(
                value=f"{best_fitness_results["bootstrap_confidence_interval_low"].median()}, {best_fitness_results["bootstrap_confidence_interval_high"].median()}",
                label="Media ponderada",
            ),
            mo.stat(
                value=f"{best_fitness_results["bootstrap_confidence_interval_low"].min()}, {best_fitness_results["bootstrap_confidence_interval_high"].max()}",
                label="Mínimo y Máximo",
            ),
        ]
    )
    return


@app.cell
def _(mo):
    mo.md(r"""### Tabla de resultados para la aproximación al valor optimo""")
    return


@app.cell
def _(
    bootstrap,
    clonal_elapsed_time,
    clonal_with_memory_elapsed_time,
    mannwhitneyu,
    mean_difference,
    pandas,
):
    elapsed_time_results = []


    for _group_index in range(len(clonal_elapsed_time)):
        _a_group = clonal_elapsed_time[_group_index]
        _b_group = clonal_with_memory_elapsed_time[_group_index]

        _a_group_values = _a_group["elapsed_time"]
        _b_group_values = _b_group["elapsed_time"]

        _b_group_values_mean = _b_group_values.mean()

        _mannwhitneyu_result = mannwhitneyu(
            _a_group_values,
            _b_group_values,
            alternative="greater",
            method="exact",
        )

        _bootstrap_result = bootstrap(
            (_a_group_values, _b_group_values),
            mean_difference,
            n_resamples=10000,
            confidence_level=0.95,
        )

        elapsed_time_results.append(
            {
                "antigen_recognition_function": _a_group[
                    "antigen_recognition_function"
                ],
                "antigenic_feature_count": _a_group["antigenic_feature_count"],
                "mannwhitneyu_p_value": _mannwhitneyu_result.pvalue,
                "bootstrap_confidence_interval_low": _bootstrap_result.confidence_interval.low,
                "bootstrap_confidence_interval_high": _bootstrap_result.confidence_interval.high,
            }
        )

    elapsed_time_results = pandas.DataFrame(elapsed_time_results)
    return (elapsed_time_results,)


@app.cell
def _(mo):
    mo.md(r"""#### Medias comparativas del conjunto de datos de resultados del tiempo de busqueda.""")
    return


@app.cell
def _(elapsed_time_results, mo):
    mo.hstack(
        [
            mo.stat(
                value=f"{elapsed_time_results["bootstrap_confidence_interval_low"].mean()}, {elapsed_time_results["bootstrap_confidence_interval_high"].mean()}",
                label="Media",
            ),
            mo.stat(
                value=f"{elapsed_time_results["bootstrap_confidence_interval_low"].median()}, {elapsed_time_results["bootstrap_confidence_interval_high"].median()}",
                label="Media ponderada",
            ),
            mo.stat(
                value=f"{elapsed_time_results["bootstrap_confidence_interval_low"].min()}, {elapsed_time_results["bootstrap_confidence_interval_high"].max()}",
                label="Mínimo y Máximo",
            ),
        ]
    )
    return


@app.cell
def _(pandas):
    clonal_data = pandas.read_csv(
        "./resources/datasets/clonal-raw-data.csv", index_col=0
    )
    return (clonal_data,)


@app.cell
def _(pandas):
    clonal_with_memory_raw_data = pandas.read_csv(
        "./resources/datasets/clonal-with-memory-raw-data.csv", index_col=0
    )
    return (clonal_with_memory_raw_data,)


@app.cell
def _(pandas):
    clonal_with_memory_data = pandas.read_csv(
        "./resources/datasets/clonal-with-memory-data.csv", index_col=0
    )
    return (clonal_with_memory_data,)


@app.cell
def _(numpy):
    def mean_difference(x, y):
        return numpy.mean(x) - numpy.mean(y)
    return (mean_difference,)


@app.cell
def _():
    import lib.benchmark as benchmarklib
    return (benchmarklib,)


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    import numpy
    import altair
    import pandas
    return altair, numpy, pandas


@app.cell
def _():
    from scipy.stats import (
        f_oneway,
        shapiro,
        norm,
        kstest,
        anderson,
        mannwhitneyu,
        bootstrap,
    )
    return (
        anderson,
        bootstrap,
        f_oneway,
        kstest,
        mannwhitneyu,
        norm,
        shapiro,
    )


@app.cell
def _(altair):
    altair.data_transformers.enable("marimo_csv")
    return


if __name__ == "__main__":
    app.run()
