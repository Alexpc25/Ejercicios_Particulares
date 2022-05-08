package polimorfismo;

public class Entrenador extends SeleccionFutbol {

	   private int idFederacion;

	   // constructor, getter y setter
		
	   @Override
	   public void entrenamiento() {
	      System.out.println("Dirige un entrenamiento (Clase Entrenador)");
	   }

	   @Override
	   public void partidoFutbol() {
	      System.out.println("Dirige un Partido (Clase Entrenador)");
	   }

	   public void planificarEntrenamiento() {
	      System.out.println("Planificar un Entrenamiento");
	   }
}