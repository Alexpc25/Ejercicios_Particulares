package herencia.futbol;

public class Entrenador extends MiembroEquipoFutbol
{

	private String idFederacion;
	
	public Entrenador(int id, String nombre, String apellidos, int edad, String equipo, String idFederacion) {
		super(id, nombre, apellidos, edad, equipo);
		this.idFederacion = idFederacion;
	}

	public void dirigirPartido() {
		System.out.println("Dirigir partido de Entrenador");
	}

	public void dirigirEntreno() {
		System.out.println("Dirigir entreno de Entrenador");
	}
}