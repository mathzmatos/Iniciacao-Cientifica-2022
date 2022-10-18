import csv

dados = [
    {"ano": "Ano", "mês": "Mes", "gasolina_precomedio": "Gasolina_PrecoMedio", "gasolina_desviopadrao": "Gasolina_DesvioPadrao", "gasolina_min": "Gasolina_Min", "gasolina_max": "Gasolina_Max", "valor_dolar": "Valor_Dolar"},
    {"ano": 2017, "mês": "Maio", "gasolina_precomedio": 3.617, "gasolina_desviopadrao": 0.252, "gasolina_min": 2.960, "gasolina_max": 4.999, "valor_dolar": 3.126},
    {"ano": 2017, "mês": "Junho", "gasolina_precomedio": 3.548, "gasolina_desviopadrao": 0.269, "gasolina_min": 2.880, "gasolina_max": 4.799, "valor_dolar": 3.101},
    {"ano": 2017, "mês": "Julho", "gasolina_precomedio": 3.553, "gasolina_desviopadrao": 0.304, "gasolina_min": 2.799, "gasolina_max": 4.950, "valor_dolar": 3.283},
    {"ano": 2017, "mês": "Agosto", "gasolina_precomedio": 3.781, "gasolina_desviopadrao": 0.265, "gasolina_min": 2.999, "gasolina_max": 5.100, "valor_dolar": 3.189},
    {"ano": 2017, "mês": "Agosto", "gasolina_precomedio": 3.781, "gasolina_desviopadrao": 0.265, "gasolina_min": 2.999, "gasolina_max": 5.100, "valor_dolar": 3.189},
    {"ano": 2017, "mês": "Setembro", "gasolina_precomedio": 3.881, "gasolina_desviopadrao": 0.253, "gasolina_min": 3.099, "gasolina_max": 5.200, "valor_dolar": 3.197},
    {"ano": 2017, "mês": "Setembro", "gasolina_precomedio": 3.881, "gasolina_desviopadrao": 0.253, "gasolina_min": 3.099, "gasolina_max": 5.200, "valor_dolar": 3.197},
    {"ano": 2017, "mês": "Outubro", "gasolina_precomedio": 3.895, "gasolina_desviopadrao": 0.250, "gasolina_min": 3.199, "gasolina_max": 5.200, "valor_dolar": 3.125},
    {"ano": 2017, "mês": "Novembro", "gasolina_precomedio": 4.004, "gasolina_desviopadrao": 0.261, "gasolina_min": 3.199, "gasolina_max": 5.200, "valor_dolar": 3.157},
    {"ano": 2017, "mês": "Dezembro", "gasolina_precomedio": 4.085, "gasolina_desviopadrao": 0.256, "gasolina_min": 3.399, "gasolina_max": 5.200, "valor_dolar": 3.283},
    {"ano": 2018, "mês": "Janeiro", "gasolina_precomedio": 4.189, "gasolina_desviopadrao": 0.268, "gasolina_min": 3.499, "gasolina_max": 5.150, "valor_dolar": 3.318},
    {"ano": 2018, "mês": "Fevereiro", "gasolina_precomedio": 4.208, "gasolina_desviopadrao": 0.268, "gasolina_min": 3.479, "gasolina_max": 5.200, "valor_dolar": 3.196},
    {"ano": 2018, "mês": "Marco", "gasolina_precomedio": 4.199, "gasolina_desviopadrao": 0.283, "gasolina_min": 3.479, "gasolina_max": 5.200, "valor_dolar": 3.220},
    {"ano": 2018, "mês": "Abril", "gasolina_precomedio": 4.215, "gasolina_desviopadrao": 0.292, "gasolina_min": 3.397, "gasolina_max": 5.200, "valor_dolar": 3.285},
    {"ano": 2018, "mês": "Maio", "gasolina_precomedio": 4.314, "gasolina_desviopadrao": 0.307, "gasolina_min": 3.369, "gasolina_max": 5.459, "valor_dolar": 3.410},
    {"ano": 2018, "mês": "Junho", "gasolina_precomedio": 4.552, "gasolina_desviopadrao": 0.271, "gasolina_min": 3.599, "gasolina_max": 5.599, "valor_dolar": 3.675},
    {"ano": 2018, "mês": "Julho", "gasolina_precomedio": 4.492, "gasolina_desviopadrao": 0.294, "gasolina_min": 3.649, "gasolina_max": 5.599, "valor_dolar": 3.773},
    {"ano": 2018, "mês": "Agosto", "gasolina_precomedio": 4.447, "gasolina_desviopadrao": 0.302, "gasolina_min": 3.649, "gasolina_max": 5.990, "valor_dolar": 3.874},
    {"ano": 2018, "mês": "Setembro", "gasolina_precomedio": 4.625, "gasolina_desviopadrao": 0.296, "gasolina_min": 3.690, "gasolina_max": 6.290, "valor_dolar": 3.913},
    {"ano": 2018, "mês": "Outubro", "gasolina_precomedio": 4.717, "gasolina_desviopadrao": 0.278, "gasolina_min": 3.899, "gasolina_max": 6.290, "valor_dolar": 4.187},
    {"ano": 2018, "mês": "Novembro", "gasolina_precomedio": 4.590, "gasolina_desviopadrao": 0.296, "gasolina_min": 3.749, "gasolina_max": 6.290, "valor_dolar": 3.733},
    {"ano": 2018, "mês": "Novembro", "gasolina_precomedio": 4.590, "gasolina_desviopadrao": 0.296, "gasolina_min": 3.749, "gasolina_max": 6.290, "valor_dolar": 3.733},
    {"ano": 2018, "mês": "Dezembro", "gasolina_precomedio": 4.365, "gasolina_desviopadrao": 0.307, "gasolina_min": 3.669, "gasolina_max": 6.290, "valor_dolar": 3.792},
    {"ano": 2019, "mês": "Janeiro", "gasolina_precomedio": 4.268, "gasolina_desviopadrao": 0.314, "gasolina_min": 3.390, "gasolina_max": 6.290, "valor_dolar": 3.309},
    {"ano": 2019, "mês": "Fevereiro", "gasolina_precomedio": 4.190, "gasolina_desviopadrao": 0.316, "gasolina_min": 3.397, "gasolina_max": 5.690, "valor_dolar": 3.704},
    {"ano": 2019, "mês": "Marco", "gasolina_precomedio": 4.305, "gasolina_desviopadrao": 0.306, "gasolina_min": 3.499, "gasolina_max": 5.988, "valor_dolar": 3.715},
    {"ano": 2019, "mês": "Abril", "gasolina_precomedio": 4.437, "gasolina_desviopadrao": 0.301, "gasolina_min": 3.599, "gasolina_max": 5.988, "valor_dolar": 3.834},
    {"ano": 2019, "mês": "Maio", "gasolina_precomedio": 4.552, "gasolina_desviopadrao": 0.306, "gasolina_min": 3.699, "gasolina_max": 5.859, "valor_dolar": 3.873},
    {"ano": 2019, "mês": "Junho", "gasolina_precomedio": 4.468, "gasolina_desviopadrao": 0.311, "gasolina_min": 3.679, "gasolina_max": 5.859, "valor_dolar": 4.003},
    {"ano": 2019, "mês": "Julho", "gasolina_precomedio": 4.351, "gasolina_desviopadrao": 0.317, "gasolina_min": 3.569, "gasolina_max": 5.859, "valor_dolar": 3.881},
    {"ano": 2019, "mês": "Agosto", "gasolina_precomedio": 4.316, "gasolina_desviopadrao": 0.308, "gasolina_min": 3.559, "gasolina_max": 5.799, "valor_dolar": 3.746},
    {"ano": 2019, "mês": "Setembro", "gasolina_precomedio": 4.326, "gasolina_desviopadrao": 0.310, "gasolina_min": 3.559, "gasolina_max": 5.799, "valor_dolar": 4.018},
    {"ano": 2019, "mês": "Outubro", "gasolina_precomedio": 4.380, "gasolina_desviopadrao": 0.303, "gasolina_min": 3.629, "gasolina_max": 5.799, "valor_dolar": 4.061},
    {"ano": 2019, "mês": "Novembro", "gasolina_precomedio": 4.413, "gasolina_desviopadrao": 0.291, "gasolina_min": 3.649, "gasolina_max": 5.799, "valor_dolar": 4.148},
    {"ano": 2019, "mês": "Dezembro", "gasolina_precomedio": 4.531, "gasolina_desviopadrao": 0.281, "gasolina_min": 3.699, "gasolina_max": 5.859, "valor_dolar": 4.183},
    {"ano": 2020, "mês": "Janeiro", "gasolina_precomedio": 4.579, "gasolina_desviopadrao": 0.276, "gasolina_min": 3.799, "gasolina_max": 5.899, "valor_dolar": 4.094},
    {"ano": 2020, "mês": "Fevereiro", "gasolina_precomedio": 4.550, "gasolina_desviopadrao": 0.274, "gasolina_min": 3.670, "gasolina_max": 5.899, "valor_dolar": 4.162},
    {"ano": 2020, "mês": "Marco", "gasolina_precomedio": 4.462, "gasolina_desviopadrao": 0.294, "gasolina_min": 3.230, "gasolina_max": 5.889, "valor_dolar": 4.316},
    {"ano": 2020, "mês": "Abril", "gasolina_precomedio": 4.066, "gasolina_desviopadrao": 0.341, "gasolina_min": 2.920, "gasolina_max": 5.889, "valor_dolar": 4.736},
    {"ano": 2020, "mês": "Maio", "gasolina_precomedio": 3.818, "gasolina_desviopadrao": 0.314, "gasolina_min": 2.870, "gasolina_max": 5.690, "valor_dolar": 5.257},
    {"ano": 2020, "mês": "Junho", "gasolina_precomedio": 3.964, "gasolina_desviopadrao": 0.301, "gasolina_min": 2.990, "gasolina_max": 5.690, "valor_dolar": 5.822},
    {"ano": 2020, "mês": "Julho", "gasolina_precomedio": 4.144, "gasolina_desviopadrao": 0.294, "gasolina_min": 3.259, "gasolina_max": 5.690, "valor_dolar": 5.188},
    {"ano": 2020, "mês": "Agosto", "gasolina_precomedio": 4.237, "gasolina_desviopadrao": 0.300, "gasolina_min": 3.370, "gasolina_max": 5.690, "valor_dolar": 5.349},
    {"ano": 2020, "mês": "Setembro", "gasolina_precomedio": 4.528, "gasolina_desviopadrao": "na", "gasolina_min": "na", "gasolina_max": "na", "valor_dolar": 5.385},
    {"ano": 2020, "mês": "Outubro", "gasolina_precomedio": 4.358, "gasolina_desviopadrao": 0.308, "gasolina_min": 3.640, "gasolina_max": 5.199, "valor_dolar": 5.272},
    {"ano": 2020, "mês": "Novembro", "gasolina_precomedio": 4.409, "gasolina_desviopadrao": 0.310, "gasolina_min": 3.590, "gasolina_max": 5.499, "valor_dolar": 5.617},
    {"ano": 2020, "mês": "Dezembro", "gasolina_precomedio": 4.483, "gasolina_desviopadrao": 0.303, "gasolina_min": 3.650, "gasolina_max": 5.499, "valor_dolar": 5.485},
    {"ano": 2021, "mês": "Janeiro", "gasolina_precomedio": 4.622, "gasolina_desviopadrao": 0.294, "gasolina_min": 3.099, "gasolina_max": 5.950, "valor_dolar": 5.096},
    {"ano": 2021, "mês": "Fevereiro", "gasolina_precomedio": 4.951, "gasolina_desviopadrao": 0.346, "gasolina_min": 3.890, "gasolina_max": 6.350, "valor_dolar": 5.271},
    {"ano": 2021, "mês": "Marco", "gasolina_precomedio": 5.484, "gasolina_desviopadrao": 0.358, "gasolina_min": 4.279, "gasolina_max": 6.700, "valor_dolar": 5.381},
    {"ano": 2021, "mês": "Abril", "gasolina_precomedio": 5.448, "gasolina_desviopadrao": 0.353, "gasolina_min": 3.899, "gasolina_max": 6.890, "valor_dolar": 5.629},
    {"ano": 2021, "mês": "Maio", "gasolina_precomedio": 5.604, "gasolina_desviopadrao": 0.341, "gasolina_min": 4.199, "gasolina_max": 6.997, "valor_dolar": 5.623},
    {"ano": 2021, "mês": "Junho", "gasolina_precomedio": 5.687, "gasolina_desviopadrao": 0.331, "gasolina_min": 4.398, "gasolina_max": 6.890, "valor_dolar": 5.270},
    {"ano": 2021, "mês": "Julho", "gasolina_precomedio": 5.807, "gasolina_desviopadrao": 0.354, "gasolina_min": 4.549, "gasolina_max": 6.999, "valor_dolar": 5.087},
    {"ano": 2021, "mês": "Agosto", "gasolina_precomedio": 5.933, "gasolina_desviopadrao": 0.355, "gasolina_min": 4.599, "gasolina_max": 7.219, "valor_dolar": 5.100},
    {"ano": 2021, "mês": "Setembro", "gasolina_precomedio": 6.078, "gasolina_desviopadrao": 0.349, "gasolina_min": 5.049, "gasolina_max": 7.236, "valor_dolar": 5.247},
    {"ano": 2021, "mês": "Outubro", "gasolina_precomedio": 6.341, "gasolina_desviopadrao": 0.402, "gasolina_min": 4.690, "gasolina_max": 7.889, "valor_dolar": 5.257},
    {"ano": 2021, "mês": "Novembro", "gasolina_precomedio": 6.744, "gasolina_desviopadrao": 0.372, "gasolina_min": 5.259, "gasolina_max": 7.999, "valor_dolar": 5.451},
    {"ano": 2021, "mês": "Dezembro", "gasolina_precomedio": 6.670, "gasolina_desviopadrao": 0.364, "gasolina_min": 5.299, "gasolina_max": 7.962, "valor_dolar": 5.419},
    {"ano": 2022, "mês": "Janeiro", "gasolina_precomedio": 6.635, "gasolina_desviopadrao": 0.368, "gasolina_min": 5.489, "gasolina_max": 8.029, "valor_dolar": 5.712},
    {"ano": 2022, "mês": "Fevereiro", "gasolina_precomedio": 6.600, "gasolina_desviopadrao": 0.383, "gasolina_min": 5.579, "gasolina_max": 7.999, "valor_dolar": 5.534},
    {"ano": 2022, "mês": "Marco", "gasolina_precomedio": 7.012, "gasolina_desviopadrao": 0.505, "gasolina_min": 5.190, "gasolina_max": 8.949, "valor_dolar": 5.188},
    {"ano": 2022, "mês": "Abril", "gasolina_precomedio": 7.245, "gasolina_desviopadrao": 0.407, "gasolina_min": 6.099, "gasolina_max": 8.599, "valor_dolar": 5.131},
    {"ano": 2022, "mês": "Maio", "gasolina_precomedio": 7.297, "gasolina_desviopadrao": 0.426, "gasolina_min": 6.199, "gasolina_max": 8.990, "valor_dolar": 4.715},
]


with open("dados_gas_dolar.csv", mode="w") as csvfile:

    fieldnames = dados[0].keys()

    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    for row in dados:
        writer.writerow(row)

        





