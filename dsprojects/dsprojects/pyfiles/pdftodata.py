import tabula

dfs = tabula.read_pdf("/Users/stasyaeasley/Desktop/SupprressionCosts_0.pdf", pages='all')

tabula.convert_into("/Users/stasyaeasley/Desktop/SupprressionCosts_0.pdf", "/Users/stasyaeasley/Desktop/Yearly_Suppression_Costs.csv", output_format="csv", pages='all')