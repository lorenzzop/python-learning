import json

# todo = [] (antigo)

try:
    with open("tarefas.json", "r") as f: #se o arquivo ja existe, inicia a lista a partir dele
        todo = json.load(f) #.load serve pra ler
except:
    todo = [] #se n existe, inicia vazia

while True:

    print("\n  -- TO-DO LIST --")
    print("\n 1 - Adicionar")
    print(" 2 - Listar")
    print(" 3 - Concluir")
    print(" 4 - Remover")
    print(" 5 - Sair")

    op = (input("\nEscolha a opção: "))

    match op:
        case "1":
            tarefa = input("Insira a tarefa: ")

            todo.append({
                "tarefa": tarefa,
                "feito": False
            })

            with open("tarefas.json", "w") as arq: #o with open (...) abre o arquivo no modo escrita (por causa do "w", q apaga o arquivo e reescreve)
                json.dump(todo, arq) #.dump sempre pra salvar

                #outros termos q podem ser usados alem do "w": "a" (append, adiciona sem apagar) e "r" (de leitura)
        
        case "2":

            if not todo:
                print("Sem tarefas ainda!")
            else:
                i = 1
                for tarefa in todo:
                    status = "✔" if (tarefa['feito']) else "❌"
                    print(f"Tarefa {i}: {tarefa['tarefa']} {status}")
                    i += 1
            
        case "3": 
            i = int(input("Qual tarefa deseja concluir? "))
            if (i < 1 or i > len(todo)):
                print ("Tarefa não existe!")
            else:
                todo[i-1]['feito'] = True
                print ("Tarefa {} concluída!".format(i))

            with open("tarefas.json", "w") as arq:
                json.dump(todo, arq)

        case "4":
            i = int(input("Qual tarefa deseja remover? "))
            if (i < 1 or i > len(todo)):
                print ("Tarefa não existe!")
            else:
                todo.pop(i-1)
                print ("Tarefa {} removida!".format(i))

            with open("tarefas.json", "w") as arq:
                json.dump(todo, arq)

        case "5":
            print("Programa finalizado")
            break
    