from controller.sistema_controller import SistemaController
from model.cad import Usuario
from view.menu import MenuView

def main():
    model = Usuario()
    view = MenuView()

    controller = SistemaController(model, view)
    controller.iniciar()

if __name__ == "__main__":
    main()