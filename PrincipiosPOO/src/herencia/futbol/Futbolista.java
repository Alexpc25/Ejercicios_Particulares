package herencia.futbol;

public class Futbolista extends MiembroEquipoFutbol
{

	private int dorsal;
	private String demarcacion;

	// constructor, getter y setter
	
	public Futbolista(int id, String nombre, String apellidos, int edad, String equipo, int dorsal, String demarcacion) {
		super(id, nombre, apellidos, edad, equipo);
		this.dorsal = dorsal;
		this.demarcacion = demarcacion;
	}

	public void jugarPartido() {
		System.out.println("Jugar partido de Futbolista");
	}

	public void entrenar() {
		System.out.println("Entrenar de Futbolista");
	}
}