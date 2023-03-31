class Tarefa:
    def __init__(self, descricao, prazo):
        self.descricao = descricao
        self.prazo = prazo
        self.concluida = False

    def __str__(self):
        if self.concluida:
            status = "CONCLUÍDA"
        else:
            status = "PENDENTE"
        return f"{self.descricao} ({self.prazo}) - {status}"

class No:
    def __init__(self, tarefa):
        self.tarefa = tarefa
        self.proximo = None

class ListaTarefas:
    def __init__(self):
        self.cabeca = None

    def adicionar_tarefa(self, descricao, prazo):
        nova_tarefa = Tarefa(descricao, prazo)
        novo_no = No(nova_tarefa)

        if self.cabeca is None:
            self.cabeca = novo_no
        else:
            no_atual = self.cabeca
            while no_atual.proximo is not None:
                no_atual = no_atual.proximo
            no_atual.proximo = novo_no

    def remover_tarefa(self, descricao):
        if self.cabeca is None:
            return
        
        if self.cabeca.tarefa.descricao == descricao:
            self.cabeca = self.cabeca.proximo
            return
        
        no_atual = self.cabeca
        while no_atual.proximo is not None:
            if no_atual.proximo.tarefa.descricao == descricao:
                no_atual.proximo = no_atual.proximo.proximo
                return
            no_atual = no_atual.proximo

    def listar_tarefas(self):
        if self.cabeca is None:
            print("Não há tarefas na lista.")
        else:
            no_atual = self.cabeca
            while no_atual is not None:
                print(no_atual.tarefa)
                no_atual = no_atual.proximo

    def marcar_como_concluida(self, descricao):
        no_atual = self.cabeca
        while no_atual is not None:
            if no_atual.tarefa.descricao == descricao:
                no_atual.tarefa.concluida = True
                return
            no_atual = no_atual.proximo

print("Bem-vindo ao gerenciador de tarefas!")
lista_tarefas = ListaTarefas()

while True:
    print("\nSelecione uma opção:")
    print("1. Adicionar tarefa")
    print("2. Remover tarefa")
    print("3. Listar tarefas")
    print("4. Marcar tarefa como concluída")
    print("5. Sair")

    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        descricao = input("Digite a descrição da tarefa: ")
        prazo = input("Digite o prazo da tarefa (dd/mm/aaaa): ")
        lista_tarefas.adicionar_tarefa(descricao, prazo)
        print("Tarefa adicionada com sucesso!")

    elif opcao == "2":
        descricao = input("Digite a descrição da tarefa a ser removida: ")
        lista_tarefas.remover_tarefa(descricao)
        print("Tarefa removida com sucesso!")

    elif opcao == "3":
        lista_tarefas.listar_tarefas()

    elif opcao == "4":
        descricao = input("Digite a descrição da tarefa a ser marcada como concluída: ")
        
def swap_nodes(input_list, val1, val2):
  node1_prev = None
  node2_prev = None
  node1 = input_list.head_node
  node2 = input_list.head_node

  if val1 == val2:
    print("Elements are the same - no swap needed")
    return

  while node1 is not None:
    if node1.get_value() == val1:
      break
    node1_prev = node1
    node1 = node1.get_next_node()

  while node2 is not None:
    if node2.get_value() == val2:
      break
    node2_prev = node2
    node2 = node2.get_next_node()

  if (node1 is None or node2 is None):
    print("Swap not possible - one or more element is not in the list")
    return

  if node1_prev is None:
    input_list.head_node = node2
  else:
    node1_prev.set_next_node(node2)

  if node2_prev is None:
    input_list.head_node = node1
  else:
    node2_prev.set_next_node(node1)

  temp = node1.get_next_node()
  node1.set_next_node(node2.get_next_node())
  node2.set_next_node(temp)        