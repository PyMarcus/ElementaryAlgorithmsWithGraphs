public class Fila{
    // uma fila de inteiros
    public int[] fila;
    public int index;
    public int tam;

    public Fila(int tamanho){
        this.fila = new int[tamanho];
        this.index = 0;
        this.tam = tamanho;
    }

    public void add(int value){
        // adiciona valor à fila (final)
        if(this.index < this.tam){
            this.fila[this.index] = value;
            this.index += 1;
        }
    }

    public int remove(){
        // remove do inicio
        int primeira_posicao = this.fila[0];
        if(this.fila.length > 0){
            int count = 0;
            for(int i = 1; i < tam; i ++) {
                if(count == i){
                    this.fila[count] = 0;
                }else  this.fila[count] = this.fila[i];
                count++;
            }
        }
        return primeira_posicao;
    }

    public void exibir(){
        // exibe a fila
        System.out.println();
        for(int i = 0; i < this.tam; i++){
            System.out.print(this.fila[i] + " ");
        }
    }
}