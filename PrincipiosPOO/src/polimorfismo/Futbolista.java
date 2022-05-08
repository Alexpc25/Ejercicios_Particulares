package polimorfismo;

public class Futbolista extends SeleccionFutbol {

	   private int dorsal;
	   private String demarcacion;

	   // constructor, getter y setter

	   @Override
	   public void entrenamiento() {
	      System.out.println("Realiza un entrenamiento (Clase Futbolista)");
	   }

	   @Override
	   public void partidoFutbol() {
	      System.out.println("Juega un Partido (Clase Futbolista)");
	   }

	   public void entrevista() {
	      System.out.println("Da una Entrevista");
	   }
}