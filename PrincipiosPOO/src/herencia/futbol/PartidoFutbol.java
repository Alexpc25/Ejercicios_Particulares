package herencia.futbol;

public class PartidoFutbol {
	public static int numeroArbitros = 2;
	public String visitante;
	public String local;
	public String resultado;
	public int asistentes;
	
	public PartidoFutbol(String x, String y, String a) {
		visitante = x;
		local = y;
		resultado = a;
	}
	
	public void contarAsistentes(int asistentes) {
		this.asistentes = asistentes;
		numeroArbitros += 1;
	}
	
	public static void incrementarNumeroArbitros() {
		numeroArbitros += 1;
	}
	
}
