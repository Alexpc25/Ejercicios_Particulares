package polimorfismo;

public abstract class SeleccionFutbol {

	protected int id;
	protected String nombre;
	protected String apellidos;
	protected int edad;

	// constructores, getter y setter

	public void viajar() {
	     System.out.println("Viajar (Clase Padre)");
	}

	public void concentrarse() {
	     System.out.println("Concentrarse (Clase Padre)");
	}

	// IMPORTANTE -> METODO ABSTRACTO => no se implementa en la clase abstracta pero si en la clases hijas
	public abstract void entrenamiento();

	public void partidoFutbol() {
	     System.out.println("Asiste al Partido de Fútbol (Clase Padre)");
	}
}