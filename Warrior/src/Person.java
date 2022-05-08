
public class Person {
	public String Nombre;
	protected String Apellidos;
	private int Edad;
	
	public Person() {
		
	}
	
	public boolean conducir() {
		return Edad >= 18;
	}
}
