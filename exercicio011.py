todo = []

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

        case "4":
            i = int(input("Qual tarefa deseja remover? "))
            if (i < 1 or i > len(todo)):
                print ("Tarefa não existe!")
            else:
                todo.pop(i-1)
                print ("Tarefa {} removida!".format(i))

        case "5":
            print("Programa finalizado")
            break
    