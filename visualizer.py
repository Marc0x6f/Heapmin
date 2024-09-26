from maxheap import Priority
import random



def gerar_clientes_aleatorios(quantidade):
    fila = Priority()
    
    # Inserir clientes com prioridades aleatórias
    for i in range(1, quantidade + 1):
        prioridade_aleatoria = random.randint(1, 10)
        cliente_nome = f"Cliente {i}"
        fila.insert(prioridade_aleatoria, cliente_nome)

    return fila

fila = gerar_clientes_aleatorios(10)


fila.gerar_arvore_grafica(nome_arquivo="arvore_heap.png")

'''


clientes = gerar_clientes_aleatorios(3)
print("Clientes em ordem de prioridade (da maior para a menor):")
for prioridade, cliente, ordem_chegada in clientes:
    print(f"Prioridade: {prioridade}, Nome: {cliente}, Ordem de chegada: {ordem_chegada}")


'''