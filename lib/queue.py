class Queue:
    """        
        ESTRUTURAS DE DADOS FILA        
        - Fila é uma lista linear de acesso restrito, que permite apenas as operações        
          de enfileiramento (enqueue) e desenfileiramento (dequeue), a primeira        
          ocorrendo no final da estrutura e a segunda no início da estrutura.        
        - Como consequência, a fila funciona pelo princípio FIFO (First In, First Out         
        - primeiro a entrar, primeiro a sair).        
        - A principal aplicação das filas são tarefas que envolvem o processamento de        
          tarefas por ordem de chegada.    
    """

    """
        Construtor da classe
    """
    def __init__(self):
        self.__data = [] # Inicializa uma lista privada vazia

    """
        Método para inserção
        O nome do método para inserção em filas é padronizado: enqueue()
    """
    def enqueue(self, val):
        self.__data.append(val)     # Insere no final da fila

    """
        Método para retirada
        O nome do método de retirada em filas também é padronizado: dequeue()
    """
    
    def dequeue(self):
        if self.is_empty(): return None
        # Retorna e retorna o primeiro elemeno da fila
        return self.__data.pop(0)

    """
        Método para consultar o inicio da fila (primeiro elemento), sem retirá-lo
        Nome padronizado: peek()
    """
    def peek(self):
        if self.is_empty(): return None
        return self.__Data[0]

    """
        Método para verificar se a fila está vazia ou não
        Retorna True se vazia ou false caso contrário
    """
    def is_empty(self):
        return len(self.__data) ==0

    """
        Método que exibe a fila como uma string (para fins de depuração)
    """
        def to_str(self):
            string = ""
            for el in self.__data:
                if string != "": string += ", "
                string += str(el)
            return "[ " + string + " ]"

    ##########################################

    fila = Queue()  # Cria uma nova fila
    print(fila.to.str())


    # Adicionando pessoas à fila
    fila.enqueue("Marciovaldo")
    fila.enqueue("Gildanete")
    fila.enqueue("Terencionildo")
    fila.enqueue("Junislerton")
    fila.enqueue("Ritielaine")

    print(fila.to_str())

    atendido = fila.dequeue(
    print(f"Atendido: {atendido")
    print(fila.to_str())

    atendido = fila.dequeue()
    print(f"Atendido: {atendido}")
    print(fila.to.str)

    fila.enqueue("Adenoirton")
    print(fila.to_str())

    proximo = fila.peek()
    print(f"Próximo a ser atendido: {proximo}")
    print(fila.to_str())