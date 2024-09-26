import heapq
import networkx as nx
import matplotlib.pyplot as plt

class Priority:
    def __init__(self):
        self.contador = 0 #para manter a ordem da chegada
        self.heap = []

    def insert(self, prioridade, dados):
        #prioridade é negativa para tranformar em maxheap ja que heapq é por padrao min heap
        heapq.heappush(self.heap,(-prioridade, self.contador, dados))
        self.contador += 1

    def esta_vazia(self):
        # Verifica se a fila está vazia
        return len(self.heap) == 0

    def remover(self):
        #remove o elemento com maior prioridade
        if self.heap:
            prioridade, ordem_chegada, dado = heapq.heappop(self.heap)
            return (-prioridade, ordem_chegada + 1, dado)
        else:
            raise IndexError("Fila vazia")
        
    def __len__(self):
        return len(self.heap)


    def gerar_arvore_grafica(self, nome_arquivo="arvore_heap.png"):
            # Cria um gráfico de árvore binária a partir do heap
            G = nx.DiGraph()  # Grafo direcionado, para mostrar a hierarquia da árvore
            pos = {}  # Posições dos nós para a visualização
            labels = {}  # Labels dos nós (prioridade e dado)

            def adicionar_no(posicao, indice):
                if indice < len(self.heap):
                    prioridade, ordem_chegada, dado = self.heap[indice]
                    # Adiciona o nó atual no gráfico
                    G.add_node(indice)
                    pos[indice] = (indice, -posicao)
                    labels[indice] = f"P:{-prioridade}\nC:{dado}"  # Mostra prioridade e nome

                    # Adiciona o filho esquerdo
                    if 2 * indice + 1 < len(self.heap):
                        G.add_edge(indice, 2 * indice + 1)  # Adiciona uma aresta
                        adicionar_no(posicao + 1, 2 * indice + 1)

                    # Adiciona o filho direito
                    if 2 * indice + 2 < len(self.heap):
                        G.add_edge(indice, 2 * indice + 2)  # Adiciona uma aresta
                        adicionar_no(posicao + 1, 2 * indice + 2)

            adicionar_no(0, 0)  # Começa a partir da raiz (posição 0)

            # Desenha o gráfico
            plt.figure(figsize=(12, 8))
            nx.draw(G, pos, with_labels=True, labels=labels, node_size=2000, node_color="lightblue", font_size=10, font_weight="bold", font_color="black")
            plt.title("Visualização da Árvore Binária (Max-Heap)")

            # Salva a imagem em um arquivo
            plt.savefig(nome_arquivo)
            print(f"Árvore binária salva em {nome_arquivo}")
