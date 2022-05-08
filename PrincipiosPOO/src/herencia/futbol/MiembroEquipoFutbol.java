package herencia.futbol;

public abstract class MiembroEquipoFutbol extends Persona{
	public String equipo;
	
	public MiembroEquipoFutbol(int id, String nombre, String apellidos, int edad, String equipo) {
		super(id, nombre, apellidos, edad);
		this.equipo = equipo;
	}
	
	@Override
	public void concentrarse() {
		System.out.println("Concentrarse de Miembro de Equipo");
	}
	
	public void darRuedaPrensa() {
		System.out.println("Dar Rueda de Prensa de Miembro de Equipo");
	}
	
	public void viajar() {
		System.out.println("Viajar de Miembro de Equipo");
	}
	
}
