import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;


public class GrafoMatrizDeAdjacencia {
    private static final int VERTICES = 4; // quantidade de vértices no grafo
    private char[] vertice = new char[VERTICES]; // armazena texto referente ao vértice
    private int[][] matriz = new int[VERTICES][VERTICES];

     public GrafoMatrizDeAdjacencia(){
        /*
            Construtor público indica a
            posicao dos vértices
         */
        this.vertice[0] = 'A';
        this.vertice[1] = 'B';
        this.vertice[2] = 'C';
        this.vertice[3] = 'D';
    }

    // métodos get
    public int getVERTICES(){
        return this.VERTICES;
    }

    public char getVertice(int p){
         return this.vertice[p];
    }

    public int getMatriz(int l, int c){
         return this.matriz[l][c];
    }

    public void setMatriz(int l, int c,int value){
         this.matriz[l][c] = value;
    }

    private void geraMatriz(){
         /*
            Gera matriz
         */
        for(int line = 0;line < getVERTICES(); line ++){
            for(int column = 0; column < getVERTICES(); column ++){
                this.setMatriz(line, column, 0);
            }
        }
        System.out.println("Matriz gerada!");
    }

    public void exibeGrafo(){
         this.geraMatriz();
        for(int line = 0;line < getVERTICES(); line ++){
            for(int column = 0; column < getVERTICES(); column ++){
                System.out.print(this.getMatriz(line, column));
            }
            System.out.println();
        }
    }

    private void matrizDeAdjacencia(){
         /*
            Matriz composta por 1 e 0, onde um representa as adjancências
         */
        setMatriz(0, 1, 1);
        setMatriz(0, 3, 1);
        setMatriz(1, 0, 1);
        setMatriz(1, 2, 1);
        setMatriz(1, 3, 1);
        setMatriz(2, 1, 1);
        setMatriz(3, 0, 1);
        setMatriz(3, 1, 1);
    }

    public void exibeLigacoes() {
         /*
            exibe ligações no grafo (onde a posicao não é zero)
         */
        this.matrizDeAdjacencia();
        System.out.println("Matriz de adjacência e suas ligações:");
        for (int line = 0; line < getVERTICES(); line++) {
            for (int column = 0; column < getVERTICES(); column++) {
                if (this.matriz[line][column] != 0)
                    System.out.println(this.getVertice(line) + " -> " + this.getVertice(column) + " ");
            }
        }
    }

    public void bfs(){
         /*
            Faz busca em profundidade
          */
        int[] veioDe = new int[this.getVERTICES()];
        boolean[] marcado = new boolean[this.getVERTICES()];
        for(int i = 0; i < marcado.length; i++){
            marcado[i] = false;
        }
        this.buscaProfundidade(veioDe, 0, marcado);
    }

    private void buscaProfundidade(int[] veioDe, int atual,boolean[] marcado){
        marcado[atual] = true; // marca a posicao atual como visitada
         for(int adjacente = 0; adjacente < this.getVERTICES(); adjacente++){  // percorrerá os vizinhos antes
             if(marcado[adjacente] == false && this.getMatriz(atual, adjacente) != 0){ // se for false(n visitado),
                 // e se for diferente de zero(tiver ligacao)
                 veioDe[adjacente] = atual; // veio de recebe atual
                 System.out.println("veio de: " + atual + " para: " + adjacente);
                 this.buscaProfundidade(veioDe, adjacente, marcado); // adjacente subtitui o atual para ser visitado
             }
         }
    }

    public void buscaEmLargura(){
         /*
                A Busca em Largura visita todos os vértices de um grafo, usando como
            critério o vérιice visiιado menos recenιemenιe e cuja vizinhança
            ainda não foi explorada.
            -
            Cada novo vértice visitado é adicionado no final de uma fila Q;
            Cada vértice da fila é removido depois que toda a vizinhança for visitada;
            a busca termina quando a fila estiver vazia
          */
         Queue<Integer> q = new LinkedList<>();
         boolean[] marcados = new boolean[this.getVERTICES()];
         int atual = 0;
         for(int i = 0; i < this.getVERTICES(); i++){
             marcados[i] = false;
         }
         buscaEmLargura(atual, q, marcados);


    }

    private void buscaEmLargura(int atual, Queue<Integer> fila, boolean[] marcados){
        marcados[atual] = true;
        fila.add(atual);
        while(fila.size() > 0){
            atual = fila.remove();
            for(int vizinhos = 0; vizinhos < this.getVERTICES(); vizinhos++){
                //if(this.getMatriz(atual, vizinhos) != 0 && marcados[vizinhos] != false){
                if(this.getMatriz(atual, vizinhos) != 0 && marcados[vizinhos] != true){
                    System.out.println("Atual: " + atual + " para: " + vizinhos);
                    fila.add(vizinhos);
                    marcados[vizinhos] = true;
                }
            }
        }
    }

}
