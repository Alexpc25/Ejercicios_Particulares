package herencia.futbol;

public class Principal {

	public static void main(String[] args) {
		Persona persona1 = new Futbolista(1, "Cristiano", "Ronaldo", 35, "United", 7, "delantero");
		Entrenador persona2 = new Entrenador(2, "Cholo", "Simeone", 65, "Atletico de Madrid", "FEF");
		Persona persona3 = new Masajista(3, "Juan", "Pelopo", 43, "Real Madrid", "Fisioterapia", 20);
		Masajista persona4 = new Masajista(3, "Juan", "Pelopo", 43, "Real Madrid", "Fisioterapia", 20);
	}

}
