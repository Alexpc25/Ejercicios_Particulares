
class Libro:
    def __init__(self, n_pags, titulo, autor, editorial, ano_publi, precio, resumen, ISBN, idioma):
        self.n_pags = n_pags
        self.titulo = titulo
        self.autor = autor
        self.editorial = editorial
        self.ano_publi = ano_publi
        self.precio = precio
        self.resumen = resumen
        self.ISBN = ISBN
        self.idioma = idioma

def main():
    lista_libros = []
    lista_libros.extend([Libro(720, "El_Mentalista", "Camilla", "Planeta", 2022, 29, "", 12345, "Español"),
                          Libro(32, "Rip Van Winkle", "Boris Johnson", "Pearson", 2008, 12, "", 24571, "Inglés"),
                          Libro(346, "La casa de Pepa Pig", "Federico García Lorca", "Barco de Papel", 2022, 23, "",
                                3571, "Español"),
                          Libro(666, "El retorno de Pepa Pig", "Pedro Sanchez", "Planeta", 2025, 23, "", 3179,
                                "Esperanto")])
    elec1 = input(
        "Elija la característica a buscar en nuestra biblioteca: n_pags/titulo/autor/ editorial/ano_publi/precio/resumen/ISBN/idioma: ")

    elec2 = input("Este es la característica elejida " + elec1 + ", especifique un valor concreto: ")

    for i in lista_libros:
        carac = getattr(i, elec1)

        if carac == elec2:
            print(i.titulo)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

