
public class Trabajador extends Persona{
	
	public int salario;
	
	public void consultarClase() {
		Person p= new Person();
		p.Apellidos = "Mart�n Ruiz";
	}
	
	public void ingresarDinero(int sueldo) {
		this.salario = sueldo;
	}
}
