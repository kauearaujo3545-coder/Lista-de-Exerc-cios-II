from notificador import Notificador


class NotificadorApp(Notificador):

    def notificar(self, mensagem):
        print(f"Notificação no app: {mensagem}")
