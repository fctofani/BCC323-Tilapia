import globalContent

from employee import Employee
from commonEmployee import CommonEmployee
from items import Items


class AdminEmployee(Employee):
    def __init__(self):
        super().__init__()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def createCommonEmployee(self, **kwargs):
        common = CommonEmployee(**kwargs)
        globalContent.database.employeeContainer.append(common)

    def createAdminEmployee(self, **kwargs):
        admin = AdminEmployee(**kwargs)
        globalContent.database.employeeContainer.append(admin)

    def deleteEmployee(self, empid):
        for i in globalContent.database.employeeContainer:
            if i.id == empid:
                globalContent.database.employeeContainer.remove(i)
                return True
        return False

    def searchEmployee(self, empid):
        for i in globalContent.database.employeeContainer:
            if i.id == empid:
                return i

    def updateEmployee(self,
                       employee, first_name="", last_name="", id=-1):

        for i in globalContent.database.employeeContainer:

            if i == employee:

                if first_name == "":
                    i.first_name = i.first_name
                else:
                    i.first_name = first_name
                if last_name == "":
                    i.last_name = i.last_name
                else:
                    i.last_name = last_name
                if id == -1:
                    i.id = i.id
                else:
                    i.id = id

    def listEmployees(self):
        print("\n------Lista de funcionários-------\n")
        idx = 1
        for i in globalContent.database.employeeContainer:
            print('(' + str(idx) + ')' + str(i))
            idx = idx + 1

    def createItem(self, item_name, id_item, value, description, status):
        item = Items(id_item, item_name, value, description, status)
        globalContent.database.itemsContainer.append(item)

    def deleteItem(self, id_item):
        for i in globalContent.database.itemsContainer:
            if i.id_item == id_item:
                if i.status == 'rented':
                    return False
                else:
                    globalContent.database.itemsContainer.remove(i)
                    return True
        return False

    def showMenu(self):  # Menu admin
        while (True):
            option = input('\n----- MENU ADMIN ----- \n'
                           + '(1) - Itens Admin\n'
                           + '(2) - Clientes\n'
                           + '(3) - Funcionários\n'
                           + '(4) - Itens\n'
                           + '(5) - SAIR\n')

            if (option == '1'):
                self.showmenuAdminItem()
            elif (option == '2'):
                self.showMenuClients()
            elif (option == '3'):
                self.showMenuEmployees()
            elif (option == '4'):
                self.showMenuItems()
            else:
                break

    def showMenuEmployees(self):
        while (True):
            option = input('----- MENU FUNCIONARIO ----- \n'
                           + '(1) - Listar Funcionários\n'
                           + '(2) - Adicionar Funcionário\n'
                           + '(3) - Editar Funcionário\n'
                           + '(4) - Remover Funcionário\n'
                           + '(5) - SAIR\n')

            if (option == '1'):
                self.listEmployees()

            elif (option == '2'):
                print("\n novo funcionário: \n")
                name = input("digite o nome: \n")
                lastname = input("digite o ultimo nome:\n")
                empid = len(globalContent.database.employeeContainer) + 1

                emp = self.createCommonEmployee(first_name=name, last_name=lastname, id=empid)
                if emp:
                    self.listEmployees()
                else:
                    print("erro ao inserir")

            elif (option == '3'):
                empid = input("digite o id\n")

                emp = self.searchEmployee(int(empid))
                if emp:
                    name = input("digite o nome: \n")
                    lastname = input("digite o ultimo nome:\n")
                    idemp = int(empid)
                    print(emp)

                    self.updateEmployee(employee=emp, first_name=name, last_name=lastname, id=idemp)
                    self.listEmployees()
                else:
                    print("nao encontrado")
            elif (option == '4'):
                empid = input("digite o id\n")

                rememp = self.deleteEmployee(int(empid))
                if rememp:
                    self.listEmployees()
                    print("removido")
                else:
                    print("nao encontrado")
            else:
                break

    def showmenuAdminItem(self):
        while (True):
            option = input('------MENU ITENS ------- \n'
                           + '(1) - adicionar itens \n'
                           + '(2) - remover itens \n'
                           + '(3) - sair\n')

            if (option == '1'):
                name = input('digite o nome do item:\n')
                itemid = (len(globalContent.database.itemsContainer) + 1)
                value = input('digite o valor:\n')
                description = input('digite a descrição\n')

                self.createItem(item_name=name, id_item=itemid,
                                value=value,
                                description=description,
                                status='available')
                self.listItems()

            elif (option == '2'):
                itemid = int(input('id para remover\n'))
                self.deleteItem(itemid)
                self.listItems()
            else:
                break
