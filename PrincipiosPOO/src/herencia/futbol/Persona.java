package herencia.futbol;

public class Persona {
	private int id;
	private String Nombre;
	private String Apellidos;
	private int Edad;
	
	public Persona(int id, String nombre, String apellidos, int edad) {
		this.id = id;
		Nombre = nombre;
		Apellidos = apellidos;
		Edad = edad;
	}
	
	public void concentrarse() {
		System.out.println("Concentrarse de Persona");
	}
}
