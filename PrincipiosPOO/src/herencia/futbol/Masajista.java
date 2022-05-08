package herencia.futbol;

public class Masajista extends MiembroEquipoFutbol
{

	private String Titulacion;
	private int aniosExperiencia;
	
	public Masajista(int id, String nombre, String apellidos, int edad, String equipo, String titulacion, int aniosExperiencia) {
		super(id, nombre, apellidos, edad, equipo);
		this.Titulacion = titulacion;
		this.aniosExperiencia = aniosExperiencia;
		// TODO Auto-generated constructor stub
	}

	// constructor, getter y setter
	@Override
	public void concentrarse() {
		System.out.println("Concentrarse de Masajista");
	}

	public void viajar() {
		System.out.println("Viajar de Masajista");
	}

	public void darMasaje() {
		System.out.println("Masaje de Masajista");
	}
}