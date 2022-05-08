
public class Trabajador extends Persona{
	
	public int salario;
	
	public void consultarClase() {
		Person p= new Person();
		p.Apellidos = "Martín Ruiz";
	}
	
	public void ingresarDinero(int sueldo) {
		this.salario = sueldo;
	}
}
